# Letterboxd Recommender

Proyecto futuro de análisis de datos y recomendación cinematográfica a partir de la exportación oficial de una cuenta de Letterboxd.

El objetivo será construir localmente un perfil de gustos explicable y recomendar diez películas todavía no vistas. Los datos propios procederán del ZIP oficial de Letterboxd y los metadatos cinematográficos podrán obtenerse de TMDB. No se automatizará ni raspará la web de Letterboxd.

## Estado

Idea documentada y aparcada hasta que el usuario decida continuar. La exportación real ya fue inspeccionada: contiene películas vistas, valoraciones, watchlist, perfil y una lista personal, suficiente para plantear un recomendador basado en contenido.

La visión completa está en [Documentacion-Interna/Vision-Recomendador.md](Documentacion-Interna/Vision-Recomendador.md).

## Inspector disponible

Descarga tus datos desde [Export your data](https://letterboxd.com/user/exportdata/) y guarda el ZIP dentro de `exports/`. No lo descomprimas ni lo subas a Git.

```powershell
python inspector_export.py "exports\letterboxd-export.zip"
```

El inspector solo muestra nombres de CSV, cabeceras y número de filas. No imprime reseñas, películas, usuarios ni otros valores personales.

## Documentación interna

Empieza por [Documentacion-Interna/Inicio.md](Documentacion-Interna/Inicio.md).

