import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
data_file = '/mnt/c/Users/aleja/OneDrive/Documentos/AT/Data Analyst/Sprint 6/my_proyect/Sprint-6-Proyect/notebooks/vehicles_us.csv'
car_data = pd.read_csv(data_file)

# Mostrar información básica del DataFrame
st.write("Información del conjunto de datos:")
st.dataframe(car_data)

# Crear un botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma basado en el odómetro
    fig_hist = px.histogram(car_data, x="odometer", title='Histograma de Odometer')

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear un botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión basado en el precio y el odómetro
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title='Gráfico de Dispersión: Precio vs Odometer')

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
