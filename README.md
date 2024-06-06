# Comandos útiles para tener a mano

Para ejecutar la API directamente sin necedidad de Docker:

    uvicorn api.main:app --reload

Para construir (_build_) la imagen Docker que expondrá la API REST:
    
    docker build -t ugo-backend-data-api:latest -f api/Dockerfile .
    
Para ejecutar la imagen anterior en un contenedor Docker:

    docker run -d -p 8000:8000 ugo-backend-data-api:latest

Para construir (_build_) la imagen Docker que levantará la interfaz web de Streamlit:

    docker build -t ugo-backend-data-web:latest -f web/Dockerfile .

Para ejecutar la imagen anterior en un contenedor Docker:

    docker run -d -p 8501:8501 ugo-backend-data-web:latest

Comando para levantar ambos servicios con visibilidad a nivel de red:

    docker-compose up --build

Importante: Ambas imágenes de Docker tienen que estar previamente construidas.

# Comandos adicionales

Si los contenedores se están ejecutando dentro de un entorno WSL de Windows, usar el siguiente comando para conocer la IP de acceso desde afuera:

    ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'

La siguiente función Bash es útil para automatizar la creación de un entorno virtual de Python.
Adicionalmente, activa el entorno virtual recién creado, crea el archivo _requirements.txt_ e ignora la carpeta de entorno en Git y Docker.

    cpea() {
        python3 -m venv ${PWD##*/}-venv
        source ${PWD##*/}-venv/bin/activate
        pip freeze > requirements.txt
        echo ${PWD##*/}-venv >> .gitignore
        echo ${PWD##*/}-venv >> .dockerignore
    }
