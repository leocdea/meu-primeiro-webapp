import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os

# Configuração da página para um layout mais amplo e título
st.set_page_config(layout="wide", page_title="Dashboard de Formações")

# --- FUNÇÕES AUXILIARES ---
@st.cache_data
def carregar_dados():
    """Carrega e pré-processa os dados do CSV de forma robusta."""
    try:
        NOME_ARQUIVO = 'Compilado_Formações_2024-copy.csv'
        caminho_script = os.path.dirname(__file__)
        caminho_arquivo = os.path.join(caminho_script, NOME_ARQUIVO)
        df = pd.read_csv(caminho_arquivo, sep=';')
        
        numeric_cols = [
            'Total_Inscrições_Cursos', 'Total_de_Aprovações_em_Cursos_ComNota',
            'Total_de_Reprovações_em_Cursos_ComNota', 'Total_Inscrições_Cursos_SemNota',
            'Total_Inscrições_Cursos_ComNota'
        ]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        df['Nomes_Todos_Cursos_Inscritos'] = df['Nomes_Todos_Cursos_Inscritos'].astype(str).fillna('')
        df['Nomes_Breves_Todos_Cursos_Inscritos'] = df['Nomes_Breves_Todos_Cursos_Inscritos'].astype(str).fillna('')
        
        return df
    except FileNotFoundError:
        st.error(f"Arquivo '{NOME_ARQUIVO}' não encontrado. Verifique se o nome do arquivo no código é exatamente igual ao nome no GitHub.")
        return None

@st.cache_data
def extrair_nomes_unicos(_df, column_name):
    """Extrai uma lista de nomes únicos de uma coluna do DataFrame."""
    nomes = _df[column_name].dropna().str.split(', ').explode()
    return sorted(nomes[nomes.str.strip() != 'nan'].str.strip().unique())

# --- CARREGAMENTO DOS DADOS ---
df_original = carregar_dados()

if df_original is not None:
    cursos_unicos = extrair_nomes_unicos(df_original, 'Nomes_Todos_Cursos_Inscritos')
    nomes_breves_unicos = extrair_nomes_unicos(df_original, 'Nomes_Breves_Todos_Cursos_Inscritos')

    # --- BARRA LATERAL DE FILTROS ---
    st.sidebar.header('🔍 Filtros Avançados')

    # --- INÍCIO DA CORREÇÃO ---
    # Adicionado .dropna() para remover valores nulos antes de criar as opções dos filtros.
    
    sre_options = sorted(df_original['SRE'].dropna().unique())
    sre_selecionada = st.sidebar.multiselect('SRE:', options=sre_options, default=sre_options)

    municipios_disponiveis = df_original[df_original['SRE'].isin(sre_selecionada)]['Municipio'].dropna().unique()
    municipio_selecionado = st.sidebar.multiselect(
        'Município:', options=sorted(municipios_disponiveis), default=sorted(municipios_disponiveis)
    )
    
    escolaridade_options = sorted(df_original['Escolaridade