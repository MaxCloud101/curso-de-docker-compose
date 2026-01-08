# Redes

## Comportamiento de red por defecto

Al ejecutar docker-compose por primera vez, Docker crea automáticamente una red predeterminada para sus servicios. Todos los servicios del archivo docker-compose.yml se conectan a esta red, a menos que defina redes personalizadas. Los servicios pueden comunicarse entre sí utilizando sus nombres de servicio como nombres de host DNS.

## Trabajando con redes

### Usando la red por defecto

Vamos a la carpeta exchange, aqui tenemos definidas dos aplicaciones:

- main_exchange.py : Esta aplicacion recibe una divisa y un monto para hacer la transformacion del monto en su respectiva divisa, escogiendo entre euros y libras.
- main.py: Esta aplicacion hace uso de main_exchange.py para realizar la conversion del monto deacuerdo a la divisa y agregando una comision por el uso del servicio.

Revisamos el archivo ```docker-compose.yaml``` y encontraremos:

```yml
services:
  exchange:
    build:
      dockerfile: Dockerfile_exchange

  app:
     build:
       dockerfile: Dockerfile
     environment:
       - EXCHANGE_URL=exchange:8000
     ports:
       - "9090:9090"
```

Aqui vemos que ```EXCHANGE_URL``` es la variable de entorno que tiene la direccion por la cual el servicio ```app``` se puede comunicar con el servicio```exchange```. Esta comunicacion se hace mediante la red por defecto, usando los nombres de los servicios como DNS hostnames.

### Definiendo una red personalizada

Definimos una red personalizada con el nombre ```custom_network```

```yml
networks:
  custom_network:

services:
  exchange:
    build:
      dockerfile: Dockerfile_exchange
    networks:
      - custom_network

  app:
     build:
       dockerfile: Dockerfile
     environment:
       - EXCHANGE_URL=exchange:8000
     ports:
       - "9090:9090"
    networks:
      - custom_network
```

### 1 Definiendo una red bridge

El modo de red más común en Docker Compose es la red bridge, que permite que los contenedores de la misma red se comuniquen entre sí. Este es el modo predeterminado para las redes, a menos que se especifique explícitamente otro controlador de red.

```yml
networks:
  custom_network:
    driver: bridge

services:
  exchange:
    build:
      dockerfile: Dockerfile_exchange
    networks:
      - custom_network

  app:
     build:
       dockerfile: Dockerfile
     environment:
       - EXCHANGE_URL=exchange:8000
     ports:
       - "9090:9090"
    networks:
      - custom_network
```

### 2 Trabajando con la Red Host

En algunos casos, puede que necesites que tus contenedores compartan la pila de red del host. Esto se denomina modo de red del host. En este modo, los contenedores evitan el aislamiento de red de Docker y se enlazan directamente a la interfaz de red del host. Este modo es útil cuando se requiere comunicación de baja latencia o acceso directo a la red del host, pero reduce el aislamiento de red entre los contenedores y el host.

```yml
services:
  web:
    image: nginx
    network_mode: "host"
```

### 3 Trabajando con redes externas

En algunos casos, podría querer conectar sus servicios a redes creadas fuera de Docker Compose. Esto es especialmente útil cuando tiene servicios ejecutándose en proyectos de Compose separados o contenedores Docker independientes que necesitan comunicarse entre sí.

Para utilizar una red externa, primero debe crear la red mediante la CLI de Docker:

```sh
$ docker network create my_external_network
```

Luego creamos el ```docker-compose.yaml```

```yml
networks:
  my_external_network:
    external: true

services:
  web:
    image: nginx
    networks:
      - my_external_network
```


