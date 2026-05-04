import streamlit as st

st.set_page_config(page_title="Análise de dados - PISI3", layout="wide")

st.title("Dashboard - Analise Exploratória de Dados (AED) com dataset tabular")
st.markdown("---")

tab_config_dados, tab_eda,  = st.tabs([
    "Configurações de Dados",
    "Análise Exploratória de Dados"
])

with tab_config_dados:
    st.header("Configurações de Dados")
    st.subheader("Carregar csv do Kaggle")
            
with tab_eda:
    st.header("Análise Exploratória de Dados (EDA)- dataset.")
