import streamlit as st
import pandas
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Focos de Incêncio no Brasil",
    layout="wide"
)

col1, col2, col3 = st.columns([1,4,1])

with col2:

    st.subheader("Dados do INPE (Instituto Nacional de Pesquisas Espaciais)")

    st.subheader("Gráficos")

    st.image("/incendioD3/assets/fireBiomas.png", width=1600)

    st.image("/incendioD3/assets/fireEstados.png", width=1600)

    st.subheader("Mapas interativos")

    mapPath = "/incendioD3/maps/heatMap.html"

    with open(mapPath, "r", encoding="utf-8") as f:
        mapaHtml = f.read()

    html(mapaHtml, width=1600, height=800)