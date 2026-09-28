import streamlit as st
st.title("IA Dengue - Guayaquil")
st.write("App de Jorge Fernando Cabrera - Lojas Guayas")

nombre = st.text_input("Tu nombre:")
if nombre:
    st.success(f"Hola {nombre}, tu app ya funciona!")
