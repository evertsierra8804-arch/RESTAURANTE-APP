import streamlit as st
import pandas as pd

st.title("🍽️ Menú del Restaurante")

# Leer el menú
df = pd.read_csv("menu.csv")

# Mostrar el menú
st.write("Selecciona lo que deseas pedir:")
for index, row in df.iterrows():
    if st.button(f"Pedir {row['plato']} (${row['precio']})"):
        st.success(f"Has pedido: {row['plato']}")