import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.load_dataset import load_csv_to_dataframe, load_info_dataset, load_statistics_summary
from src.generate_plots import plot_diagnosis_distribution, plot_feature_distribution, plot_outlier_boxplot

st.set_page_config(page_title="Análise de dados - PISI3", layout="wide")

st.title("Dashboard - Analise Exploratória de Dados (AED) com dataset tabular")
st.markdown("---")

tab_carregar_dados, tab_analise,  = st.tabs([
    "Carregamento dos Dados",
    "Análise Exploratória de Dados"
])

st.session_state.df = None
with tab_carregar_dados:
    
    with st.expander("Configurações do Dataset", expanded=True):
        st.write("Dados carregados de: breast_cancer.csv")
    
        st.session_state.df = load_csv_to_dataframe()
        if(st.session_state.df is not None):
            st.success('Dados carregados com sucesso!')
    
    with st.expander("Informações das colunas, dos Tipos de dados e quantidade dos valores não Nulos e Nulos no dataset"):
        load_info_dataset(st.session_state.df)
    
    with st.expander("Síntese Estatística do dataset"):
        load_statistics_summary(st.session_state.df)
        
with tab_analise:
    st.subheader("Análise Exploratória de Dados (EDA)- dataset.")
    
    if(st.session_state.df is not None):
        df = st.session_state.df
        
        with st.expander("Distribuição da Variável Alvo: Diagnóstico"):
            fig = plot_diagnosis_distribution(df)
            st.pyplot(fig)
            
        with st.expander("Análise Individual de Atributos"):
            colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if 'diagnosis' in colunas_numericas: 
                colunas_numericas.remove('diagnosis')
            
            coluna_selecionada = st.selectbox("Selecione um atributo para analisar:", colunas_numericas)
            col1, col2 = st.columns(2)
            with col1:
                st.pyplot(plot_feature_distribution(df, coluna_selecionada))
                
            with col2:
                st.pyplot(plot_outlier_boxplot(df, coluna_selecionada))
