# Usa una imagen oficial de Python 3.10.12 como imagen base
FROM python:3.10.12-slim

# Establece el directorio de trabajo dentro del contenedor a /app
WORKDIR /app

# Copia el archivo de dependencias al directorio de trabajo actual
COPY ../requirements.txt .

# Instala las dependencias enumeradas en el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del directorio de trabajo actual dentro del contenedor
COPY . .

# Expone el puerto 8000 para que el contenedor sea accesible
EXPOSE 8000

# Usa Uvicorn para servir la aplicación, reemplaza `app:app` con tu aplicación y punto de entrada
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
