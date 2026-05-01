import pandas as pd

# extrair dados

catalog = pd.read_csv("data/raw/streaming_catalog.csv")
genre = pd.read_csv("data/raw/genre_summary.csv")

# transformar dados

# remover duplicados
catalog = catalog.drop_duplicates()

# converter tipos 
catalog["release_year"] = pd.to_numeric(catalog["release_year"], errors="coerce")
catalog["imdb_rating"] = pd.to_numeric(catalog["imdb_rating"], errors="coerce")
catalog["rotten_tomatoes_score"] = pd.to_numeric(catalog["rotten_tomatoes_score"], errors="coerce")

# remover nulos 
catalog = catalog.dropna(subset=["imdb_rating", "rotten_tomatoes_score", "release_year"])

# selecionar colunas
catalog = catalog[[
    "show_id", "title", "type", "platform",
    "primary_genre", "imdb_rating",
    "rotten_tomatoes_score",
    "duration_minutes",
    "release_year",
    "hours_watched_million"
]]

# métricas
catalog["engagement"] = catalog["hours_watched_million"]

catalog["score"] = (
    catalog["imdb_rating"] * 0.6 +
    (catalog["rotten_tomatoes_score"] / 10) * 0.4
).round(2)

# classificação de período 
catalog["release_period"] = pd.cut(
    catalog["release_year"],
    bins=[1980, 2005, 2015, 2030],
    labels=["Older", "Mid", "Recent"]
)

# merge com dados de gênero
df = catalog.merge(
    genre,
    on="primary_genre",
    how="left"
)

# salvar dados processados
df.to_csv("data/processed/processed_data.csv", index=False)