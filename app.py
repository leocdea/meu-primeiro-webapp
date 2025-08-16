# Importa a biblioteca streamlit com o apelido 'st'
import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
# st.set_page_config define as configurações iniciais da página,
# como o título que aparece na aba do navegador e o layout.
st.set_page_config(page_title="Meu Primeiro Web App", layout="wide")

# --- CABEÇALHO / SEÇÃO PRINCIPAL ---
# st.container() cria um bloco para agrupar elementos
with st.container():
    st.subheader("Instituto Federal do Espírito Santo - Campus Serra")
    st.subheader("Pós-Graduação em Mineração de Dados Educacionais - SEDU")
    st.subheader("Disciplina Ferramentas e Soluções em Nuvem")
    st.subheader("Professor Maxwell Eduardo Monteiro")
    st.subheader("Olá, seja bem-vindo(a)!")
    # 1) SEU NOME
    st.title("Web App do Leonardo Cruz de Andrade")
    
    # 2) TEMA QUE PRETENDE TRATAR
    st.header("Tema: Análise da relação entre Infraestrutura e Desempenho Educacional - Anos Iniciais da Rede Municipal do Espírito Santo em 2023")
    st.write(
        "O objetivo deste projeto é analisar a relação da infraestutura escolar com o desempenho educacional no ano de 2023 das escolas públicas municipais do Estado do Espírito Santo com foco anos inciais (fundamental I) para extrair insights sobre oportunidades de melhorias nas políticas públicas."
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
        - **Ideb (Índice de Desenvolvimento da Educação Básica):** Base de dados "divulgacao_anos_iniciais_municipios_2023", disponibilizada pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep). Contém os resultados do principal indicador de qualidade da educação básica no Brasil, permitindo a análise do desempenho das escolas e municípios para os anos iniciais do ensino fundamental.
        - **IBGE (Instituto Brasileiro de Geografia e Estatística):** Arquivos da base "BR_Municipios_2022", que oferecem dados geoespaciais e informações estatísticas sobre os municípios brasileiros. Estes dados são essenciais para a criação de mapas, análises territoriais e para a contextualização socioeconômica das localidades estudadas.
        - **Censo Escolar: "Microdados_ed_basica_2023"**, levantamento detalhado realizado pelo Inep. Esta base de dados abrange informações sobre escolas, matrículas, docentes, turmas e infraestrutura da educação básica no Brasil, sendo fundamental para análises aprofundadas sobre o sistema educacional.
        
        """
    )

