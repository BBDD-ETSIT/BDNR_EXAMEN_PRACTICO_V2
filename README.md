<img  align="left" width="150" style="float: left;" src="https://www.upm.es/sfs/Rectorado/Gabinete%20del%20Rector/Logos/UPM/CEI/LOGOTIPO%20leyenda%20color%20JPG%20p.png">
<img  align="right" width="60" style="float: right;" src="http://www.dit.upm.es/figures/logos/ditupm-big.gif">


<br/><br/>


# Exámen Práctico de ODM con PYTHON-FLASK y MONGOENGINE

## 1. Dependencias

Para realizar la práctica el alumno deberá tener instalado en su ordenador:
- Herramienta GIT para gestión de repositorios [Github](https://git-scm.com/downloads)
- Entorno de ejecución de Python 3 [Python](https://www.python.org/downloads/)
- Base de datos MongoDB [MongoDB](https://www.mongodb.com/try/download/community)
- Base de datos [Fuseki](https://jena.apache.org/documentation/fuseki2/)

## 2. Descargar e instalar el código del proyecto

Abra un terminal en su ordenador y siga los siguientes pasos.

Clone el repositoro de GitHub
```
git clone https://github.com/BBDD-ETSIT/BDNR_EXAMEN_PRACTICO_V2.git
```

Navegue a través de un terminal a la carpeta BDNR_EXAMEN_PRACTICO_V2.
```
BDNR_EXAMEN_PRACTICO_V2
```

Una vez dentro de la carpeta, se instalan las dependencias. Para ello debe crear un virtual environment de la siguiente manera:

```
[LINUX/MAC] > python3 -m venv venv
[WINDOWS] > py.exe -m venv env
```

Si no tiene instalado venv, Lo puede instalar de la siguiente manera:

```
[LINUX/MAC] > python3 -m pip install --user virtualenv
[WINDOWS] > py.exe -m pip install --user virtualenv
```

Una vez creado el virtual environment lo activamos para poder instalar las dependencias:

```
[LINUX/MAC] > source venv/bin/activate
[WINDOWS] > .\env\Scripts\activate
```

Instalamos las dependencias con pip:

```
pip3 install -r flaskr/requirements.txt 
```

En un terminal distinto a donde se está ejecutando la aplicación, ejecutar los seeders de la colección Productions para llenar la base de datos con los datos iniciales:
```
mongoimport -d moviesbdnr -c production --file ./flaskr/seeders/production.json --jsonArray
```

> [!NOTE]  
> Si no ha realizado la práctica, deberá también ejecutar los seeders para user y movies, tal y como se indica en el siguiente fragmento de código.

```
mongoimport -d moviesbdnr -c user --file ./flaskr/seeders/user.json --jsonArray
mongoimport -d moviesbdnr -c movie --file ./flaskr/seeders/movie.json --jsonArray
```

Comprobar que los datos han sido guardados en cada una de las colecciones. Para ello, se debe usar la mongo shell para conectarse a la bbdd y realizar un find en cada una de las colecciones.

Ahora podemos arrancar el servidor con el siguiente comando (Debemos tener arrancado MongoDB):

```
flask --app ./flaskr/run.py  run --debug
```

Abra un navegador y vaya a la url "http://localhost:5000" para ver la aplicación.

Si necesita arrancar la aplicación en un puerto diferente al predeterminado puede usar el siguiente comando (reemplazando el 5002 por el puerto correspondiente):

```
flask --app ./flaskr/run.py  run --debug --port=5002
```

> [!NOTE]  
> Si ha modificado algun documento de manera indeseada y se quiere volver a restablecer los valores por defecto, borre la base de datos que ha creado, repita los seeders y vuelva a arrancar el servidor con flask.
