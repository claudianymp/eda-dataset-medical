import streamlit as st

st.set_page_config(page_title="Análise de dados - PISI3", layout="wide")

st.title("Dashboard - Analise Exploratória de Dados (AED) com dataset tabular")
st.markdown("---")

tab_carregar_dados, tab_analise,  = st.tabs([
    "Carregamento dos Dados",
    "Análise Exploratória de Dados"
])

with tab_carregar_dados:
    st.subheader("Carregar csv do Kaggle")
    st.write("Verificar tipos de dados, valores nulos e estatísticas descritivas básicas")
    
            
with tab_analise:
    st.subheader("Análise Exploratória de Dados (EDA)- dataset.")
