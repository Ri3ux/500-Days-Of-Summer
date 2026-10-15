# Descriptción del proyecto

La empresa de comercio electrónico Store 1 está preparando el lanzamiento de un nuevo **Programa de Fidelización de Clientes**. Para ello, necesita analizar su base de clientes y asegurarse de que los datos estén completos, limpios y organizados.

El objetivo es diseñar campañas personalizadas y optimizar futuras acciones de marketing. Para lograrlo, necesita segmentar a los clientes según variables como la edad, el historial de compras y las categorías de productos adquiridos.

Como miembro del equipo de análisis, tu tarea inicial será revisar y transformar una muestra de los datos existentes para dejarlos listos para el análisis. En esta fase deberás:

1. Limpiar los perfiles de los clientes.
2. Estandarizar nombres y edades.
3. Calcular el gasto total por cliente.
4. Validar la consistencia de los datos y corregir errores.
5. Preparar los datos para generar indicadores de negocio (KPIs).

Los datos brindados por la empresa Store 1 tienen el formato de una lista de Python, con las siguientes columnas de datos:

* **usuario_id:** Identificador único para cada usuario.
* **usuario_nombre:** Nombre del usuario.
* **usuario_edad:** Edad del usuario.
* **categorias_fav_low:** Categorías favoritas de los artículos que compró el usuario, como ELECTRÓNICA, DEPORTE, LIBROS, etc.
*** gasto_por_categoria:** Una lista de números enteros que indican la cantidad total gastada en cada una de las categorías favoritas.

```python
usuarios = [ 
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['ROPA', 'ELECTRÓNICA', 'BELLEZA'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['LIBROS', 'HOGAR', 'DEPORTE'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BELLEZA', 'HOGAR', 'COMIDA'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['ROPA', 'COMIDA', 'BELLEZA'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['DEPORTE', 'ELECTRÓNICA', 'HOGAR'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOGAR', 'LIBROS', 'ROPA'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BELLEZA', 'ROPA', 'ELECTRÓNICA'], [189, 299, 579]],
]
```

En la segunda parte de este proyecto, durante el próximo sprint, desarrollarás un análisis completo que responderá directamente a las necesidades del cliente.