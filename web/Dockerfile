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

# Expone el puerto que Streamlit utiliza por defecto (8501)
EXPOSE 8501

# Comando para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "web/streamlit_app.py", "--server.address=0.0.0.0"]
