# Funciones avanzadas de Docker Compose

Si bien Docker Compose simplifica las configuraciones multicontenedor, también ofrece varias funciones avanzadas que mejoran el control y la eficiencia en la gestión del ciclo de vida de su aplicación. Estas funciones le permiten escalar servicios, administrar dependencias, garantizar el estado del servicio y mucho más. Revisaremos las herramientas avanzadas en Docker Compose.

### Escalado de servicios con Docker Compose

Una de las características más útiles de Docker Compose es la posibilidad de escalar sus servicios horizontalmente. Esto significa que puede ejecutar varias instancias de un servicio para gestionar más carga o garantizar la redundancia. El escalado es especialmente beneficioso para servicios sin estado, como servidores web o procesos de trabajo.

Puede escalar servicios usando la opción ```--scale``` con ```docker-compose up```:

```sh
docker-compose up --scale web=3
```

Alternativamente, puede definir réplicas de servicio en su ```docker-compose.yml```:

```yaml
services:
  web:
    image: nginx:latest
    deploy:
      replicas: 3
```


