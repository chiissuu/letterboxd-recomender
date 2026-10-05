# Letterboxd Recommender — Inicio

Válvula de contexto para Obsidian y futuras sesiones.

## Estado actual

Idea definida y aparcada para desarrollarla más adelante. El proyecto deja atrás el objetivo de comparar seguidores y pasa a ser un sistema local, explicable y evaluable de recomendaciones cinematográficas.

## Mapa

- [Contexto](Contexto.md): origen y objetivo provisional.
- [Visión del recomendador](Vision-Recomendador.md): propuesta completa del producto y su arquitectura.
- [Investigacion](Investigacion.md): fuentes y posibilidades técnicas.
- [Decisiones](Decisiones.md): límites ya establecidos.
- [Funcionamiento](Funcionamiento.md): inspector actual y futuro flujo.
- [Pendientes](Pendientes.md): acciones necesarias para continuar.
- [Sesión inicial](Sesiones/2026-10-05-investigacion-inicial.md): trabajo realizado.

## Estructura

```text
letterboxd-recomender/
├── inspector_export.py
├── tests/test_inspector_export.py
├── README.md
├── .gitignore
└── Documentacion-Interna/
```

## Retomar el proyecto

Leer primero Vision-Recomendador, Investigacion y Decisiones. No implementar peticiones automatizadas a letterboxd.com ni login por navegador. Mantener el ZIP, la caché de TMDB y todos los resultados personales fuera de Git.

