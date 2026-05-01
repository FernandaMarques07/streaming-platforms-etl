# 🎬 Streaming Data ETL Project / Projeto de ETL com Dados de Streaming

---

## 📌 Overview / Visão Geral

**EN:**
This project was developed as part of a practical challenge focused on understanding the **ETL process (Extract, Transform, Load)** using Python. The goal was to simulate a real-world data pipeline and demonstrate the ability to collect, clean, transform, and visualize data.

**PT-BR:**
Este projeto foi desenvolvido como parte de um desafio prático com foco na compreensão do processo de **ETL (Extração, Transformação e Carregamento)** utilizando Python. O objetivo foi simular um pipeline de dados real e demonstrar a capacidade de coletar, tratar, transformar e visualizar dados.

---

## 📊 Dataset

Dataset disponível no Kaggle:
https://www.kaggle.com/datasets/meruvakodandasuraj/streaming-content-catalog-netflix-prime-disney/data

**EN:**
The dataset contains over 15,000 titles from major streaming platforms (Netflix, Prime Video, Disney+, etc.), including ratings, genres, watch time, and more.

**PT-BR:**
O dataset contém mais de 15.000 títulos de plataformas de streaming (Netflix, Prime Video, Disney+, etc.), incluindo avaliações, gêneros, tempo assistido e outras informações.

---

## ⚙️ Challenge Requirements / O que a Atividade Pedia

### EN:

The challenge focused on implementing the ETL pipeline:

* **Extract:** Load data from an external source (API or CSV)
* **Transform:** Clean, process, and enrich the data
* **Load:** Save the processed data for analysis

### PT-BR:

A atividade teve como foco aplicar o pipeline de ETL:

* **Extração:** Carregar dados de uma fonte externa (API ou CSV)
* **Transformação:** Limpar, tratar e enriquecer os dados
* **Carregamento:** Salvar os dados processados para análise

---

## 🧠 What I Implemented / O que Eu Fiz

### ✔ Extract / Extração

* **EN:** Loaded two CSV files using pandas
* **PT-BR:** Carreguei dois arquivos CSV utilizando pandas

Arquivos:

* `streaming_catalog.csv`
* `genre_summary.csv`

---

### ✔ Transform / Transformação

**EN:**

* Removed duplicates
* Converted data types (ratings and year)
* Removed null values
* Selected relevant columns
* Created new features:

  * **Engagement** (based on watch time)
  * **Score** (IMDb + Rotten Tomatoes weighted)
* Created `release_period` classification
* Merged datasets by genre

**PT-BR:**

* Removi duplicatas
* Converti tipos de dados (avaliações e ano)
* Removi valores nulos
* Selecionei colunas relevantes
* Criei novas métricas:

  * **Engagement** (baseado em horas assistidas)
  * **Score** (combinação ponderada de IMDb e Rotten Tomatoes)
* Criei a classificação `release_period`
* Realizei o merge dos datasets por gênero

---

### ✔ Load / Carregamento

**EN:**
Saved the processed dataset as `processed_data.csv`.

**PT-BR:**
Salvei o dataset tratado como `processed_data.csv`.

---

## 📈 Power BI Visualization / Visualização no Power BI

**EN:**
After processing the data, I created a dashboard in Power BI with:

* Platform comparison (engagement)
* Top genres by platform
* Score analysis (content quality)
* Release period trends
* Interactive filters

**PT-BR:**
Após o processamento dos dados, desenvolvi um dashboard no Power BI com:

* Comparação entre plataformas (engajamento)
* Gêneros mais populares por plataforma
* Análise de score (qualidade do conteúdo)
* Tendências por período de lançamento
* Filtros interativos

---

## 🚀 Key Learnings / Aprendizados

**EN:**

* Practical understanding of ETL pipeline
* Data cleaning and feature engineering
* Working with real datasets
* Better data visualization practices

**PT-BR:**

* Compreensão prática do pipeline ETL
* Limpeza e transformação de dados
* Trabalho com datasets reais
* Melhoria na criação de visualizações

---

## 📁 Technologies / Tecnologias

* Python (pandas)
* Power BI
* Kaggle (datasets)

---

## 💡 Final Note / Observação Final

**EN:**
This project focuses on the ETL process and simulates a real data workflow, demonstrating practical data analysis skills.

**PT-BR:**
Este projeto tem como foco o processo de ETL e simula um fluxo de dados real, demonstrando habilidades práticas em análise de dados.
