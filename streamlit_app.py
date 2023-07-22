from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Plataforma Interactiva para Transferencias Optimas

![](./app/static/logo.jpeg)
"""


# ----------------- game start --------

st.subheader("| Intro")
st.image("static/R. Alvarado.jpg")

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

player = st.text_input('Type an animal')

if st.button('Check availability'):
    st.image(f"static/{player}")
