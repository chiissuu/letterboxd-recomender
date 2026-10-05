# Decisiones

## No automatizar Letterboxd

No se harán peticiones automatizadas a la web, scraping ni navegador con sesión. Los términos lo prohíben salvo autorización. Tampoco se investigarán endpoints internos ni se almacenarán cookies.

## No solicitar la API por ahora

La propia página de acceso indica que no concede credenciales para proyectos personales de análisis. La arquitectura queda preparada conceptualmente para revisarse si cambia esa política, sin implementar un cliente inutilizable.

## Exportación como fuente de verdad

El ZIP oficial es la única entrada prevista. Se mantiene fuera de Git mediante `.gitignore`. No se publicarán películas, reseñas, listas, nombres de usuarios ni estadísticas derivadas de una cuenta real.

## Verificar antes de diseñar

No asumir nombres o columnas. `inspector_export.py` muestra únicamente estructura, cabeceras y recuentos. El checker definitivo se decidirá tras ejecutar ese inspector sobre una exportación actual.

## Sin unfollow automático

Aunque la API documenta una operación para modificar relaciones, no tenemos acceso autorizado. Si el objetivo social no puede resolverse con datos exportados, la acción será manual desde la interfaz oficial.

## Cambio de objetivo

El checker social queda aparcado. La carpeta pasa a representar un recomendador cinematográfico basado en los datos propios exportados. La investigación sobre seguidores se conserva porque explica por qué se produjo el cambio.

## Recomendador explicable

El núcleo será un algoritmo reproducible y evaluable. Una IA generativa podrá redactar el análisis narrativo de forma opcional, pero no será la única responsable de seleccionar las películas.

## TMDB para metadatos

Letterboxd recomienda TMDB para datos de películas. Si se implementa, el token se leerá desde `TMDB_API_TOKEN`, se guardará una caché gitignorada y se añadirá la atribución exigida por TMDB. No se enviará el ZIP completo a servicios externos.

