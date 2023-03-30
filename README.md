# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME

# Respuestas de la tarea
1. ¿Cual es su entrada? R: La entrada del script es el url de la pagina a escanear. 
2. ¿Que procesamiento esta haciendo? R: Pide al url las peliculas mas populares de IMDB y las escribe en un archivo csv. 
3. ¿Cual es su salida? R: Un archivo csv en el cual podemos utilizar para un futuro.

#Principios SOLID
S - Single Responsibility: Separamos los archivos para que una clase haga 1 sola tarea y no realize de mas.

O - Open Closed Principle: Se podrian crear interfaces a las clases para poder agregar mas extensiones sin modificar la original.

L - Liskov Substitution Principle: No se esta trabajando con herencia.

I - Interface Segregation Principle: Se crean interfaces minimas para cada modulo, asi dando un uso a los metodos utilizados por el cliente.

D - Dependency Inversion: Los modulos de alto y bajo nivel no dependes de si mismos sino de abstracciones.


