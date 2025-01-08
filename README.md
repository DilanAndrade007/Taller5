
# README - Proyecto de Indexación y Recuperación de Películas

## Descripción

Este proyecto tiene como objetivo la creación de un sistema de indexación y recuperación de películas utilizando diferentes enfoques. Inicialmente, se construye un índice invertido manualmente en Python, luego se utiliza la biblioteca Whoosh para una indexación más avanzada, y finalmente se emplea Elasticsearch para la indexación y recuperación a gran escala. A lo largo del proyecto, se proporciona un enfoque paso a paso para procesar, indexar y consultar grandes volúmenes de datos de películas basados en sus tramas.

### Funcionalidades principales:
1. **Construcción de un índice invertido manualmente**: Se carga un conjunto de datos de películas, se procesan las tramas y se construye un índice invertido basado en las palabras clave encontradas.
2. **Indexación con Whoosh**: Utilizando la biblioteca Whoosh, se crea un índice optimizado y se realizan consultas sobre el índice.
3. **Integración con Elasticsearch**: Con Elasticsearch, se establece una infraestructura de indexación y búsqueda escalable, que permite realizar consultas rápidas sobre grandes volúmenes de datos.

## Requisitos

Antes de ejecutar este proyecto, asegúrese de tener las siguientes herramientas instaladas:

### Software necesario:
- **Python 3.x**: Se requiere Python 3 para ejecutar el código.
- **Docker**: Para iniciar Elasticsearch en un contenedor Docker.
  
### Librerías necesarias:
1. **pandas**: Para la manipulación de datos.
2. **Whoosh**: Para la indexación local.
3. **elasticsearch**: Cliente de Python para interactuar con Elasticsearch.

Instale las dependencias ejecutando:
```bash
pip install pandas whoosh elasticsearch
```

### Docker (para Elasticsearch):
1. Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Iniciar Elasticsearch usando el siguiente comando:
```bash
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.10.2
```

## Estructura del Proyecto

- **`wiki_movie_plots_deduped.csv`**: Datos usados en el proyecto.
- **`Taller_5.ipynb`**: Notebook del desarrollo del proyecto.
- **`elasticsearch_movies.py`**: Código para interactuar con Elasticsearch para la indexación y consulta de películas.

## Pasos de Implementación

### Parte 1: Construcción Manual de un Índice Invertido
1. **Carga de Datos**: Los datos de las películas se cargan desde un archivo CSV utilizando pandas.
2. **Normalización de Texto**: Se procesan las tramas de las películas, convirtiéndolas a minúsculas y eliminando caracteres especiales.
3. **Construcción del Índice Invertido**: Se crea un índice invertido que mapea cada palabra clave a las películas que contienen esa palabra.
4. **Búsqueda en el Índice**: Se implementa una función para realizar consultas, buscando películas que contengan ciertas palabras clave.

### Parte 2: Indexación con Whoosh
1. **Configuración de Whoosh**: Se define un esquema de índice utilizando Whoosh, que incluye campos como `Title` y `Plot`.
2. **Indexación de Datos**: Los datos de las películas se indexan utilizando Whoosh, almacenando tanto el título como la trama de cada película.
3. **Consultas con Whoosh**: Se realizan consultas de búsqueda en el índice utilizando la librería Whoosh y se recuperan los títulos de las películas correspondientes.

### Parte 3: Indexación y Recuperación con Elasticsearch
1. **Configuración de Elasticsearch**: Se instala y ejecuta Elasticsearch en un contenedor Docker.
2. **Conexión a Elasticsearch**: Se configura la conexión con Elasticsearch desde Python.
3. **Creación de un Índice**: Se crea un índice en Elasticsearch con los campos `Title` y `Plot`.
4. **Indexación de Datos en Elasticsearch**: Cada película se indexa en Elasticsearch, utilizando su título como identificador único.
5. **Consultas en Elasticsearch**: Se implementa una función para realizar consultas sobre el índice de Elasticsearch y recuperar los títulos de las películas que coinciden con una consulta de texto.

  
## Conclusiones

A través de cada parte del proyecto, hemos aprendido cómo construir y mejorar índices, manejar grandes volúmenes de datos y realizar consultas eficientes.

### Consideraciones finales

- **Optimización**: Aunque Elasticsearch ofrece una mayor escalabilidad, Whoosh es útil para proyectos más pequeños o entornos locales donde no se necesita una infraestructura compleja.
- **Desafíos**: Durante el proyecto, se enfrentaron algunos desafíos relacionados con la configuración de Elasticsearch y la gestión del contenedor Docker. Asegúrese de que los servicios estén funcionando correctamente antes de comenzar con la indexación.

## Autor

    Dilan Andrade
    Hernan Sanchez
    Galo Tarapues

