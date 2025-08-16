# Importa a biblioteca streamlit com o apelido 'st'
import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
# st.set_page_config define as configurações iniciais da página,
# como o título que aparece na aba do navegador e o layout.
st.set_page_config(page_title="Meu Primeiro Web App", layout="wide")

# --- CABEÇALHO / SEÇÃO PRINCIPAL ---
# st.container() cria um bloco para agrupar elementos
with st.container():
    st.subheader("Olá, seja bem-vindo(a)!")
    # 1) SEU NOME
    st.title("Web App do [Seu Nome Aqui]")
    
    # 2) TEMA QUE PRETENDE TRATAR
    st.header("Tema: Análise de Vendas de E-commerce")
    st.write(
        "Este é o meu primeiro Web App usando Streamlit! "
        "O objetivo deste projeto é analisar dados de vendas de um e-commerce fictício "
        "para extrair insights sobre produtos mais vendidos, tendências sazonais e perfil de clientes."
    )
    st.write("---") # Adiciona uma linha divisória

# --- SEÇÕES DO APP (DIVISÃO) ---
# 3) A DIVISÃO DAS SEÇÕES DO APP
# Usamos st.sidebar para criar uma barra lateral de navegação
st.sidebar.header("Navegue pelas Seções")
secao = st.sidebar.selectbox(
    'Selecione a página:',
    ['Página Inicial', 'Análise de Produtos', 'Análise Geográfica', 'Previsão de Vendas']
)

# Lógica para exibir conteúdo baseado na seleção da sidebar
if secao == 'Página Inicial':
    st.header("Visão Geral do Projeto")
    st.write("Nesta seção, apresentaremos os objetivos do projeto, a metodologia utilizada e um resumo dos principais resultados que serão explorados nas outras seções.")
    # No futuro, aqui você poderia adicionar KPIs gerais como:
    # - Total de Vendas
    # - Número de Clientes
    # - Ticket Médio

elif secao == 'Análise de Produtos':
    st.header("Análise de Produtos")
    st.write("Aqui vamos explorar quais são os produtos mais vendidos, as categorias mais lucrativas e a relação entre diferentes produtos. Gráficos de barras e de pizza serão utilizados para visualizar esses dados.")
    # Espaço reservado para futuros gráficos e tabelas
    st.text("Em breve: Gráfico de produtos mais vendidos.")

elif secao == 'Análise Geográfica':
    st.header("Análise Geográfica")
    st.write("Nesta seção, o foco será a análise de vendas por região. Vamos visualizar em um mapa de onde vêm a maioria dos pedidos e qual o desempenho de vendas por estado ou cidade.")
    # Espaço reservado para futuros mapas
    st.text("Em breve: Mapa de calor de vendas por estado.")

elif secao == 'Previsão de Vendas':
    st.header("Previsão de Vendas")
    st.write("Utilizando modelos de séries temporais, esta seção apresentará uma previsão de vendas para os próximos meses, ajudando no planejamento de estoque e estratégias de marketing.")
    # Espaço reservado para futuros gráficos de previsão
    st.text("Em breve: Gráfico de previsão de vendas futuras.")

st.write("---")

# --- BASES DE DADOS ---
# 4) BASES DE DADOS QUE IMAGINA USAR
with st.container():
    st.header("Bases de Dados Utilizadas (Planejamento)")
    st.write(
        "Para este projeto, pretendo utilizar as seguintes fontes de dados (ou similares):"
    )
    st.markdown(
        """
        - **Olist Dataset:** Um conjunto de dados público e anonimizado sobre e-commerce disponível no Kaggle, contendo informações de pedidos, produtos, clientes e avaliações.
        - **Dados de Geolocalização:** Arquivos com informações de CEPs brasileiros para a criação dos mapas.
        - **Dados Internos Fictícios:** Criação de uma base de dados simulada para complementar as análises.
        """
    )

