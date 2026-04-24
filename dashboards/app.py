from pathlib import Path
import unicodedata

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================

st.set_page_config(
    page_title="Dashboard de Focos de Incêndio - MG",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "final"


# ============================================================
# ESTILO VISUAL - DARK THEME
# ============================================================

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #0f1117;
            color: #e5e7eb;
        }

        [data-testid="stSidebar"] {
            background-color: #151922;
            border-right: 1px solid #2d3748;
        }

        .main-title {
            font-size: 2.4rem;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 0.3rem;
        }

        .section-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #f97316;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }

        .ai-notice {
            background: linear-gradient(135deg, #111827, #1f2937);
            border: 1px solid #334155;
            border-left: 6px solid #38bdf8;
            padding: 1rem 1.2rem;
            border-radius: 14px;
            margin: 1rem 0 1.4rem 0;
            color: #dbeafe;
        }

        .insight-box {
            background: linear-gradient(135deg, #2a1607, #431407);
            border-left: 6px solid #f97316;
            padding: 1rem 1.2rem;
            border-radius: 12px;
            margin: 1rem 0;
            color: #fed7aa;
        }

        .info-box {
            background: #151922;
            border: 1px solid #334155;
            padding: 1rem 1.2rem;
            border-radius: 12px;
            margin: 1rem 0;
            color: #e5e7eb;
        }

        div[data-testid="stMetric"] {
            background-color: #151922;
            border: 1px solid #334155;
            padding: 1rem;
            border-radius: 14px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.25);
        }

        div[data-testid="stMetric"] label {
            color: #cbd5e1 !important;
        }

        div[data-testid="stMetricValue"] {
            color: #f8fafc !important;
        }

        div[data-testid="stMetricDelta"] {
            color: #fb923c !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

@st.cache_data
def load_municipios_data() -> pd.DataFrame:
    file_path = DATA_DIR / "dados_municipios.csv"

    if not file_path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(file_path)
    except Exception as erro:
        st.error(f"Erro ao carregar dados municipais: {erro}")
        return pd.DataFrame()


def show_image(relative_path: str, caption: str | None = None) -> None:
    image_path = BASE_DIR / relative_path

    if image_path.exists():
        st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: `{relative_path}`")


def show_html_map(relative_path: str, height: int = 650) -> None:
    map_path = BASE_DIR / relative_path

    if not map_path.exists():
        st.warning(f"Mapa não localizado: `{relative_path}`")
        return

    try:
        html_map = map_path.read_text(encoding="utf-8")
        components.html(html_map, height=height, scrolling=True)
    except Exception as erro:
        st.error(f"Erro ao carregar o mapa: {erro}")


def normalize_file_name(value: str) -> str:
    text = str(value).strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = "".join(char if char.isalnum() else "_" for char in text)
    text = "_".join(part for part in text.split("_") if part)
    return text


def find_column(df: pd.DataFrame, possible_names: list[str]) -> str | None:
    normalized_columns = {col.strip().lower(): col for col in df.columns}

    for name in possible_names:
        key = name.strip().lower()
        if key in normalized_columns:
            return normalized_columns[key]

    return None


def create_ranking_estados_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Posição": list(range(1, 11)),
            "Estado": [
                "PARÁ", "MATO GROSSO", "MARANHÃO", "AMAZONAS", "TOCANTINS",
                "PIAUÍ", "RONDÔNIA", "BAHIA", "MINAS GERAIS", "ACRE",
            ],
            "Número de Focos": [393955, 317760, 229624, 162838, 140215, 118402, 111008, 106858, 94619, 80451],
        }
    )


def create_ranking_municipios_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Posição": list(range(1, 11)),
            "Município": [
                "PARACATU", "JOÃO PINHEIRO", "LASSANCE", "UBERABA", "UNAÍ",
                "DIAMANTINA", "UBERLÂNDIA", "ARINOS", "BURITIZEIRO", "JAÍBA",
            ],
            "Número de Focos": [1727, 1383, 1342, 1267, 1103, 1053, 1026, 924, 885, 879],
        }
    )


def format_number_br(value: int | float) -> str:
    try:
        return f"{int(value):,}".replace(",", ".")
    except Exception:
        return str(value)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔥 Navegação")
