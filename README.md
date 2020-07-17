# API Restaurantes App (Grability)

API que intercambia información con la aplicación móvil sin requerir registro previo por parte de los usuarios finales de la aplicación. Backend desarrollado con Django

## Descripción

La aplicación expone un API REST basado en `djangorestframework` que permite consultar información de restaurantes y los productos que éstos ofrecen a través de una aplicación móvil que ya se encuentra desarrollada. Para interactuar con el API no se requiere ningún tipo de registro de usuarios dado que el acceso a la información de forma segura se garantiza por medio de la implementación de API-Keys.

## Requisitos
* Python versión >= 3.6
* Administrador de entornos virtuales `pipenv`
* PostgreSQL version >= 11

## Configuración

Clone el repositorio en el directorio de su preferencia y desde el interior del directorio del proyecto instale los paquetes necesarios

```bash
pipenv install
```

### Archivo de configuración (.env)
Para que el API funcione correctamente, es necesario crear el archivo de configuración `.env` en el mismo nivel donde se encuentra ubicado el archivo `manage.py`. A continuación se muestra una configuración de ejemplo:
```
SECRET_KEY=YOUR_SECRET_KEY
DBNAME=DATABASE_NAME
DBUSER=DATABASE_USER
DBPASS=DATABASE_PASSWORD
DBHOST=DATABASE_IP_OR_HOST
DBPORT=DATABASE_PORT
DEBUG=True
```
Se deben reemplazar los valores correspondientes a cada parámetro. Para la variable `SECRET_KEY` seguir las recomendaciones de la [documentación](https://docs.djangoproject.com/en/3.0/ref/settings/) oficial de Django. Si se va a desplegar la aplicación en un ambiente productivo, recuerde modificar el valor de la variable `DEBUG` a `False`.

Activar el entorno virtual

```bash
pipenv shell
```

Finalmente ejecutar las migraciones en la base de datos
```bash
python manage.py migrate
```
## Ejemplo

La aplicación cuenta con un mecanismo para generar datos de prueba que persisten en la base de datos. Para generar los objetos de prueba ejecutar

```bash
python manage.py seed_db
```

Por defecto se crearán 50 restaurantes y para cada uno de ellos 50 productos. Si desea especificar la cantidad de restaurantes a crear, debe agregar el parámetro  `--restaurants` y de igual forma si quiere una cantidad diferente de productos para cada restaurante pasar el parámetro `--products`. 

```bash
python manage.py seed_db --restaurants 120 --products 25
```

Para iniciar el servidor de pruebas ejecutar

```
python manage.py runserver
```

### api_key.txt

Durante el proceso anterior, la aplicación genera el archivo `api_key.txt` el cual contiene el API_KEY generado para la aplicación. Los API_KEYS generados se pueden administrar desde la vista web de administrador de Django.

```
----------------------------------------------------------------------
API-KEY:INITIAL-KEY
KEY:YOUR_KEY
```

### Restaurantes

El endpoint `api/v1/restaurants` retorna la lista de restaurantes creados, para tener acceso a esta información se debe incluir el header `GRABILITY-API-KEY` con la llave generada en el archivo `api_key.txt` en la petición.

```
curl -X GET http://your_host_or_ip:8000/api/v1/restaurants -H "GRABILITY-API-KEY: YOUR_API_KEY"
```

### Productos

#### Lisa de productos

Para consultar la lista de productos de un restaurante se debe realizar la consulta al endpoint `api/v1/restaurant/{restaurant_id}/products`. De esa forma el API filtra los productos que pertenecen al restaurante específicado por su ID.

```
curl -X GET http://your_host_or_ip:8000/api/v1/restaurant/17/products -H "GRABILITY-API-KEY: YOUR_API_KEY"
```

#### Detalle de un producto

Adicionalmente el API cuenta con un endpoint por medio del cual se puede consultar el detalle de un producto. De igual manera, el ID del producto se debe especificar en la URI de consulta `api/v1/product/{product_id}`

```
curl -X GET http://your_host_or_ip:8000/api/v1/product/3 -H "GRABILITY-API-KEY: YOUR_API_KEY"
```

**_NOTA:_** _Las consultas de listas (lista de productos y lista de restaurantes) se encuentran paginadas por un máximo de 10 elementos por página_.

### Autenticación JWT

Adicionalmente, el API cuenta con un mecanismo de autenticación basado en [JWT](https://jwt.io/introduction/), el token generado tiene un tiempo de expiración por seguridad, por lo que se debe actualizar el token constantemente.

#### Login

El proceso de login se realiza a través del endpoint `token-auth/login` el cual solicita las credenciales de acceso correspondientes (`username`, `password`) para generar el token correspondiente (ver [ejemplo](https://drive.google.com/file/d/15KhZ4O37tWlXXETvoE4k1iyWTJoNy_ND/view?usp=sharing)).

```
curl -X POST http://your_host_or_ip:8000/token-auth/login -d '{"username":"admin","password":"password123"}'
```



#### Verificación del token

Para validar el estado del token actual se dispone el endpoint `api/v1/token-auth/verify` que entrega la información del estado actual del token indicado en el parámetro `token`.  Si el token aún es vigente el API retorna el token consultado con código de estado HTTP 200, mientras que si el token expiró el código de estado es 400 (ver [ejemplo](https://drive.google.com/file/d/1-9eaLtHZi9qVL2eU5-MHQfGbPr0kZhFV/view?usp=sharing))

```
curl -X POST http://your_host_or_ip:8000/token-auth/verify -d '{"token":"<CURRENT_TOKEN>"}'
```



#### Actualización del token

Si al verificar el estado del token este ha expirado, se puede realizar la renovación del mismo por medio del endpoint `api/v1/token-auth/refresh` el cual solicita el token expirado y entrega como resultado un nuevo token.

```
curl -X POST http://your_host_or_ip:8000/token-auth/refresh -d '{"token":"<CURRENT_TOKEN>"}'
```



### Creación de API_KEY

Finalmente, otro servico que expone el API es la posibilidad de generar API_Keys para la aplicación, permitiendo administración completa sobre los mismos. El acceso a este endpoint esta restringido para usuarios de tipo administrador, por lo que primero se debe crear un usuario con este privilegio (`python manage.py createsuperuser`) y una vez se autentique puede realizar la petición.

```
curl -X POST http://your_host_or_ip:8000/api/v1/api-key/create -d '{"name":"API-KEY-NAME"}' -H "Authorization: JWT <ADMIN_USER_TOKEN"
```



## Fuentes

* [Json Web Token (JWT)](https://jwt.io/)
* [Django Rest Framework](https://www.django-rest-framework.org/)