from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from vega_datasets import data

players = pd.read_csv("static/mineros_players.csv")


"""
# Gráficas de desempeño

Estas gráficas tienen un conjunto de métricas seleccionadas a partir de técnicas de inteligencia artificial.
Cada barra representa la fuerza relativa del jugador en cada una de las métricas.
La distancia que existe de la barra al centro indica el percentil comparado con la base de datos completa.

La descripción completa la encontrarás en al entrada [Gráfica de desempeño de jugadores](https://www.nies.futbol/2023/07/grafica-de-desempeno-de-jugadores.html).
"""


# ----------------- game start --------

st.subheader("Selecciona un jugador")

player = st.selectbox(
    'Jugador', players["Player"].to_list(),
    )

if st.button('Muestra la gráfica de desempeño'):
    st.image(f"static/{player}.jpg")

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
