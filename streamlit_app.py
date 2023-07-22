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

if st.session_state.stage >= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)
