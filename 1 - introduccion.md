# Docker Compose

## Introduccion

Docker Compose es una herramienta de Docker que permite definir y ejecutar aplicaciones multicontenedor de forma sencilla y coordinada, utilizando un archivo YAML (docker-compose.yml) para configurar todos los servicios (contenedores, redes, volúmenes, puertos) de una aplicación, permitiendo levantarlos o bajarlos todos juntos con un único comando, ideal para entornos de desarrollo y pruebas. 

## ¿Qué hace Docker Compose?

- Orquestación: Gestiona múltiples contenedores como una única aplicación, facilitando la ejecución de aplicaciones complejas (web + base de datos + caché, por ejemplo).
- Configuración como código: Define toda la infraestructura en un archivo YAML, lo que lo hace reproducible y versionable (control de versiones).
- Simplifica la gestión: En lugar de ejecutar comandos docker run para cada contenedor, usas un solo comando (docker-compose up) para iniciar todo.
- Redes y volúmenes: Crea redes automáticas para la comunicación entre contenedores y gestiona volúmenes para persistencia de datos

## ¿Para qué se usa?

- Entornos de desarrollo: Configurar rápidamente entornos locales idénticos al de producción.
- Pruebas (Testing): Desplegar entornos de prueba consistentes.
- Integración Continua/Entrega Continua (CI/CD): Incluir la configuración de la aplicación en pipelines de automatización

## Ejemplo de uso
  
Imagina una aplicación web con:

- Un contenedor para tu aplicación (frontend/backend).
- Un contenedor para una base de datos (ej: PostgreSQL).
- Un contenedor para un servicio de caché (ej: Redis). 

Con Docker Compose, defines estos tres en docker-compose.yml, y con un solo comando, se crean y conectan. 