section = st.sidebar.radio(
    "Selecione uma seção:",
    [
        "Visão Geral - MG",
        "Análises de Minas Gerais",
        "Ranking Nacional",
        "Mapa de Calor",
        "Análises por Município",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("Dashboard de focos de incêndio entre 2015 e 2025.")


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown('<div class="main-title">🔥 Dashboard de Focos de Incêndio</div>', unsafe_allow_html=True)
st.markdown(
    "Análise exploratória de focos de incêndio no Brasil, com foco principal no estado de **Minas Gerais**."
)
st.markdown(
    """
    <div class="ai-notice">
    <strong>Aviso sobre a criação do dashboard:</strong><br>
    Este dashboard foi feito por IA, utilizando o ChatGPT, a partir de um prompt de autoria do responsável pelo projeto.
    Ele tem apenas a finalidade de exemplificar e reunir as análises e visualizações já produzidas, não estando presente
    nas questões, ideias das visualizações e informações reunidas.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("---")


# ============================================================
# 1. VISÃO GERAL
# ============================================================

if section == "Visão Geral - MG":
    st.markdown('<div class="section-title">1. Visão Geral — Minas Gerais</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-box">
        Este dashboard apresenta análises sobre focos de incêndio registrados entre <strong>2015 e 2025</strong>,
        destacando a evolução anual dos registros, a variação percentual, os biomas mais afetados,
        a distribuição mensal dos focos, o ranking nacional e análises específicas por município.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Maior registro", "2021", "12.110 focos")
    col2.metric("Menor registro", "2018", "4.627 focos")
    col3.metric("Mês mais crítico", "Setembro", "Maior ocorrência")
    col4.metric("Ranking nacional", "9º lugar", "Minas Gerais")

    st.markdown(
        """
        <div class="insight-box">
        <strong>Insight principal:</strong> Minas Gerais apresentou seu maior pico de focos em 2021,
        enquanto 2018 foi o ano com menor número de registros. O mês de setembro se destaca como
        o período mais crítico, reforçando a influência do clima seco no aumento das ocorrências.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# 2, 3, 4, 6. ANÁLISES DE MINAS GERAIS
# ============================================================

elif section == "Análises de Minas Gerais":
    st.markdown('<div class="section-title">2. Focos de incêndio por ano em Minas Gerais</div>', unsafe_allow_html=True)
    st.write("O gráfico abaixo mostra a evolução anual dos focos de incêndio em Minas Gerais.")
    show_image("assets/graficosMg/num_focos_anos_mg.png", "Número de focos de incêndio por ano em Minas Gerais")

    st.markdown("---")
    st.markdown('<div class="section-title">3. Taxa de Variação Anual dos Focos de Incêndio</div>', unsafe_allow_html=True)
    st.write("A taxa de variação anual indica o crescimento ou a redução dos focos de incêndio em relação ao ano anterior.")
    st.code("Taxa = ((F_atual - F_anterior) / F_anterior) * 100", language="text")
    show_image("assets/graficosMg/variacao_focos_mg.png", "Taxa de variação anual dos focos de incêndio em Minas Gerais")

    st.markdown("---")
    st.markdown('<div class="section-title">4. Biomas mais afetados em Minas Gerais</div>', unsafe_allow_html=True)
    st.write("Esta seção apresenta a distribuição dos focos por bioma.")
    show_image("assets/graficosMg/biomas_mg.png", "Biomas mais afetados em Minas Gerais")

    st.markdown("---")
    st.markdown('<div class="section-title">6. Número de focos de incêndio por mês</div>', unsafe_allow_html=True)
    st.write("A análise mensal permite identificar os períodos do ano com maior concentração de focos de incêndio.")
    show_image("assets/graficosMg/num_focos_mes_mg.png", "Número de focos de incêndio por mês em Minas Gerais")
    st.markdown(
        """
        <div class="insight-box">
        <strong>Insights:</strong><br>
        • O mês com maior ocorrência de focos de incêndio em Minas Gerais foi <strong>setembro</strong>.<br>
        • A maior parte dos focos ocorreu durante o <strong>inverno</strong>, período mais seco do ano no estado.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# 5. RANKING NACIONAL
# ============================================================

elif section == "Ranking Nacional":
    st.markdown('<div class="section-title">5. Ranking nacional dos estados mais afetados</div>', unsafe_allow_html=True)
    ranking_estados = create_ranking_estados_df()

    styled_ranking = ranking_estados.style.apply(
        lambda row: [
            "background-color: #7c2d12; color: #ffedd5; font-weight: bold"
            if row["Estado"] == "MINAS GERAIS"
            else "background-color: #111827; color: #e5e7eb"
            for _ in row
        ],
        axis=1,
    ).format({"Número de Focos": format_number_br})

    st.dataframe(styled_ranking, use_container_width=True, hide_index=True)

    st.markdown(
        """
        <div class="insight-box">
        <strong>Insight:</strong> Minas Gerais aparece como o <strong>9º estado mais afetado</strong>
        no ranking nacional, com <strong>94.619 focos</strong> registrados no período analisado.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# 7. MAPA DE CALOR
# ============================================================

elif section == "Mapa de Calor":
    st.markdown('<div class="section-title">7. Mapa de calor dos focos de incêndio</div>', unsafe_allow_html=True)
    st.write("O mapa de calor permite visualizar espacialmente as regiões mais afetadas por focos de incêndio em Minas Gerais.")
    show_html_map("maps/HeatMapMG.html", height=650)


# ============================================================
# 8. ANÁLISES POR MUNICÍPIO
# ============================================================

elif section == "Análises por Município":
    st.markdown('<div class="section-title">8. Análises por Município</div>', unsafe_allow_html=True)

    st.subheader("Ranking dos municípios mais afetados")
    ranking_municipios = create_ranking_municipios_df()
    st.dataframe(
        ranking_municipios.style.apply(
            lambda row: ["background-color: #111827; color: #e5e7eb" for _ in row],
            axis=1,
        ).format({"Número de Focos": format_number_br}),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")
    st.subheader("Seleção de município")

    df_municipios = load_municipios_data()

    if df_municipios.empty:
        st.warning("Arquivo `data/final/dados_municipios.csv` não encontrado ou vazio.")
    else:
        municipio_col = find_column(df_municipios, ["municipio", "Município", "Municipio", "cidade", "Cidade"])

        if municipio_col is None:
            st.error("Não foi possível encontrar uma coluna de município no arquivo `dados_municipios.csv`.")
            st.write("Colunas disponíveis:", list(df_municipios.columns))
        else:
            municipios = sorted(df_municipios[municipio_col].dropna().astype(str).unique())
            municipio_selecionado = st.selectbox(
                "Selecione um município:",
                municipios,
                index=municipios.index("DIVINÓPOLIS") if "DIVINÓPOLIS" in municipios else 0,
            )

            df_filtrado = df_municipios[
                df_municipios[municipio_col].astype(str).str.upper() == municipio_selecionado.upper()
            ]

            col1, col2, col3 = st.columns(3)
            col1.metric("Município selecionado", municipio_selecionado)
            col2.metric("Registros encontrados", len(df_filtrado))

            focos_col = find_column(df_filtrado, ["Numero_Focos", "Número de Focos", "Numero Focos", "Focos", "focos"])

            if focos_col and not df_filtrado.empty:
                total_focos = pd.to_numeric(df_filtrado[focos_col], errors="coerce").sum()
                col3.metric("Total de focos", format_number_br(total_focos))
            else:
                col3.metric("Total de focos", "N/D")

            st.write("Dados filtrados do município:")
            st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

            st.markdown("---")
            st.subheader("Visualizações do município")

            municipio_arquivo = normalize_file_name(municipio_selecionado)

            show_image(
                f"assets/graficosMunicipiosTaxa/grafico_taxa_{municipio_arquivo}.png",
                "Taxa de variação anual do município",
            )

            show_image(
                f"assets/graficosMunicipiosMes/grafico_mes_{municipio_arquivo}.png",
                "Focos por mês no município",
            )

            st.markdown("#### Mapa interativo do município")
            show_html_map(f"assets/mapas/mapa_focos_{municipio_arquivo}.html", height=600)
