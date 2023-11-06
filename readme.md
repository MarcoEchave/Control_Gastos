## instalacion del proyecto 

### El primer paso es descargar el repositorio con el siguiente comando desde la terminal

>git clone https://github.com/MarcoEchave/Control_Gastos.git

### Una vez descargado el proyecto hay que moverse al proyecto y crear el ambiete virtual 

>python -m venv env
### Posteriormente hay que activar el entorno virtual 
### activacion para sistemas UNIX
>source env/bin/activate

### activacion para windows
>env\Scripts\activate

### una vez activado, se procedde a instalar los paquetes

> pip install -r requirement.txt
### Posteriormente se mueve de directorio al proyecto y se hacen las migraciones correspondienes 
>cd controlGastos

>python manage.py migrate 

>python manage.py makemigrations

### Hechas las migraciones se procede a correr el prograna

>python manage.py runserver
