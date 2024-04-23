import streamlit as st
import requests

st.title('Ugo! App - Backend Data Analytics Service')

country_province = {
    "Argentina": ["Buenos Aires", "Córdoba", "Mendoza", "Neuquén"],
    "México": ["DF", "Playa del Carmen", "Tulum", "Chiapas", "Puebla"]
}

name = st.text_input('Nombre')
type_value = st.text_input('Categoría')
description = st.text_area('Descripción')
country = st.selectbox('País', list(country_province.keys()))
province = st.selectbox('Provincia', country_province[country])
price_min = st.number_input('Precio mínimo', step=1)
price_max = st.number_input('Precio máximo', step=1)

if st.button('Crear experiencia'):
    response = requests.post('http://localhost:8000/experience/',
                             json={'name': name, 'type': type_value, 'description': description, 
                                   'country': country, 'province': province, 'price_min': price_min,
                                   'price_max': price_max})
    if response.status_code == 201:
        st.success('Ítem creado exitosamente!')
    else:
        st.error('Algo salió mal')

if st.button('Mostrar experiencias'):
    response = requests.get('http://localhost:8000/experience/')
    if response.status_code == 200:
        items = response.json()
        for item in items:
            st.write(f"Nombre: {item['name']}")
    else:
        st.error('Algo salió mal')


if st.button('Editar experiencias'):
    respone = requests.put('')