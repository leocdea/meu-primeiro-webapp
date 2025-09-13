import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Título do aplicativo
st.set_page_config(layout="wide") # Deixa a página mais larga para melhor visualização
st.title("📊 Análise de Dados de Custos de Seguro")

# Carregar dataset com cache para otimização
@st.cache_data
def carregar_dados(name):
    """Função para carregar os dados de um arquivo CSV."""
    return pd.read_csv(name)

df = carregar_dados("insurance.csv")

# --- Barra Lateral com Filtros ---
st.sidebar.header("🔧 Filtros")

# Filtro por sexo (multiselect)
sexo = st.sidebar.multiselect(
    "Sexo",
    options=df['sex'].unique(),
    default=df['sex'].unique()
)

# Filtro por fumante (radio button para melhor usabilidade)
fumante = st.sidebar.radio(
    "É fumante?",
    options=df['smoker'].unique(),
    index=0 # Define 'yes' ou o primeiro item como padrão
)

# Aplicar filtros no dataframe
df_filtrado = df[(df['sex'].isin(sexo)) & (df['smoker'] == fumante)]

# --- Corpo Principal da Aplicação ---

st.subheader("🔍 Visualização da Tabela de Dados")
st.dataframe(df_filtrado)

# Adiciona uma verificação para evitar erros com dataframe vazio
if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
else:
    # Estatísticas Descritivas
    st.subheader("📈 Estatísticas Descritivas")
    st.write(df_filtrado.describe())

    # --- Visualizações de Dados ---
    st.subheader("🎨 Gráficos e Visualizações")

    col1, col2 = st.columns(2) # Divide a área de gráficos em duas colunas

    with col1:
        # Gráfico 1: Dispersão (seu código original, que já era bom)
        st.subheader("💸 Idade vs. Custos")
        st.scatter_chart(
            df_filtrado,
            x="age",
            y="charges",
            color="bmi", # Cor baseada no IMC
            size="children", # Tamanho baseado no número de filhos
        )

        # Gráfico 2 (MELHORADO): Boxplot Custo x Sexo
        st.subheader("📦 Distribuição de Custos por Sexo")
        fig, ax = plt.subplots()
        sns.boxplot(data=df_filtrado, x="sex", y="charges", ax=ax)
        st.pyplot(fig)

    with col2:
        # Gráfico 3 (MELHORADO): Barras Custo médio x Região
        st.subheader("🌍 Custo Médio por Região")
        custo_medio_regiao = df_filtrado.groupby('region')['charges'].mean().sort_values()
        st.bar_chart(custo_medio_regiao)

        # Gráfico 4 (BÔNUS): Histograma para ver a distribuição do IMC
        st.subheader("🏃 Distribuição do IMC (Índice de Massa Corporal)")
        fig, ax = plt.subplots()
        sns.histplot(df_filtrado['bmi'], kde=True, ax=ax)
        st.pyplot(fig)