# Funcionamiento

## Inspector actual

`inspector_export.py` recibe la ruta de un ZIP, lo abre sin extraer archivos, localiza entradas `.csv` y muestra:

- ruta relativa dentro del ZIP;
- nombres de columnas;
- cantidad de filas.

No imprime valores de las filas. Detecta de forma orientativa nombres que contengan `follower`, `following`, `friend` o `network`. La ausencia de esos nombres no demuestra por sí sola que no haya información social; habrá que revisar las cabeceras mostradas.

## Flujo previsto

1. El usuario genera el export oficial.
2. Guarda el ZIP en `exports/`, carpeta gitignorada.
3. Ejecuta el inspector.
4. Se documenta la estructura observada sin copiar valores personales.
5. Se define una funcionalidad mínima según los archivos existentes.
6. El futuro checker lee CSV localmente y escribe resultados gitignorados.

## Privacidad

No hay red en el inspector. El ZIP no se extrae, modifica o copia. Las pruebas crean un ZIP sintético temporal.

