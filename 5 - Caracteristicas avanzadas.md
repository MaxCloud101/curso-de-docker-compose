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

### Dependencias de servicio con ```depends_on```

En muchas aplicaciones, ciertos servicios dependen de la disponibilidad de otros para poder iniciarse. Docker Compose proporciona la opción ```depends_on``` para expresar esta relación. Esto garantiza que Docker inicie los servicios dependientes en el orden correcto.

```yaml
services:
  web:
    image: nginx
    depends_on:
      - db

  db:
    image: postgres
```


### Controles de salud para garantizar la disponibilidad del servicio

Docker Compose permite definir comprobaciones de estado para supervisar el estado de un servicio. Una comprobación de estado ejecuta periódicamente un comando dentro del contenedor, y Docker utiliza el resultado para determinar si el contenedor está en buen estado. Puede configurar comprobaciones de estado para sus servicios mediante la opción "healthcheck".

```yaml
services:
  db:
    image: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 30s
      timeout: 10s
      retries: 5
```

En este caso, Docker comprobará cada 30 segundos si la base de datos de Postgres está lista para aceptar conexiones. Si el servicio falla la comprobación 5 veces, Docker lo marcará como unhealthy.

### Gestión de limitaciones de recursos

Docker Compose permite controlar los recursos (CPU y memoria) asignados a cada servicio. Esto es especialmente importante al ejecutar varios contenedores en el mismo host, ya que ayuda a evitar la contención de recursos.

```yaml
services:
  web:
    image: nginx
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: "512M"
```

### Uso de políticas de reinicio para la resiliencia del servicio

Para garantizar que sus servicios se reinicien automáticamente en caso de fallo, puede definir una política de reinicio. Docker Compose ofrece varias opciones para gestionar cómo y cuándo deben reiniciarse los contenedores:

- no: No reiniciar automáticamente el contenedor (predeterminado).
- always: Reiniciar siempre el contenedor si se detiene.
- on-failure: Reiniciar solo si el contenedor sale con un código distinto de cero.
- unless-stopped: Reiniciar a menos que el contenedor se detenga explícitamente.

```yaml
services:
  web:
    image: nginx
    restart: always
```






