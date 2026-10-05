# Visión — Letterboxd Recommender

## Idea central

Analizar localmente una exportación personal de Letterboxd, construir un perfil cinematográfico explicable y recomendar diez películas todavía no vistas.

El proyecto combina tratamiento de datos, consumo de una API externa, ingeniería de características, algoritmos de recomendación, evaluación, privacidad y presentación de resultados. Está pensado como proyecto educativo y de portfolio.

## Resultado esperado

Una ejecución futura podría ser:

```powershell
python recommender.py --top 10
```

Y producir:

```text
resultados/
├── perfil_de_gustos.json
├── recomendaciones.csv
└── informe_recomendaciones.html
```

Cada recomendación debe incluir puntuación y motivos verificables:

```text
1. Película de ejemplo (2003)
   Compatibilidad estimada: 92 %

   Motivos:
   - Afinidad con thrillers criminales.
   - Director o reparto presentes en películas muy valoradas.
   - Temas similares a varias favoritas.
   - No aparece entre las películas vistas.
```

## Datos disponibles

El export real inspeccionado contiene suficientes señales para una primera versión:

- 218 valoraciones;
- 219 películas vistas;
- 48 películas en la watchlist;
- una lista personal con más de cien entradas;
- películas favoritas dentro de `profile.csv`.

También existen diario, reseñas, comentarios y likes, aunque en este export varios están vacíos. Los datos personales de `profile.csv`, como correo o ubicación, no son necesarios y deben ignorarse.

## Metadatos externos

El export aporta principalmente título, año, valoración y URL. Para conocer género, dirección, reparto, palabras clave, idioma, país, duración y sinopsis se propone usar la API oficial de TMDB.

TMDB permite uso no comercial con atribución. La aplicación deberá incluir:

> This product uses the TMDB API but is not endorsed or certified by TMDB.

El token se guardará en `TMDB_API_TOKEN`. Nunca se escribirá en código, `.env` versionado o resultados. Los metadatos descargados se guardarán en una caché local para evitar peticiones repetidas.

## Flujo de datos

1. Leer el ZIP o los CSV locales.
2. Combinar `ratings.csv`, `watched.csv`, `watchlist.csv`, favoritos y listas.
3. Normalizar títulos, años, fechas y valoraciones.
4. Resolver cada película contra TMDB usando título y año.
5. Marcar coincidencias dudosas para revisión manual.
6. Enriquecer las coincidencias con metadatos cinematográficos.
7. Construir el perfil de gustos.
8. Generar películas candidatas.
9. Excluir títulos ya vistos y aplicar filtros.
10. Puntuar, diversificar y explicar las diez mejores.

## Señales del perfil

| Señal | Interpretación inicial |
|---|---|
| 4.5–5 estrellas | Preferencia muy fuerte |
| 4 estrellas | Preferencia positiva |
| 3 estrellas | Señal aproximadamente neutral |
| Menos de 2.5 | Características que podrían penalizarse |
| Película favorita | Peso especial |
| Lista `lifechangers` | Preferencia fuerte, pendiente de interpretar con el usuario |
| Rewatch | Interés adicional |
| Watchlist | Curiosidad, sin considerarla gusto confirmado |

Las características posibles incluyen géneros, directores, actores, palabras clave, décadas, idiomas, países y duración. Las valoraciones bajas también son importantes: evitan confundir frecuencia con preferencia.

## Generación de candidatas

Combinar dos fuentes:

1. Películas relacionadas con las mejor valoradas mediante las recomendaciones de TMDB.
2. Búsquedas con TMDB Discover usando géneros, personas, idiomas, países y palabras clave dominantes.

Después excluir:

- películas ya vistas;
- coincidencias de identidad dudosa;
- títulos con una señal pública insuficiente;
- contenido adulto salvo configuración explícita;
- opcionalmente, películas ya presentes en la watchlist.

## Puntuación inicial

Una primera fórmula explicable:

```text
70 % similitud con el perfil
15 % afinidad con películas favoritas
10 % confianza de las valoraciones públicas
 5 % diversidad dentro del top final
```

Los porcentajes serán hipótesis iniciales, no valores definitivos. El resultado debe conservar un desglose por componente para poder explicar y ajustar cada recomendación.

La diversidad evitará devolver diez películas casi idénticas, de la misma saga o del mismo director. Puede aplicarse como una fase de reordenación después de obtener las puntuaciones individuales.

## Evaluación

El proyecto debe demostrar si recomienda bien:

1. Separar temporalmente una parte de las películas ya valoradas.
2. Construir el perfil con las restantes.
3. Tratar las películas ocultas como candidatas conocidas para evaluación.
4. Comprobar si coloca arriba las valoradas con 4 o 5 estrellas.
5. Comparar con líneas base sencillas: popularidad y género dominante.

Posibles métricas: precision@10, recall@10, NDCG@10 y cobertura. Para evitar usar información futura, es preferible una separación temporal cuando haya fechas suficientes.

## Papel opcional de una IA generativa

El algoritmo de recomendación debe funcionar sin IA generativa. Esto permite reproducir resultados, medir calidad y explicar puntuaciones.

Una IA podría añadirse después para:

- redactar el perfil de gustos en lenguaje natural;
- resumir patrones ya calculados;
- convertir el desglose de una recomendación en una explicación agradable.

Si se usa un servicio externo, enviar únicamente características derivadas y resultados necesarios. No enviar `profile.csv`, correo, ubicación ni el ZIP completo.

## Fases de desarrollo

### Fase 1 — Ingesta local

Leer y combinar los CSV, validar columnas, deduplicar películas y producir un catálogo personal normalizado.

### Fase 2 — Enriquecimiento con TMDB

Crear la credencial, hacer búsquedas por título/año, gestionar ambigüedades y añadir caché.

### Fase 3 — Perfil de gustos

Calcular preferencias y aversiones por características, con un informe JSON inspeccionable.

### Fase 4 — Recomendador inicial

Generar candidatas, excluir vistas y crear el primer top 10 explicable.

### Fase 5 — Evaluación

Comparar variantes y líneas base, medir resultados y ajustar pesos con evidencia.

### Fase 6 — Informe

Crear CSV y HTML local con las recomendaciones, explicaciones y nivel de confianza.

### Fase 7 — Interfaz opcional

Valorar una aplicación web local cuando el pipeline y la evaluación ya funcionen.

## Privacidad y publicación

- `exports/`, `resultados/`, cachés y tokens siempre gitignorados.
- No publicar películas o valoraciones reales en la rama principal.
- Para una demo pública, generar un dataset sintético o anonimizado no reversible.
- No automatizar Letterboxd ni usar su API privada.
- Atribuir TMDB y revisar sus condiciones antes de publicar o monetizar.

## Criterio de éxito del MVP

El MVP estará terminado cuando pueda leer un export, enriquecer las películas identificadas, generar diez recomendaciones no vistas con explicaciones y superar una línea base sencilla en una evaluación reproducible.

