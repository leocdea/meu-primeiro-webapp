import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página para um layout mais amplo e título
st.set_page_config(layout="wide", page_title="Dashboard de Formações")

# --- FUNÇÕES AUXILIARES ---
@st.cache_data
def carregar_dados():
    """Carrega e pré-processa os dados do CSV."""
    try:
        df = pd.read_csv('base de dados/Compilado_Formações_2024-copy.csv', sep=';')
        
        # Colunas numéricas que precisam de tratamento
        numeric_cols = [
            'Total_Inscrições_Cursos', 'Total_de_Aprovações_em_Cursos_ComNota',
            'Total_de_Reprovações_em_Cursos_ComNota', 'Total_Inscrições_Cursos_SemNota',
            'Total_Inscrições_Cursos_ComNota'
        ]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        # Garante que as colunas de cursos são strings para evitar erros
        df['Nomes_Todos_Cursos_Inscritos'] = df['Nomes_Todos_Cursos_Inscritos'].astype(str).fillna('')
        df['Nomes_Breves_Todos_Cursos_Inscritos'] = df['Nomes_Breves_Todos_Cursos_Inscritos'].astype(str).fillna('')
        
        return df
    except FileNotFoundError:
        st.error("Arquivo 'Compilado_Formações_2024-copy.csv' não encontrado. Verifique se o arquivo está na pasta correta.")
        return None

@st.cache_data
def extrair_nomes_unicos(_df, column_name):
    """Extrai uma lista de nomes únicos de uma coluna do DataFrame."""
    nomes = _df[column_name].dropna().str.split(', ').explode()
    return sorted(nomes[nomes.str.strip() != 'nan'].str.strip().unique())

# --- CARREGAMENTO DOS DADOS ---
df_original = carregar_dados()

