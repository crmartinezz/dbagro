import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Base de Datos AgroColombiano",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Base de Datos AgroColombiano")
st.sidebar.title("🔍 Opciones de Navegación")
# Establecer semilla para reproducibilidad
np.random.seed(42)

menu = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Inicio", "Datos", "Visualización", "Configuración"]
)
# Generación de la base de datos
data_agro = pd.DataFrame({
    "Fecha": pd.date_range(start="2024-01-01", periods=150, freq="D"),
    "Producto": np.random.choice(["Café", "Banano", "Arroz", "Maíz", "Yuca", "Soya", "Caña de azúcar", "Papas"], size=150),
    "Cantidad_Producción": np.random.randint(1000, 10000, size=150),  # Cantidad de producción en kilogramos
    "Precio_Uni": np.random.uniform(1000, 3000, size=150),  # Precio unitario en COP
    "Descuento": np.random.uniform(5, 20, size=150),  # Descuento en porcentaje
    "Satisfacción": np.random.randint(1, 10, size=150),  # Satisfacción de los productores
    "Región": np.random.choice(["Antioquia", "Cundinamarca", "Santander", "Tolima", "Valle del Cauca", "Magdalena", "Nariño", "Cesar"], size=150),
    "Tipo_Clima": np.random.choice(["Tropical", "Templado", "Cálido", "Frío"], size=150)
})
if menu == "Datos":
    st.subheader("📂 Datos Generados")
    st.dataframe(data)
# Mostrar las primeras filas de la base de datos generada
data_agro.head()
