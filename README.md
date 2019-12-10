# ArquiSoftware_EntregaFinal


## Instalar virtualenv

https://virtualenv.pypa.io/en/latest/installation/

## Activar el environment
$ source /home/nombre_usuario/ENV/bin/activate

## Instalar django en el enviroment
$ python -m pip install Django

## Ejecutar  migraciones

Django por defecto viene funcionando con sqlite, por lo que para nuestro caso nos conviene no meternos con otra base de datos.

$ python manage.py migrate

## Crear una nueva migracion

Simplemente cambiar los modelos y luego:
$ python manage.py makemigrations chat

## Correr en localhost

$ python manage.py runserver 8000


