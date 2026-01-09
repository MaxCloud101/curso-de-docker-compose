# Volumenes

Al ejecutar contenedores, los datos almacenados en ellos son efímeros, lo que significa que se perderán al detenerse o eliminarse el contenedor. Para garantizar la persistencia de los datos, Docker Compose permite usar volúmenes, que permiten almacenar datos fuera del ciclo de vida del contenedor. Los volúmenes son la forma preferida de persistir datos, ya que son administrados por Docker y pueden compartirse entre contenedores.

## Trabajando con volumenes

### Definiendo una volumen

Una vez definido un volumen, puede asociarlo a un servicio mediante la opción "volumenes" de ese servicio. Esto asigna un directorio del host a un directorio dentro del contenedor.

```yml
volumes:
  db_data:

services:
  db:
    image: postgres:13
    volumes:
      - db_data:/var/lib/postgresql/data
```

### Trabajando con Bind mounts

Los Bind mounts le permiten asignar directamente directorios en su máquina host a directorios dentro del contenedor.

```yml
services:
  app:
    image: myapp:latest
    volumes:
      - ./app:/usr/src/app
```

### Compartir volúmenes entre servicios

A veces, varios servicios necesitan acceder a los mismos datos. Docker Compose permite compartir volúmenes entre servicios, lo que les permite colaborar en los mismos archivos o conjuntos de datos.

```yml
services:
  web:
    image: nginx:latest
    volumes:
      - shared_data:/usr/share/nginx/html

  worker:
    image: myworker:latest
    volumes:
      - shared_data:/usr/src/app/data

volumes:
  shared_data:
```

### Persistencia de datos para bases de datos

Para las bases de datos, el uso de volúmenes es crucial para garantizar que no se pierdan datos al detener o eliminar los contenedores. A continuación, se muestra un ejemplo de una configuración de Docker Compose para un servicio MySQL que persiste datos mediante un volumen con nombre:

```yml
services:
  mysql:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: mydatabase
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

### Eliminación de volúmenes

Los volúmenes no se eliminan automáticamente al detener o eliminar un contenedor. Debe eliminarlos explícitamente cuando ya no sean necesarios. Para eliminar todos los volúmenes no utilizados, puede ejecutar el siguiente comando:

```yml
docker volume prune
```
Para eliminar un volumen específico, utilice:
```yml
docker volume rm volume_name
```
