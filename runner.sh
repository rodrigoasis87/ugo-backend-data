#!/bin/bash

if [ -z "$APP" ]; then
    echo "Uso: $0 [api|web]"
    exit 1
fi

if [ "$APP" = "api" ]; then
    uvicorn api.main:app --host 0.0.0.0 --port $PORT
elif [ "$APP" = "web" ]; then
    streamlit run web/streamlit_app.py --server.address=0.0.0.0 --server.port=$PORT
else
    echo "Opción no válida. Se recibió:" $APP
    echo "El parámetro de entrada debe ser: api o web."
    exit 1
fi
