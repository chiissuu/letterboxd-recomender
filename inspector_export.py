# ==================================================
# 1. PREPARACIÓN Y DATOS
# ==================================================

from __future__ import annotations

import argparse
import csv
import io
import sys
import zipfile
from pathlib import Path

NOMBRES_SOCIALES = ("follower", "following", "friend", "network")


# ==================================================
# 2. INSPECCIÓN DE LA EXPORTACIÓN
# ==================================================

# 2.1. Lectura segura de un CSV

def resumir_csv(nombre: str, archivo_binario) -> dict:
    texto = io.TextIOWrapper(archivo_binario, encoding="utf-8-sig", newline="")
    lector = csv.reader(texto)
    cabeceras = next(lector, [])
    filas = sum(1 for _ in lector)
    return {"archivo": nombre, "cabeceras": cabeceras, "filas": filas}


# 2.2. Inspección del ZIP sin extraerlo

def inspeccionar_zip(ruta: Path) -> list[dict]:
    resultados = []
    try:
        with zipfile.ZipFile(ruta) as exportacion:
            for entrada in sorted(exportacion.infolist(), key=lambda item: item.filename.casefold()):
                if entrada.is_dir() or not entrada.filename.casefold().endswith(".csv"):
                    continue
                with exportacion.open(entrada) as archivo:
                    resultados.append(resumir_csv(entrada.filename, archivo))
    except (OSError, zipfile.BadZipFile, UnicodeError, csv.Error) as error:
        raise ValueError("No se pudo leer la exportación como un ZIP de CSV válido.") from error
    return resultados


# ==================================================
# 3. CONSOLA
# ==================================================

# 3.1. Presentación sin datos personales

def mostrar(resultados: list[dict]) -> None:
    if not resultados:
        print("No se encontraron archivos CSV.")
        return
    print(f"CSV encontrados: {len(resultados)}")
    for resultado in resultados:
        cabeceras = ", ".join(resultado["cabeceras"]) or "sin cabeceras"
        print(f"- {resultado['archivo']} | filas: {resultado['filas']} | cabeceras: {cabeceras}")
    sociales = [r["archivo"] for r in resultados if any(
        palabra in r["archivo"].casefold() for palabra in NOMBRES_SOCIALES
    )]
    if sociales:
        print("Posibles archivos sociales: " + ", ".join(sociales))
    else:
        print("No se detectaron archivos con nombres de seguidores o seguidos.")


# 3.2. Punto de entrada

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Inspecciona la estructura de una exportación de Letterboxd sin mostrar sus datos."
    )
    parser.add_argument("exportacion", type=Path, help="Ruta al ZIP descargado de Letterboxd.")
    args = parser.parse_args(argv)
    try:
        mostrar(inspeccionar_zip(args.exportacion))
        return 0
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

