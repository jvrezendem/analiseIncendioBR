import streamlit as st
import pandas
from streamlit.components.v1 import html
from pathlib import Path 


BASE_DIR = Path(__file__).resolve().parent     
ROOT_DIR = BASE_DIR.parent                      
def p(*parts):                                  
    return ROOT_DIR.joinpath(*parts)


st.set_page_config(
    page_title="Focos de Incêncio no Brasil",
    layout="wide"
)

col1, col2, col3 = st.columns([1,4,1])

with col2:

    st.subheader("Dados do INPE (Instituto Nacional de Pesquisas Espaciais)")

    st.subheader("Gráficos")

    st.image(str(p("assets", "fireBiomas.png")), width=1600)

    st.image(str(p("assets", "fireEstados.png")), width=1600)

    st.subheader("Mapas interativos")

    mapPath = p("maps", "heatMap.html")

    with open(mapPath, "r", encoding="utf-8") as f:
        mapaHtml = f.read()

    html(mapaHtml, width=1600, height=800)