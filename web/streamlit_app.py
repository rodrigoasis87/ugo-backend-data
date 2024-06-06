import os

from dotenv import load_dotenv
import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components
import requests

load_dotenv(override=True)

API_URL = os.getenv("API_URL")

st.title("Ugo! App - Backend Data Analytics Service")

modal = Modal(
    "Demo Modal",
    key="demo-modal",
)

open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")

#         html_string = '''
#         <h1>HTML string in RED</h1>

#         <script language="javascript">
#             document.querySelector("h1").style.color = "red";
#         </script>
#         '''
#         components.html(html_string)

#         st.write("Some fancy text")
#         value = st.checkbox("Check me")
#         st.write(f"Checkbox checked: {value}")

country_province = {
    "Argentina": ["Buenos Aires", "Córdoba", "Mendoza", "Neuquén"],
    "México": ["DF", "Playa del Carmen", "Tulum", "Chiapas", "Puebla"],
}

name = st.text_input("Nombre")
type_value = st.text_input("Categoría")
description = st.text_area("Descripción")
country = st.selectbox("País", list(country_province.keys()))
province = st.selectbox("Provincia", country_province[country])
price_min = st.number_input("Precio mínimo", step=1)
price_max = st.number_input("Precio máximo", step=1)
discount = st.number_input("Descuento", step=1)

if st.button("Crear experiencia"):
    response = requests.post(
        f"{API_URL}/experience/",
        json={
            "name": name,
            "type": type_value,
            "description": description,
            "country": country,
            "province": province,
            "price_min": price_min,
            "price_max": price_max,
            "discount": discount
        },
    )
    if response.status_code == 201:
        st.success("Ítem creado exitosamente!")
    else:
        st.error("Algo salió mal")

# mostrar experiencias sin botón

# if st.button('Mostrar experiencias'):
#     response = requests.get(f"{API_URL}/experience/')
#     if response.status_code == 200:
#         items = response.json()
#         for item in items:
#             st.write(f"Nombre: {item['name']}")
#     else:
#         st.error('Algo salió mal')


# mostrar experiencia con botón de review

if st.button("Mostrar experiencias"):
    response = requests.get(f"{API_URL}/experience/")
    st.write(response.json())
    if response.status_code == 200:
        items = response.json()
        for item in items:
            st.write(
                f"Nombre: {item['name']}\n"
                f"Tipo: {item['type']}\n"
                f"Descripción: {item['description']}"
            )

            # if st.button("Abrir", key={item["_id"]}):
            #     modal.open()

            # if modal.is_open():
            #     with modal.container():
            #         st.write("Text goes here")

    else:
        st.error("Algo salió mal")


# editar experiencias

if st.button("Editar experiencias"):
    respone = requests.put("")


# postear reviews

if st.button("Insertar review"):
    response = requests.post(
        f"{API_URL}/experience/",
        json={
            "name": name,
            "type": type_value,
            "description": description,
            "country": country,
            "province": province,
            "price_min": price_min,
            "price_max": price_max,
        },
    )
    if response.status_code == 201:
        st.success("Ítem creado exitosamente!")
    else:
        st.error("Algo salió mal")
