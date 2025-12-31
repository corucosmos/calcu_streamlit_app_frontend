# frontend/app.py
import os
import streamlit as st
import requests
import json
import pandas as pd

# Configuración de la página∫
st.set_page_config(
    page_title="Calcu-Streamlit-App",
    page_icon="🚀",
    layout="wide"
)

# Configuración del backend
#BACKEND_URL = "http://localhost:8000"  # Cambia si tu backend está en otro puerto
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

# Título de la aplicación
st.title("🚀 Calcu-Streamlit-App")
st.markdown("---")

# Sidebar para navegación
st.sidebar.title("📊 App")
pagina = st.sidebar.radio(
    "",
    ["🏠 Inicio", "🧮 Calculadora"]
)

# Página de Inicio
if pagina == "🏠 Inicio":
    st.header("Bienvenido a la Aplicación")
    st.markdown("""
    Esta es una aplicación de ejemplo que demuestra cómo integrar:
    
    - **Frontend**: Streamlit para la interfaz de usuario **Calculadora**
    - **Backend**: FastAPI para la lógica de la App y API REST
    
    ### Características:
    **Calculadora**: Realiza operaciones matemáticas básicas

    """)

# Página de Calculadora
elif pagina == "🧮 Calculadora":
    st.header("Calculadora")
    
    col1, col2 = st.columns(2)
    
    with col1:
        a = st.number_input("Primer número:", value=10.0)
        b = st.number_input("Segundo número:", value=5.0)
    
    with col2:
        operacion = st.selectbox(
            "Selecciona la operación:",
            ["suma", "resta", "multiplicacion", "division"]
        )
        
        if st.button("Calcular", type="primary", use_container_width=True):
            try:
                payload = {
                    "a": a,
                    "b": b,
                    "operacion": operacion
                }
                
                response = requests.post(
                    f"{BACKEND_URL}/calcular",
                    json=payload
                )
                
                if response.status_code == 200:
                    resultado = response.json()
                    
                    # Mostrar resultado
                    st.success(f"✅ Resultado: {resultado['resultado']}")
                    
                    # Mostrar detalles en un expander
                    with st.expander("Ver detalles de la operación"):
                        st.json(resultado)
                else:
                    st.error(f"Error: {response.json()['detail']}")
                    
            except Exception as e:
                st.error(f"Error al conectar con el backend: {e}")

st.sidebar.markdown("---")

st.markdown("---")

try:
    response = requests.get(f"{BACKEND_URL}/health", timeout=5)
    if response.status_code == 200:
        st.success("✅ Backend conectado correctamente")
    else:
        st.warning("⚠️ Backend respondió con un estado inesperado")
except requests.exceptions.ConnectionError:
    st.error("❌ No se pudo conectar al backend. Asegúrate de que esté ejecutándose.")
    st.info("Ejecuta el backend con: `uvicorn backend.api:app --reload`")

st.markdown("---")