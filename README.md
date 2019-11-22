MUEI-RIWS

Práctica de recuperación de la información de la asignatura "Recuperación de la Información y Web Semántica" del Máster Universitario en Ingeniería Informática.

Este repositorio contiene el código de tres partes de un proyecto de recuperación de la información que toma datos de productos de la web myprotein.es y los muestra en un interfaz web ofreciendo posibilidad de realizar búsquedas y filtrar por distintos filtros.

### Ejecución

En primer lugar, es necesario levantar el servidor de Elasticsearch y Kibana entrando en el directorio 'Elasticsearch' y ejecutando el comando

```
# docker-compose -f docker-compose.yml up
```

Se levanta en la máquina donde se ejecuta una imagen de Elasticsearch en el puerto 9200 y una de Kibana en el puerto 5601.

Se puede comprobar el estado de Elasticsearch con el comando

```
curl -XGET 'ip-servidor:9200/_cluster/health?pretty'
```

Una vez Elasticsearch está corriendo, pasamos a ejecutar el crawler. Se introduce la IP del servidor en el fichero Crawler/myprotein/myprotein/settings.py y se ejecuta desde un terminal

```
cd Crawler/myprotein/myprotein
scrapy crawl myprotein
```

El proceso lleva unos minutos y al terminar envía los datos al servidor Elasticsearch.

Podemos comprobar que los datos se visualizan correctamente accediendo a Kibana en http://ip-servidor:5601 o si el índice existe con una consulta a Elasticsearch

```
curl -i -XHEAD 'http://ip-servidor:9200/myprotein/'
```

Por último, se ejecuta el cliente web

```
cd client
npm install
npm run serve
```

Se accede a él en la dirección http://ip-servidor:8080