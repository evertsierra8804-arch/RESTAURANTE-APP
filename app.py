import streamlit as st
import pandas as pd

st.title("🍽️ Menú del Restaurante")

# Cargar el menú desde el archivo CSV
df = pd.read_csv("menu.csv")

# Mostrar el menú
st.write("Selecciona lo que deseas pedir:")

# Iterar sobre cada fila del CSV para crear los botones
for index, row in df.iterrows():
    if st.button(f"Pedir {row['plato']} (${row['precio']})"):
        st.success(f"Has pedido: {row['plato']}")