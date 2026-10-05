import csv
import io
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout
from pathlib import Path

import inspector_export


class PruebasInspector(unittest.TestCase):
    def crear_zip(self, carpeta: str) -> Path:
        ruta = Path(carpeta) / "export.zip"
        with zipfile.ZipFile(ruta, "w") as archivo:
            archivo.writestr("diary.csv", "Date,Name,Year\n2026-01-01,Ejemplo,2025\n")
            archivo.writestr("lists/list.csv", "Name,Year\nEjemplo,2025\n")
            archivo.writestr("nota.txt", "ignorar")
        return ruta

    def test_enumera_csv_y_no_muestra_valores(self):
        with tempfile.TemporaryDirectory() as carpeta:
            resultados = inspector_export.inspeccionar_zip(self.crear_zip(carpeta))
        self.assertEqual([r["archivo"] for r in resultados], ["diary.csv", "lists/list.csv"])
        self.assertEqual(resultados[0]["cabeceras"], ["Date", "Name", "Year"])
        self.assertEqual(resultados[0]["filas"], 1)
        salida = io.StringIO()
        with redirect_stdout(salida):
            inspector_export.mostrar(resultados)
        self.assertNotIn("Ejemplo", salida.getvalue())

    def test_zip_invalido(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "mal.zip"
            ruta.write_text("no es zip", encoding="utf-8")
            with self.assertRaises(ValueError):
                inspector_export.inspeccionar_zip(ruta)


if __name__ == "__main__":
    unittest.main()

