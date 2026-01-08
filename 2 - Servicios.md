# Servicios

Los servicios en Docker Compose son los componentes individuales de una aplicación (como un backend, una base de datos, un frontend) definidos en el archivo docker-compose.yml, que se ejecutan en contenedores separados pero orquestados juntos.

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
