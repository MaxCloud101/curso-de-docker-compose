# Redes

## Comportamiento de red por defecto

Al ejecutar docker-compose por primera vez, Docker crea automáticamente una red predeterminada para sus servicios. Todos los servicios del archivo docker-compose.yml se conectan a esta red, a menos que defina redes personalizadas. Los servicios pueden comunicarse entre sí utilizando sus nombres de servicio como nombres de host DNS.

## Trabajando con redes

### Usando la red por defecto

Vamos a la carpeta exchange, aqui tenemos definidas dos aplicaciones:

- main_exchange.py : Esta aplicacion recibe una divisa y un monto para hacer la transformacion del monto en su respectiva divisa, escogiendo entre euros y libras.
- main.py: Esta aplicacion hace uso de main_exchange.py para realizar la conversion del monto deacuerdo a la divisa y agregando una comision por el uso del servicio.


