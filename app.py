import streamlit as st
import pandas as pd
import plotly.express as px

#Lectura de archivo 'vehicles_us.csv'
car_data = pd.read_csv('vehicles_us.csv')

#Creación de header
st.header('Ventas de Coches - Análisis de datos visuales')


hist_button = st.checkbox('Presiona aquí para construir un histograma de los datos') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Visualización de histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.checkbox('Presiona aquí para construir un diagrama de dispersión de los datos')

if scatter_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Visualización de diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)