from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Plataforma Interactiva para Transferencias Óptimas

![](./app/static/logo.jpeg)
"""


# ----------------- game start --------

st.subheader("Selecciona un jugador")

player = st.selectbox(
    'Jugador', ['R. Alvarado', 'H. Martín'],
    )

if st.button('Check availability'):
    st.image(f"static/{player}.jpg")
