# Contexto

## Origen

Proyecto inspirado en Instagram Checker y GitHub Checker. El objetivo planteado es averiguar si puede analizarse la relación seguidores/seguidos de Letterboxd y, si fuera posible, ayudar a gestionar quienes no siguen de vuelta.

## Diferencia fundamental

Instagram proporciona una exportación con seguidores y seguidos. GitHub dispone de una API pública apropiada. Letterboxd exporta los datos propios en CSV, pero sus fuentes oficiales no afirman que incluya el grafo social. Su API requiere aprobación y excluye expresamente proyectos personales de análisis en este momento.

## Alcance provisional

La exportación real confirmó que no existe información social. El usuario decidió dejar a un lado el checker y conservar una nueva idea para desarrollar más adelante: analizar sus gustos y generar diez recomendaciones personalizadas.

El proyecto futuro usará Python, ejecución local y la exportación oficial. Podrá enriquecer películas mediante la API de TMDB, sin login automatizado, cookies ni scraping de Letterboxd. Ver [Visión del recomendador](Vision-Recomendador.md).

