# Bushido: El camino del Data Scientist

[![Python](https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

Apuntes, ejercicios y proyectos de mi formación como **Data Scientist** en TripleTen.

## Estructura

```
Data Scientist/
├── [1] … [12] *.ipynb   # Apuntes por tema
├── Exercises/           # Ejercicios de práctica
├── Sprints/             # Proyectos de cada sprint
├── Datasets/            # Datos usados en apuntes y proyectos
└── unite_test.py        # Ejemplo de pruebas unitarias con pytest
```

## Apuntes

| # | Notebook | Contenido |
|---|----------|-----------|
| 1 | Librerías | Pandas como librería |
| 2 | Notebooks | Métodos de los strings |
| 3 | Visualización de datos | Gráficos para explorar datos |
| 4 | Teoría de la probabilidad | Conceptos básicos de probabilidad |
| 5 | Análisis estadístico | Variables categóricas y cuantitativas |
| 6 | Pruebas de hipótesis | Muestras aleatorias y medias muestrales |
| 7 | Terminal | Herramientas de desarrollo de software |
| 8 | Scripts | Scripts en Python |
| 9 | Clases | Clases y objetos en Python |
| 10 | Documentos | Lectura y escritura de archivos |
| 11 | API Rest | Peticiones HTTP y autenticación |
| 12 | Calidad del código | Buenas prácticas y pruebas unitarias |

## Ejercicios

- Ingeniería de características
- Transformación de datos
- Estadística descriptiva

## Proyectos

| Sprint | Proyecto |
|--------|----------|
| 1 | Análisis de clientes de Store 1 — primera fase |
| 2 | Análisis de clientes de Store 1 — segunda fase |
| 3 | Déjame escuchar música |
| 4 | ¡Llena ese carrito! |
| 5 | ¿Cuál es la mejor tarifa? (Megaline) |
| 6 | Patrones de éxito de videojuegos (tienda Ice) |
| 7 | Panel web con Streamlit desplegado en Render → [streamlit-webapp](https://github.com/Ri3ux/streamlit-webapp) |

## Uso

Los notebooks se pueden abrir con Jupyter o con VS Code. Las pruebas de `unite_test.py` se ejecutan con:

```bash
pytest "Data Scientist/unite_test.py"
```
