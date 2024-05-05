import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components
import requests


# Función para filtrar experiencias por nombre
def filter_by_name(items, keyword):
    filtered_by_name = []
    for item in items:
        if keyword.lower() in item["name"].lower():
            filtered_by_name.append(item)
    return filtered_by_name


# Función para filtrar experiencias por tipo
def filter_by_type(items, keyword):
    filtered_by_type = []
    for item in items:
        if keyword.lower() in item["type"].lower():
            filtered_by_type.append(item)
    return filtered_by_type


if st.button("Buscar experiencia"):
    response = requests.get("http://localhost:8000/experience/")
    if response.status_code == 200:
        items = response.json()

        # Widget de entrada de texto para el término de búsqueda
        search_name = st.text_input("Buscar por nombre de experiencia:")

        search_type = st.text_input("Buscar por tipo de experiencia:")

        # Filtrar experiencias según el término de búsqueda
        filtered_name = filter_by_name(items, search_name)

        filtered_type = filter_by_type(items, search_type)

        for item in filtered_name:
            st.write(
                f"Nombre: {item['name']}, Tipo: {item['type']}, Descripción: {item['description']}"
            )
            # Botón para abrir el modal de revisión
            review_button_id = f"review_button_{item['id']}"
            if st.button(f"Dejar review para {item['name']}", key=review_button_id):
                # Aquí deberías abrir el modal correspondiente
                st.write(f"Ingresar review para {item['name']}")

        for item in filtered_type:
            st.write(
                f"Nombre: {item['name']}, Tipo: {item['type']}, Descripción: {item['description']}"
            )
            # Botón para abrir el modal de revisión
            review_button_id = f"review_button_{item['id']}"
            if st.button(f"Dejar review para {item['name']}", key=review_button_id):
                # Aquí deberías abrir el modal correspondiente
                st.write(f"Ingresar review para {item['name']}")

    else:
        st.error("Algo salió mal")


# Modal de revisión
def review_modal(experience_id):
    st.write(f"Modal para revisión de la experiencia con ID {experience_id}")
    # Aquí puedes agregar un formulario para ingresar la revisión


# Ejemplo de cómo llamar al modal
review_modal(
    1
)  # Deberías llamar a esta función con el ID de la experiencia correspondiente al botón presionado
