import streamlit as st
import os
from src.data_loader import download_sample_data, load_dicom, load_csv_to_dataframe
from src.eda_load_limpeza import load_info_dataset, load_estatistica_bruta, limpar_dados
from src.eda_mineracao import load_histograma

st.set_page_config(page_title="Análise de dados - PISI3", layout="wide")

st.title("Dashboard - Analise Exploratória de Dados (AED) com dataset de imagens radiológicas")
st.markdown("---")

tab_set_dados, tab_eda,  = st.tabs([
    "Configurações de Dados",
    "Análise Exploratória de Dados"
])

with tab_set_dados:
    st.header("Configurações de Dados")
    st.subheader("Carregar csv do Kaggle")
    
    if 'df' not in st.session_state:
        st.session_state.df = None
        st.session_state.df = load_csv_to_dataframe()
        st.success('Dados carregados!')
        
    if st.button("Baixar Amostra do Kaggle"):
        with st.spinner("Acessando API..."):
            download_sample_data()
            st.success("Dados prontos!")

            # Carregar Dados
            if os.path.exists('./data/train.csv'):
                df = download_sample_data(limit=1) # Carrega dataframe
                
                # Carregar Imagens para treino
                path_exemplo = "./data/train/" + os.listdir("./data/train/")[0]
                ds_imagens = load_dicom(path_exemplo)
            
            else:
                st.warning("Aguardando carregamento de dados do Kaggle.")
            
with tab_eda:
    st.header("Análise Exploratória de Dados (EDA)- dataset VinBigData.")
    if 'df' in st.session_state and st.session_state.df is not None:
        df_inicial = st.session_state.df
        st.session_state.df = limpar_dados(df_inicial)
        df = st.session_state.df
            
        st.subheader(" ➔ Apresentação dos Dados")
        with st.expander("Estrutura do Dataset (Tipos e Dados Nulos)"):
            load_info_dataset(df_inicial)
            
        with st.expander("Detalhes Estatísticos"): 
            load_estatistica_bruta(df)
            
        with st.expander("Visualizar as 15 primeiras linhas"):
            st.table(df.tail(15))
            
        st.subheader(" ➔ Visualização Gráfica dos Dados")
        with st.expander("Distribuição de Frequência das Patologias"):
            load_histograma(df)
        
        with st.expander("LOADING..."):    
            st.write('loading')
    else:
        st.warning("⚠️ O DataFrame ainda não foi carregado. Vá até a barra lateral ou aba de carregamento.")