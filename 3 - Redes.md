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

