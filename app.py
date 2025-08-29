# Importa a biblioteca streamlit com o apelido 'st'
import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
# st.set_page_config define as configurações iniciais da página,
# como o título que aparece na aba do navegador e o layout.
st.set_page_config(page_title="Análise Educacional ES", layout="wide")

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
        "O objetivo deste projeto é analisar a relação da infraestutura escolar com o desempenho educacional no ano de 2023 das escolas públicas municipais do Estado do Espírito Santo com foco nos anos inciais (Fundamental I) para extrair insights sobre oportunidades de melhorias nas políticas públicas."
    )
    st.write("---") # Adiciona uma linha divisória

# --- NAVEGAÇÃO NA BARRA LATERAL ---
# Usamos st.sidebar para criar uma barra lateral de navegação
st.sidebar.header("Navegue pelas Seções")
secao = st.sidebar.selectbox(
    'Selecione a página:',
    ['Página Inicial', 'Análise do IDEB 2023', 'Análise do Censo 2023', 'Análise dos Insights']
)

# --- SEÇÕES DO APP (COM LAYOUT MELHORADO) ---

# Lógica para exibir conteúdo baseado na seleção da sidebar
if secao == 'Página Inicial':
    with st.container():
        st.header("Visão Geral do Projeto")
        # st.columns cria colunas para organizar o conteúdo lado a lado
        col1, col2 = st.columns((2, 1)) # A primeira coluna será 2x maior que a segunda

        with col1:
            st.write("Nesta seção, apresentaremos os objetivos do projeto, a metodologia utilizada e um resumo dos principais resultados que serão explorados nas outras seções.")
            st.markdown(
                """
                - **Motivação:** Entender como a infraestrutura escolar impacta o desempenho dos alunos.
                - **Metodologia:** Análise exploratória de dados combinando Censo Escolar e IDEB.
                - **Tecnologias:** Python, Pandas, Streamlit.
                """
            )
        with col2:
            st.info("Métricas Principais (Exemplos)")
            # st.metric é ideal para exibir KPIs (Key Performance Indicators)
            st.metric(label="Nº de Municípios Analisados", value="78")
            st.metric(label="Período de Análise", value="2023")


elif secao == 'Análise do IDEB 2023':
    with st.container():
        st.header("Análise do IDEB 2023")
        st.write("Aqui vamos explorar os dados do IDEB 2023 segmentados pelos munícipios do ES. Gráficos serão utilizados para visualizar esses dados.")
        
        # Dividindo a seção em colunas para melhor visualização
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Placeholder para Mapa")
            st.image("https://placehold.co/600x400/0072B2/FFFFFF?text=Mapa+IDEB+por+Munic%C3%ADpio", caption="Futuro mapa coroplético do IDEB 2023")
        
        with col2:
            st.subheader("Placeholder para Gráfico de Barras")
            st.image("https://placehold.co/600x400/D55E00/FFFFFF?text=Top+10+Munic%C3%ADpios", caption="Futuro ranking dos municípios por nota do IDEB")


elif secao == 'Análise do Censo 2023':
    with st.container():
        st.header("Análise do Censo 2023")
        st.write("Aqui vamos explorar os dados do Censo 2023 segmentados pelos munícipios do ES. Gráficos serão utilizados para visualizar esses dados de infraestrutura.")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Internet nas Escolas")
            st.image("https://placehold.co/400x300/009E73/FFFFFF?text=Gr%C3%A1fico+de+Pizza", caption="Percentual de escolas com acesso à internet.")
        with col2:
            st.subheader("Laboratórios")
            st.image("https://placehold.co/400x300/F0E442/000000?text=Gr%C3%A1fico+de+Pizza", caption="Percentual de escolas com laboratório de ciências/informática.")
        with col3:
            st.subheader("Acessibilidade")
            st.image("https://placehold.co/400x300/CC79A7/FFFFFF?text=Gr%C3%A1fico+de+Pizza", caption="Percentual de escolas com rampas de acesso.")
            

elif secao == 'Análise dos Insights':
    with st.container():
        st.header("Análise dos Insights")
        st.write("Aqui vamos explorar os insights a partir da junção e análise dos dados do IDEB 2023 e do Censo 2023. O objetivo é encontrar correlações.")
        st.subheader("Placeholder para Gráfico de Dispersão (Scatter Plot)")
        st.image("https://placehold.co/800x500/56B4E9/FFFFFF?text=IDEB+vs+Infraestrutura", caption="Futuro gráfico de dispersão para visualizar a correlação entre a nota do IDEB e um indicador de infraestrutura.")


st.write("---")

# --- BASES DE DADOS (COM LAYOUT MELHORADO) ---
with st.container():
    st.header("Bases de Dados Utilizadas (Planejamento)")
    st.write(
        "Para este projeto, pretendo utilizar as seguintes fontes de dados (ou similares). Clique para expandir e ver os detalhes:"
    )
    
    # st.expander cria uma seção "sanfona" que pode ser expandida ou recolhida
    with st.expander("Ideb (Índice de Desenvolvimento da Educação Básica)"):
        st.write(
            """
            - **Fonte:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep).
            - **Base:** `divulgacao_anos_iniciais_municipios_2023`.
            - **Descrição:** Contém os resultados do principal indicador de qualidade da educação básica no Brasil, permitindo a análise do desempenho das escolas e municípios para os anos iniciais do ensino fundamental.
            """
        )
    
    with st.expander("IBGE (Instituto Brasileiro de Geografia e Estatística)"):
        st.write(
            """
            - **Fonte:** Instituto Brasileiro de Geografia e Estatística (IBGE).
            - **Base:** `BR_Municipios_2022`.
            - **Descrição:** Oferece dados geoespaciais e informações estatísticas sobre os municípios brasileiros. Estes dados são essenciais para a criação de mapas, análises territoriais e para a contextualização socioeconômica das localidades estudadas.
            """
        )

    with st.expander("Censo Escolar"):
        st.write(
            """
            - **Fonte:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep).
            - **Base:** `Microdados_ed_basica_2023`.
            - **Descrição:** Levantamento detalhado que abrange informações sobre escolas, matrículas, docentes, turmas e infraestrutura da educação básica no Brasil, sendo fundamental para análises aprofundadas sobre o sistema educacional.
            """
        )
