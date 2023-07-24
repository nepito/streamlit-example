from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from vega_datasets import data

source = data.seattle_weather()

"""
# Plataforma Interactiva para Transferencias Óptimas

Estas gráficas tienen un conjunto de métricas seleccionadas a partir de técnicas de inteligencia artificial.
Cada barra representa la fuerza relativa del jugador en cada una de las métricas.
La distancia que existe de la barra al centro indica el percentil comparado con la base de datos completa.

La descripción completa la encontrarás en al entrada [Gráfica de desempeño de jugadores](https://www.nies.futbol/2023/07/grafica-de-desempeno-de-jugadores.html).
"""


# ----------------- game start --------

st.subheader("Selecciona un jugador")

player = st.selectbox(
    'Jugador', ['R. Alvarado', 'H. Martín'],
    )

if st.button('Muestra la gráfica de desempeño'):
    st.image(f"static/{player}.jpg")

st.altair_chart(
    alt.Chart(source, title="Daily Max Temperatures (C) in Seattle, WA").mark_rect().encode(
        x=alt.X("date(date):O", title="Day", axis=alt.Axis(format="%e", labelAngle=0)),
        y=alt.Y("month(date):O", title="Month"),
        color=alt.Color("max(temp_max)", legend=alt.Legend(title=None)),
        tooltip=[
            alt.Tooltip("monthdate(date)", title="Date"),
            alt.Tooltip("max(temp_max)", title="Max Temp"),
        ],
    ).configure_view(step=13, strokeWidth=0).configure_axis(domain=False)
)

st.dataframe(source)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
