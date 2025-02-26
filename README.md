# trabajo_clase_2

#Que son bases de datos vectoriales 

Este tipo de bases están diseñados para para almacenar y administrar datos que están representados como vectores en espacios multidimensionales. 
Los puntos de datos son almacenados como matrices de números llamados vectores que se agrupan según la similitud.
Estas bases son útiles cuando se involucran búsquedas por similitud, como por ejemplo el reconocimiento de imágenes, recomendaciones y procesamiento de lenguaje natural (PLN) y para búsqueda aproximada en grandes volúmenes de datos no estructurados.

#Aplicaciones de bases de datos vectoriales.
Se pueden usar en ámbitos como: 
•	Procesamiento de lenguaje natural (PLN): Para búsqueda semántica en documentos y bases de conocimiento.
•	Reconocimiento de imágenes: Comparación y búsqueda de imágenes similares en grandes bases de datos.
•	Motores de recomendación: Comparación de preferencias de usuarios basadas en embeddings.
•	Búsqueda de audio y video: Identificación y clasificación de archivos multimedia.
•	Ciberseguridad: Análisis de patrones de actividad sospechosa.


Como implemento en postgres Bases de Datos Vectoriales

pgvector, es una extensión que permite que Postgres actúe como una base de datos vectorial, este permite consultar e indexar tipos de datos vectoriales, así como también generar y almacenar incrustaciones vectoriales de PostgreSQL. 
PostgreSQL con pgvector permite almacenar y buscar vectores de manera eficiente, siendo ideal para aplicaciones como IA, NLP y motores de recomendación. La combinación de índices y consultas optimizadas ayuda a escalar la búsqueda por similitud en bases de datos grandes.

Para implementar una Base de Datos Vectorial en PostgreSQL, se debe por ejemplo seguir los pasos:

•	Instalación de pgvector
Se debe instalar la extensión antes de poder usarla en PostgreSQL.
En Linux (Debian/Ubuntu):
sudo apt install postgresql-postgis pgvector
En macOS con Homebrew:
brew install pgvector
Si se usa Docker, se debe ejecutar PostgreSQL con pgvector preinstalado:
docker run --name pgvector-db -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 ankane/pgvector
•	Activar la extensión en PostgreSQL
Se conecta a PostgreSQL y se habilita la extensión:
CREATE EXTENSION IF NOT EXISTS vector;
•	Crear una tabla con datos vectoriales

El tipo de dato vector permite definir columnas con dimensiones fijas.
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    embedding vector(3) -- este "3" se cambiaria por el número de dimensiones necesarias
);


Que es un data lake.

Un Data Lake es un repositorio de almacenamiento que permite guardar grandes volúmenes de datos en su formato original, estructurados, semiestructurados y no estructurados. A diferencia de los Data Warehouses, que requieren estructuración previa, los Data Lakes almacenan datos sin procesar y los organizan cuando son necesarios.

Que aplicaciones tienen los data lakes. 
Los Data Lakes son esenciales para empresas que trabajan con grandes volúmenes de datos, especialmente en Big Data, IA, IoT y análisis predictivo. Su flexibilidad y escalabilidad los convierten en una solución poderosa para extraer valor de datos no estructurados y optimizar la toma de decisiones:
•	Big Data Analytics
Permiten almacenar y analizar enormes cantidades de datos provenientes de diversas fuentes, facilitando el descubrimiento de patrones y tendencias que pueden impulsar decisiones estratégicas.
•	Machine Learning e Inteligencia Artificial
Almacenar datos sin procesar permite entrenar modelos de aprendizaje automático con información amplia y variada, lo que puede mejorar la precisión de los algoritmos y la capacidad predictiva.
•	Internet de las Cosas (IoT)
Los Data Lakes son ideales para recoger y almacenar datos generados por dispositivos conectados, sensores y otros dispositivos IoT, permitiendo analizar en tiempo real el comportamiento y rendimiento de sistemas complejos.
•	Integración y unificación de datos
Funcionan como una única fuente de datos para toda la organización, integrando información proveniente de diferentes sistemas y formatos, lo que facilita la obtención de una visión completa y unificada de la información.
•	Business Intelligence (BI) y Reportes
Almacenan datos históricos que pueden ser utilizados para generar reportes, dashboards y análisis en profundidad, ayudando a las empresas a evaluar el rendimiento y tomar decisiones basadas en datos.
•	Archivado y Retención de Datos
Actúan como depósitos de datos históricos, permitiendo conservar información para análisis futuros, cumplimiento normativo o auditorías.


Bibliografía:
https://airbyte.com/data-engineering-resources/postgresql-as-a-vector-database
https://www.elastic.co/es/what-is/vector-database
https://www.ibm.com/es-es/topics/vector-database
https://www.ibm.com/mx-es/topics/data-lake
