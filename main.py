import pandas as pd 
import numpy as np
import streamlit as st

st.header("Evaluacion del Momento 2")

# Título de la aplicación
st.title("Análisis Básico de Ventas")

# Cargar el dataset
df = pd.read_csv("static/datasets/sales_data.csv")

# Mostrar dataset completo
st.subheader("Datos Completos")
st.dataframe(df)


# Filtros en la barra lateral
st.sidebar.header("Filtros")

category = st.sidebar.selectbox(
    "Selecciona una categoría",
    options=['Todas', 'Electronics', 'Accessories']
)


min_price = int(df['Price'].min())
max_price = int(df['Price'].max())
price_range = st.sidebar.slider(
    "Selecciona un rango de precios",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)


# Aplicar filtros

filtered_df = df[
    (df['Price'] >= price_range[0]) &
    (df['Price'] <= price_range[1])
]

if category != 'Todas':
    filtered_df = filtered_df[filtered_df["Category"] == category]

# Mostrar datos filtrados
st.subheader("Datos Filtrados")
st.dataframe(filtered_df)
st.write(f"Total de registros: {len(filtered_df)}")
st.write(f"Rango de precios: {price_range[0]} - {price_range[1]}")


# Estadísticas
st.subheader("Estadísticas")
if not filtered_df.empty:
    total_sales = filtered_df['Total_Sales'].sum()
    avg_price = filtered_df['Price'].mean()
    st.metric("Total de Ventas", f"${total_sales:,.2f}")
    st.metric("Precio Promedio", f"${avg_price:,.2f}")
else:
    st.write("No hay datos para los filtros seleccionados.")