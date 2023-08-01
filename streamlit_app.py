from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from vega_datasets import data

players = pd.read_csv("static/players_streamlit.csv")


"""
# Gráficas de desempeño

Estas gráficas tienen un conjunto de métricas seleccionadas a partir de técnicas de inteligencia artificial.
Cada barra representa la fuerza relativa del jugador en cada una de las métricas.
La distancia que existe de la barra al centro indica el percentil comparado con la base de datos completa.

La descripción completa la encontrarás en al entrada [Gráfica de desempeño de jugadores](https://www.nies.futbol/2023/07/grafica-de-desempeno-de-jugadores.html).
"""


# ----------------- game start --------
tab1, tab2 = st.tabs(["Jugadores", "Equipos"])

with tab1:
    st.subheader("Selecciona un jugador")
    player = st.selectbox('Jugador', players["Player"].to_list(),)
    if st.button('Muestra la gráfica de desempeño'):
        st.image(f"static/{player}.jpg")

with tab2:
    data = pd.read_csv('static/played_minutes.csv')
    played_minutes = data[data.team == "Mineros de Zacatecas"]

# Crear el gráfico de Altair
    chart = alt.Chart(played_minutes, title="Minutes Played by Player and Match").mark_rect().encode(
        alt.X("match:O", sort=alt.EncodingSortField(field="date", op="sum", order="descending")).title("Match"),
        alt.Y("player:O").title("Player"),
        alt.Color("minutes:Q", scale=alt.Scale(scheme='blues')).title("Minutes"),
        tooltip=[
            alt.Tooltip("match:O", title="Match"),
            alt.Tooltip("player:O", title="Player"),
            alt.Tooltip("minutes:Q", title="Minutes"),
        ],
    ).configure_view(
        step=13,
        strokeWidth=0
    ).configure_axis(
        domain=False
    )
    st.altair_chart(chart)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
