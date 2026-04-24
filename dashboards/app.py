from pathlib import Path

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
ASSETS_DIR = BASE_DIR / "assets"
MAPS_DIR = BASE_DIR / "maps"
DATA_DIR = BASE_DIR / "data" / "final"


# ============================================================
# ESTILO VISUAL
# ============================================================

st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.4rem;
            font-weight: 800;
            color: #1f2933;
            margin-bottom: 0.3rem;
        }

        .section-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #263238;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }

        .insight-box {
            background: linear-gradient(135deg, #fff7ed, #ffedd5);
            border-left: 6px solid #f97316;
            padding: 1rem 1.2rem;
            border-radius: 12px;
            margin: 1rem 0;
            color: #431407;
        }

        .info-box {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            padding: 1rem 1.2rem;
            border-radius: 12px;
            margin: 1rem 0;
            color: #263238;
        }

        .mg-highlight {
            background-color: #fff3cd;
            color: #5c3d00;
            font-weight: 700;
        }

        div[data-testid="stMetric"] {
            background-color: #ffffff;
            border: 1px solid #e5e7eb;
            padding: 1rem;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
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
    """Carrega os dados finais dos municípios, caso o arquivo exista."""
    file_path = DATA_DIR / "dados_municipios.csv"

    if not file_path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(file_path)
    except Exception as erro:
        st.error(f"Erro ao carregar dados municipais: {erro}")
        return pd.DataFrame()


def show_image(relative_path: str, caption: str | None = None) -> None:
    """Exibe uma imagem da pasta do projeto com tratamento de erro."""
    image_path = BASE_DIR / relative_path

    if image_path.exists():
        st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: `{relative_path}`")


def show_html_map(relative_path: str, height: int = 650) -> None:
    """Renderiza um arquivo HTML dentro do Streamlit."""
    map_path = BASE_DIR / relative_path

    if not map_path.exists():
        st.warning(f"Mapa não localizado: `{relative_path}`")
        return

    try:
        html_map = map_path.read_text(encoding="utf-8")
        components.html(html_map, height=height, scrolling=True)
    except Exception as erro:
        st.error(f"Erro ao carregar o mapa: {erro}")


def normalize_text(value: str) -> str:
    """Normaliza textos para facilitar buscas por município."""
    return str(value).strip().upper()


def find_column(df: pd.DataFrame, possible_names: list[str]) -> str | None:
    """Encontra uma coluna considerando nomes possíveis."""
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
                "PARÁ",
                "MATO GROSSO",
                "MARANHÃO",
                "AMAZONAS",
                "TOCANTINS",
                "PIAUÍ",
                "RONDÔNIA",
                "BAHIA",
                "MINAS GERAIS",
                "ACRE",
            ],
            "Número de Focos": [
                393955,
                317760,
                229624,
                162838,
                140215,
                118402,
                111008,
                106858,
                94619,
                80451,
            ],
        }
    )


def create_ranking_municipios_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Posição": list(range(1, 11)),
            "Município": [
                "PARACATU",
                "JOÃO PINHEIRO",
                "LASSANCE",
                "UBERABA",
                "UNAÍ",
                "DIAMANTINA",
                "UBERLÂNDIA",
                "ARINOS",
                "BURITIZEIRO",
                "JAÍBA",
            ],
            "Número de Focos": [
                1727,
                1383,
                1342,
                1267,
                1103,
                1053,
                1026,
                924,
                885,
                879,
            ],
        }
    )


