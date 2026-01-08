# Servicios

Los servicios en Docker Compose son los componentes individuales de una aplicación (como un backend, una base de datos, un frontend) definidos en el archivo docker-compose.yml, que se ejecutan en contenedores separados pero orquestados juntos.

Para crear y levantar todos los servicios de una aplicación Docker definidos en un archivo docker-compose.yml usaremos:

```sh
$ docker compose up
```

## Trabajando con servicios 

### Definicion de un servicio 

Colocamos la siguiente configuracion en el archivo docker-compose.yaml

```yaml
services:
  web:
    image: nginx:latest
```

### Exponiendo un servicio en localhost

Enlazamos el servicio en el puerto 80 con el puerto 8080 del host

```yaml
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

Podemos verificar el servicio en ```http://localhost:8080```

### Agregando variables de entorno

En el siguiente ejemplo usamos variables de entorno para agregar el usuario y contraseña a nuestra base de datos en postgresql

```yaml
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
    ports:
      - "5432:5432"
```

Podemos conectarno a travez de cualquier IDE de base de datos

### Agregando variables de entorno desde el archivo .env

Creamos un archivo .env con la siguiente informacion

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
```

Definimos el docker compose

```yaml
services:
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
    ports:
      - "5432:5432"
```

### Agregando variables de entorno usando ```env_file ```

Creamos un archivo .env con la siguiente informacion

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
```

Definimos el docker compose
```yaml
services:
  db:
    image: postgres:13
    env_file:
      - .env
    ports:
      - "5432:5432"
```

Podemos sobrescribir las variables de entorno definidas en el ```env_file``` con atributos en environment

```yaml
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: supersecret
    env_file:
      - .env
    ports:
      - "5432:5432"
```

> [!NOTE]
> Nunca envíe archivos .env que contengan datos confidenciales (p. ej., claves API o contraseñas) a sistemas de control de versiones. Use .gitignore para excluir archivos .env.

> [!NOTE]
> Utilice los secretos de Docker para la información confidencial en entornos de producción. Docker Compose cuenta con soporte nativo para gestionar los secretos de forma más segura

### Arrancando un servicio desde el Dockerfile

Nos colocamos en la carpeta flaskapp dentro de este repositorio. Alli verificamos el archivo ```docker-compose.yaml``` donde arrancamos el servicio desde un Dockerfile

```
services:
  flaskapp:
    build:
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
```
