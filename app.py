import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Streaming Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregamento de dados
@st.cache_data
def load_data() -> pd.DataFrame:
    try:
        return pd.read_csv("data/processed/processed_data.csv")
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo de dados: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("Nenhum dado encontrado para exibição.")
    st.stop()

# Filtros na barra lateral
st.sidebar.header("Filtros")

platforms = sorted(df["platform"].dropna().unique()) if "platform" in df.columns else []
genres = sorted(df["primary_genre"].dropna().unique()) if "primary_genre" in df.columns else []
types = sorted(df["type"].dropna().unique()) if "type" in df.columns else []

selected_platforms = st.sidebar.multiselect("Plataforma", platforms, default=platforms)
selected_genres = st.sidebar.multiselect("Gênero", genres, default=genres)
selected_types = st.sidebar.multiselect("Tipo", types, default=types)

filtered = df[
    (df["platform"].isin(selected_platforms)) &
    (df["primary_genre"].isin(selected_genres)) &
    (df["type"].isin(selected_types))
]

st.sidebar.divider()
st.sidebar.caption(f"Exibindo **{len(filtered)}** de **{len(df)}** títulos.")

# Cabecalho principal
st.title("Dashboard de Streaming")
st.markdown("Visão consolidada do catálogo, engajamento e performance das plataformas.")
st.divider()

if filtered.empty:
    st.warning("Nenhum registro encontrado para os filtros selecionados.")
    st.stop()

# Metricas
col1, col2, col3, col4 = st.columns(4)

total_titles = len(filtered)
avg_imdb = filtered["imdb_rating"].mean() if "imdb_rating" in filtered.columns else 0
total_hours = filtered["hours_watched_million"].sum() if "hours_watched_million" in filtered.columns else 0
avg_score = filtered["score"].mean() if "score" in filtered.columns else 0

col1.metric("Total de Títulos", f"{total_titles:,}")
col2.metric("IMDb Médio", f"{avg_imdb:.2f}" if pd.notna(avg_imdb) else "N/A")
col3.metric("Horas Assistidas", f"{total_hours:,.1f} Mi")
col4.metric("Score Médio", f"{avg_score:.2f}" if pd.notna(avg_score) else "N/A")

st.divider()

# Conteudo em abas
tab_overview, tab_summary, tab_catalog = st.tabs([
    "Visão Geral & Gráficos",
    "Resumo por Gênero",
    "Catálogo Completo"
])

with tab_overview:
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Títulos por Plataforma")
        st.bar_chart(filtered["platform"].value_counts())

        st.subheader("Score Médio por Plataforma")
        score_platform = filtered.groupby("platform")["score"].mean().sort_values(ascending=False)
        st.bar_chart(score_platform)

    with col_right:
        st.subheader("Títulos por Gênero")
        st.bar_chart(filtered["primary_genre"].value_counts())

        st.subheader("Lançamentos por Ano")
        year_chart = filtered.groupby("release_year").size()
        st.line_chart(year_chart)

with tab_summary:
    st.subheader("Resumo por Gênero")
    
    summary = (
        filtered.groupby("primary_genre")
        .agg(
            total_titulos=("primary_genre", "count"),
            imdb_medio=("imdb_rating", "mean"),
            score_medio=("score", "mean"),
            horas_assistidas_total=("hours_watched_million", "sum")
        )
        .reset_index()
        .round({"imdb_medio": 2, "score_medio": 2, "horas_assistidas_total": 1})
        .rename(columns={
            "primary_genre": "Gênero",
            "total_titulos": "Qtd Títulos",
            "imdb_medio": "IMDb Médio",
            "score_medio": "Score Médio",
            "horas_assistidas_total": "Total Horas (Mi)"
        })
    )
    
    st.dataframe(
        summary, 
        use_container_width=True, 
        hide_index=True
    )

with tab_catalog:
    st.subheader("Explorador do Catálogo")
    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )