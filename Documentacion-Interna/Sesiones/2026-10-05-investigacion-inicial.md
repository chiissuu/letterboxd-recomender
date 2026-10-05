# 2026-10-05 — Investigación inicial

## Objetivo

Determinar si Letterboxd Checker puede repetir la comparación social de Instagram/GitHub y si es viable automatizar consultas o unfollows.

## Hallazgos

- Export oficial disponible como ZIP de CSV.
- Las fuentes oficiales no confirman que el export incluya seguidores/seguidos.
- API con endpoints sociales y OAuth2, pero acceso por solicitud.
- Letterboxd declara que actualmente no concede API a proyectos personales de análisis.
- Términos prohíben scraping y recopilación automatizada no autorizada.

## Trabajo creado

- README provisional y `.gitignore` para datos privados.
- Inspector local del ZIP, sin mostrar valores.
- Pruebas unitarias sintéticas.
- Documentación de contexto, investigación, decisiones, funcionamiento y pendientes.

## Próximo paso

El inspector se ejecutó sobre la exportación real: 17 CSV, sin archivos ni cabeceras de seguidores/seguidos. `profile.csv` contiene datos personales y el export permanece gitignorado.

El checker social no puede construirse desde el ZIP. No se automatizarán las páginas públicas porque los términos prohíben la extracción automatizada. Queda decidir si el proyecto pivota hacia análisis de actividad cinematográfica.

