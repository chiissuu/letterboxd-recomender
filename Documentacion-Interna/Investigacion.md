# Investigación

Consulta realizada el 5 de octubre de 2026.

## Exportación oficial

Letterboxd permite generar un ZIP con documentos CSV desde [Export your data](https://letterboxd.com/user/exportdata/). Indica que incluye perfil, películas, reseñas, listas y más, además de contenido eliminado y reseñas de títulos eliminados. Su [FAQ oficial](https://letterboxd.com/about/faq/) confirma que la exportación reúne la cuenta completa en CSV.

Las fuentes oficiales no enumeran todos los archivos ni confirman seguidores y seguidos. Ejemplos públicos de herramientas que consumen el export describen normalmente `diary.csv`, `watched.csv`, `ratings.csv`, `reviews.csv`, `watchlist.csv`, `profile.csv`, `comments.csv` y carpetas de listas, likes, contenido eliminado y huérfano. Esto es evidencia secundaria y debe verificarse con el ZIP del usuario.

## API oficial

Existe una [API documentada](https://api-docs.letterboxd.com/) con OAuth2. Técnicamente ofrece consulta paginada de miembros seguidos y seguidores mediante `/members`, y modificación de la relación con otro miembro mediante `PATCH /member/{id}/me` con autenticación y permiso `content:modify`.

El obstáculo es el acceso: la [página oficial de solicitud](https://letterboxd.com/api-beta/) dice que se concede solo previa solicitud y que actualmente no aceptan proyectos privados o personales, de análisis, visualización o recomendaciones. Por tanto, no se puede plantear hoy como GitHub Checker con una credencial que cualquier usuario genere.

## Automatización de la web

Los [términos de uso](https://letterboxd.com/legal/terms-of-use/) actualizados en diciembre de 2025 prohíben usar robots, spiders, scrapers u otras herramientas automáticas de recopilación o monitorización salvo autorización explícita. También permiten suspender o limitar cuentas por incumplimiento.

Conclusión: no usar `requests`, Playwright, Selenium, cookies de sesión ni endpoints internos para recorrer seguidores o ejecutar unfollows. Pausas o movimientos “humanos” no convierten esa automatización en autorizada.

## Metodologías posibles

1. **Export local:** vía principal, privada y repetible. Adecuada para analizar actividad cinematográfica. Solo servirá para relaciones sociales si el ZIP real contiene esos datos.
2. **API oficial:** técnicamente ideal para seguidores y unfollow, pero bloqueada mientras Letterboxd no apruebe el proyecto.
3. **Proceso manual:** si el export no contiene relaciones, revisar las páginas Following/Followers en la interfaz y actuar manualmente. El programa no debe recopilar esas páginas.
4. **RSS:** Letterboxd ofrece feeds de nuevas entradas, reseñas y listas; no resuelven la comparación de seguidores.

## Exportación real inspeccionada

El 5 de octubre de 2026 se inspeccionó el ZIP real del usuario sin extraerlo ni mostrar valores. Contiene 17 CSV relacionados con perfil, diario, películas vistas, valoraciones, reseñas, watchlist, comentarios, likes, una lista y contenido eliminado o huérfano.

No contiene archivos cuyos nombres indiquen seguidores, seguidos, amigos o red. Tampoco aparecen columnas sociales en las cabeceras. `profile.csv` sí contiene campos personales como nombre, correo, ubicación, web y biografía; todo el directorio `exports/` debe permanecer gitignorado.

Conclusión confirmada para este export: no es posible calcular `following - followers` a partir de los datos oficiales descargados.

## Páginas públicas de relaciones

Las rutas `/chiissuu/following/` y `/chiissuu/followers/` muestran la información necesaria en la interfaz. Técnicamente un programa podría descargar y recorrer su HTML, pero eso sería una herramienta automatizada de extracción. La cláusula 6.11 de los términos prohíbe robots, spiders, scrapers y otros programas de recopilación salvo autorización explícita.

Que las páginas sean públicas no concede permiso para automatizar su recopilación. Tampoco lo solucionan pausas, un navegador real o movimientos que simulen una persona. La revisión debe hacerse manualmente en la interfaz o mediante la API oficial si Letterboxd concede acceso por escrito en el futuro.