if df_original is not None:
    # Extrai listas de nomes únicos para os filtros
    cursos_unicos = extrair_nomes_unicos(df_original, 'Nomes_Todos_Cursos_Inscritos')
    nomes_breves_unicos = extrair_nomes_unicos(df_original, 'Nomes_Breves_Todos_Cursos_Inscritos')

    # --- BARRA LATERAL DE FILTROS ---
    st.sidebar.header('🔍 Filtros Avançados')

    sre_selecionada = st.sidebar.multiselect(
        'SRE:', options=sorted(df_original['SRE'].unique()),
        default=sorted(df_original['SRE'].unique())
    )

    municipios_disponiveis = df_original[df_original['SRE'].isin(sre_selecionada)]['Municipio'].unique()
    municipio_selecionado = st.sidebar.multiselect(
        'Município:', options=sorted(municipios_disponiveis),
        default=sorted(municipios_disponiveis)
    )
    
    escolaridade_selecionada = st.sidebar.multiselect(
        'Escolaridade:', options=sorted(df_original['Escolaridade'].dropna().unique()),
        default=sorted(df_original['Escolaridade'].dropna().unique())
    )

    cargos_disponiveis = df_original['Cargo'].dropna().unique()
    cargo_selecionado = st.sidebar.multiselect(
        'Cargo:', options=sorted(cargos_disponiveis),
        default=sorted(cargos_disponiveis)
    )

    st.sidebar.markdown('---')
    st.sidebar.subheader('Filtros por Curso')
    
    curso_selecionado = st.sidebar.multiselect(
        'Nome Completo do Curso:', options=cursos_unicos
    )
    
    nome_breve_selecionado = st.sidebar.multiselect(
        'Nome Breve do Curso:', options=nomes_breves_unicos
    )

    # --- APLICAÇÃO DOS FILTROS ---
    df_filtrado = df_original[
        df_original['SRE'].isin(sre_selecionada) &
        df_original['Municipio'].isin(municipio_selecionado) &
        df_original['Escolaridade'].isin(escolaridade_selecionada) &
        df_original['Cargo'].isin(cargo_selecionado)
    ]

    if curso_selecionado:
        df_filtrado = df_filtrado[df_filtrado['Nomes_Todos_Cursos_Inscritos'].apply(
            lambda x: any(curso in x for curso in curso_selecionado)
        )]
        
    if nome_breve_selecionado:
        df_filtrado = df_filtrado[df_filtrado['Nomes_Breves_Todos_Cursos_Inscritos'].apply(
            lambda x: any(nome_breve in x for nome_breve in nome_breve_selecionado)
        )]

    # --- TÍTULO DO DASHBOARD ---
    st.title('🚀 Dashboard Analítico de Formações 2024')
    st.markdown("Utilize os filtros na barra lateral para explorar os dados de forma interativa.")
    st.markdown("---")
    
    if df_filtrado.empty:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
    else:
        # --- MÉTRICAS PRINCIPAIS ---
        total_inscricoes = df_filtrado['Total_Inscrições_Cursos'].sum()
        total_participantes = df_filtrado['CPF'].nunique()
        total_aprovacoes = df_filtrado['Total_de_Aprovações_em_Cursos_ComNota'].sum()
        total_reprovacoes = df_filtrado['Total_de_Reprovações_em_Cursos_ComNota'].sum()
        
        total_avaliacoes = total_aprovacoes + total_reprovacoes
        taxa_aprovacao = (total_aprovacoes / total_avaliacoes * 100) if total_avaliacoes > 0 else 0

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Inscrições", f"{int(total_inscricoes)}")
        col2.metric("Participantes Únicos", f"{int(total_participantes)}")
        col3.metric("Total de Aprovações", f"{int(total_aprovacoes)}")
        col4.metric("Taxa de Aprovação", f"{taxa_aprovacao:.2f}%")
        st.markdown("---")

        # --- ABAS DE NAVEGAÇÃO ---
        tab1, tab2, tab3 = st.tabs(["📊 Visão Geral", "🎓 Análise de Cursos", "👥 Análise de Participantes"])

        with tab1:
            st.header("Desempenho Geral")
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.subheader("Aprovações vs. Reprovações")
                fig_aprovacao = go.Figure(go.Pie(
                    labels=['Aprovados', 'Reprovados'],
                    values=[total_aprovacoes, total_reprovacoes],
                    hole=.5,
                    marker_colors=['#008000', '#FF0000']
                ))
                fig_aprovacao.update_layout(legend_title_text='Resultado')
                st.plotly_chart(fig_aprovacao, use_container_width=True)

            with col2:
                st.subheader("Taxa de Aprovação por SRE")
                aprovacoes_sre = df_filtrado.groupby('SRE').agg(
                    Aprovados=('Total_de_Aprovações_em_Cursos_ComNota', 'sum'),
                    Reprovados=('Total_de_Reprovações_em_Cursos_ComNota', 'sum')
                ).reset_index()
                aprovacoes_sre['Total'] = aprovacoes_sre['Aprovados'] + aprovacoes_sre['Reprovados']
                aprovacoes_sre['Taxa_Aprovacao'] = aprovacoes_sre.apply(
                    lambda row: (row['Aprovados'] / row['Total'] * 100) if row['Total'] > 0 else 0, axis=1
                )
                
                fig_sre = px.bar(
                    aprovacoes_sre.sort_values('Taxa_Aprovacao', ascending=False),
                    x='SRE', y='Taxa_Aprovacao',
                    text=aprovacoes_sre['Taxa_Aprovacao'].apply(lambda x: f'{x:.1f}%'),
                    title='Percentual de Aprovação por SRE'
                )
                st.plotly_chart(fig_sre, use_container_width=True)

        with tab2:
            st.header("Análise Detalhada de Cursos")
            cursos_filtrados = df_filtrado['Nomes_Todos_Cursos_Inscritos'].str.split(', ').explode()
            contagem_cursos = cursos_filtrados.value_counts().nlargest(15).reset_index()
            contagem_cursos.columns = ['Curso', 'Número de Inscrições']
            
            fig_cursos = px.bar(
                contagem_cursos.sort_values('Número de Inscrições', ascending=True),
                x='Número de Inscrições', y='Curso', orientation='h',
                title='Top 15 Cursos Mais Procurados', text='Número de Inscrições'
            )
            st.plotly_chart(fig_cursos, use_container_width=True)

        with tab3:
            st.header("Análise de Engajamento dos Participantes")
            st.subheader("Top 20 Participantes por Número de Inscrições (Top Alunos)")
            top_alunos = df_filtrado.groupby(['Nome_Completo', 'Municipio', 'SRE'])['Total_Inscrições_Cursos'].sum().nlargest(20).reset_index()
            st.dataframe(top_alunos, use_container_width=True)
            
    # --- DADOS BRUTOS (OPCIONAL) ---
    with st.expander("Ver dados brutos filtrados"):
        st.dataframe(df_filtrado)