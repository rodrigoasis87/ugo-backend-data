import streamlit as st
import requests

st.title('Ugo! App - Backend Data Analytics Service')

name = st.text_input('Nombre')
description = st.text_area('Descripción')

if st.button('Crear ítem'):
    response = requests.post('http://localhost:8000/items/', json={'name': name, 'description': description})
    if response.status_code == 200:
        st.success('Ítem creado exitosamente!')
    else:
        st.error('Algo salió mal')

if st.button('Mostrar ítems'):
    response = requests.get('http://fastapi_app:8000/items/')
    if response.status_code == 200:
        items = response.json()
        for item in items:
            st.write(f"Nombre: {item['name']}, Texto: {item['text']}")
    else:
        st.error('Algo salió mal')
