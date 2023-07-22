from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Plataforma Interactiva para Transferencias Óptimas

Estas gráficas tienen un conjunto de métricas seleccionadas a partir de técnicas de inteligencia artificial.
Cada barra representa la fuerza relativa del jugador en cada una de las métricas.
La distancia que existe de la barra al centro indica el percentil comparado con la base de datos completa.
"""


# ----------------- game start --------

st.subheader("Selecciona un jugador")

player = st.selectbox(
    'Jugador', ['R. Alvarado', 'H. Martín'],
    )

if st.button('Muestra la gráfica de desempeño'):
    st.image(f"static/{player}.jpg")