def format_number_br(value: int | float) -> str:
    """Formata números no padrão brasileiro."""
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
    st.write(
        "O gráfico abaixo mostra a evolução anual dos focos de incêndio em Minas Gerais, "
        "destacando os anos de maior e menor ocorrência."
    )
    show_image(
        "assets/graficosMg/num_focos_anos_mg.png",
        "Número de focos de incêndio por ano em Minas Gerais",
    )

    st.markdown("---")
    st.markdown('<div class="section-title">3. Taxa de Variação Anual dos Focos de Incêndio</div>', unsafe_allow_html=True)
    st.write(
        "A taxa de variação anual indica o crescimento ou a redução dos focos de incêndio "
        "em relação ao ano anterior."
    )
    st.code("Taxa = ((F_atual - F_anterior) / F_anterior) * 100", language="text")
    show_image(
        "assets/graficosMg/variacao_focos_mg.png",
        "Taxa de variação anual dos focos de incêndio em Minas Gerais",
    )

    st.markdown("---")
    st.markdown('<div class="section-title">4. Biomas mais afetados em Minas Gerais</div>', unsafe_allow_html=True)
    st.write(
        "Esta seção apresenta a distribuição dos focos por bioma, permitindo identificar "
        "quais formações naturais foram mais afetadas no período analisado."
    )
    show_image(
        "assets/graficosMg/biomas_mg.png",
        "Biomas mais afetados em Minas Gerais",
    )

    st.markdown("---")
    st.markdown('<div class="section-title">6. Número de focos de incêndio por mês</div>', unsafe_allow_html=True)
    st.write(
        "A análise mensal permite identificar os períodos do ano com maior concentração "
        "de focos de incêndio."
    )
    show_image(
        "assets/graficosMg/num_focos_mes_mg.png",
        "Número de focos de incêndio por mês em Minas Gerais",
    )
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
    st.write(
        "A tabela abaixo apresenta os 10 estados brasileiros com maior número de focos de incêndio "
        "no período analisado, com destaque para Minas Gerais."
    )

    ranking_estados = create_ranking_estados_df()

    styled_ranking = ranking_estados.style.apply(
        lambda row: [
            "background-color: #fff3cd; color: #5c3d00; font-weight: bold"
            if row["Estado"] == "MINAS GERAIS"
            else ""
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
    st.write(
        "O mapa de calor permite visualizar espacialmente as regiões mais afetadas por focos "
        "de incêndio em Minas Gerais."
    )

    show_html_map("maps/heatMap.html", height=650)


# ============================================================
# 8. ANÁLISES POR MUNICÍPIO
# ============================================================

elif section == "Análises por Município":
    st.markdown('<div class="section-title">8. Análises por Município</div>', unsafe_allow_html=True)

    st.subheader("Ranking dos municípios mais afetados")
    ranking_municipios = create_ranking_municipios_df()
    st.dataframe(
        ranking_municipios.style.format({"Número de Focos": format_number_br}),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")
    st.subheader("Seleção de município")

    df_municipios = load_municipios_data()

    if df_municipios.empty:
        st.warning("Arquivo `data/final/dados_municipios.csv` não encontrado ou vazio.")
    else:
        municipio_col = find_column(
            df_municipios,
            ["municipio", "Município", "Municipio", "cidade", "Cidade"],
        )

        if municipio_col is None:
            st.error(
                "Não foi possível encontrar uma coluna de município no arquivo `dados_municipios.csv`."
            )
            st.write("Colunas disponíveis:", list(df_municipios.columns))
        else:
            municipios = sorted(df_municipios[municipio_col].dropna().astype(str).unique())
            municipio_selecionado = st.selectbox(
                "Selecione um município:",
                municipios,
                index=municipios.index("DIVINÓPOLIS") if "DIVINÓPOLIS" in municipios else 0,
            )

            df_filtrado = df_municipios[
                df_municipios[municipio_col].astype(str).str.upper()
                == municipio_selecionado.upper()
            ]

            col1, col2, col3 = st.columns(3)
            col1.metric("Município selecionado", municipio_selecionado)
            col2.metric("Registros encontrados", len(df_filtrado))

            focos_col = find_column(
                df_filtrado,
                ["Numero_Focos", "Número de Focos", "Numero Focos", "Focos", "focos"],
            )

            if focos_col and not df_filtrado.empty:
                total_focos = pd.to_numeric(df_filtrado[focos_col], errors="coerce").sum()
                col3.metric("Total de focos", format_number_br(total_focos))
            else:
                col3.metric("Total de focos", "N/D")

            st.write("Dados filtrados do município:")
            st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

            st.markdown("---")
            st.subheader("Visualizações do município")
            st.write(
                "Quando existirem imagens específicas para o município selecionado, elas serão exibidas abaixo."
            )

            municipio_arquivo = municipio_selecionado.lower()

            possible_images = [
                (
                    f"assets/graficosMaioresMunicipios/taxa_variacao_anual_{municipio_arquivo}.png",
                    "Taxa de variação anual do município",
                ),
                (
                    f"assets/graficosMaioresMunicipios/focos_mes_{municipio_arquivo}.png",
                    "Focos por mês no município",
                ),
                (
                    f"assets/graficosMaioresMunicipios/mapa_print_{municipio_arquivo}.png",
                    "Mapa do município",
                ),
            ]

            for image_path, caption in possible_images:
                show_image(image_path, caption)
