import streamlit as st

st.info("Iniciando o teste...")

# Criando as colunas. Uma variável para cada coluna.
col1, col2, col3 = st.columns(3)

# ---- Bloco da COLUNA 1 ----
with col1:
    st.header("Bloco 1")
    st.success("Este texto está na col1.")

# ---- Bloco da COLUNA 2 ----
with col2:
    st.header("Bloco 2")
    st.warning("Este texto está na col2.")

# ---- Bloco da COLUNA 3 ----
with col3:
    st.header("Bloco 3")
    st.error("Este texto está na col3.")

st.info("... Fim do teste.")
