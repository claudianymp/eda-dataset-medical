import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit as st
import pandas as pd
from src.feature_information import get_pca_loadings
from src.load_dataset import load_csv_to_dataframe, load_info_dataset, load_statistics_summary, clean_prepare_data
from src.visualization import plot_diagnosis_distribution, plot_correlation_heatmap, plot_separation_density, plot_comparative_boxplot, plot_tsne
from src.model import CancerMLP

    
st.set_page_config(page_title="Análise de dados - PISI3", layout="wide")

st.title("Dashboard - Analise Exploratória de Dados (EDA) com dataset tabular")
st.markdown("---")

tab_loading_data, tab_ranking_PCA, tab_analysis,tab_train_model  = st.tabs([
    "Carregamento dos Dados",
    "Ranking PCA",
    "Análise Exploratória de Dados",
    "Treinar Rede Neural"
])

st.session_state.df_test = None
st.session_state.df_train = None
st.session_state.df = None
with tab_loading_data:
    with st.expander("Configurações do Dataset", expanded=True):
        st.write("Dados carregados do dataset breast cancer (test e train)")
    
        st.session_state.df_test = load_csv_to_dataframe('./data/test.csv')
        st.session_state.df_train = load_csv_to_dataframe('./data/train.csv')
        st.session_state.df = pd.concat([st.session_state.df_train, st.session_state.df_test], ignore_index=True)
        if(st.session_state.df is not None):
            st.success(f'Dados carregados! Total de linhas: {len(st.session_state.df)}')
    
    with st.expander("Informações das colunas, dos Tipos de dados e quantidade dos valores não Nulos e Nulos no dataset"):
        load_info_dataset(st.session_state.df)
    
    with st.expander("Síntese Estatística do dataset"):
        load_statistics_summary(st.session_state.df)

with tab_ranking_PCA:
    with st.expander("Ranking de Importância dos Componentes (PCA Loadings)"):
        ranking_pca = get_pca_loadings(st.session_state.df)
        st.dataframe(ranking_pca)
        
with tab_analysis:
    st.subheader("Análise Exploratória de Dados (EDA).")
    
    if(st.session_state.df_test is not None):
        df = st.session_state.df_test
        
        with st.expander("Distribuição da Variável Alvo: Diagnóstico"):
            st.pyplot(plot_diagnosis_distribution(df))
            
        with st.expander("Análise de Separação: Atributo Mais Influente"):
            st.subheader("Análise: Raio do Tumor")
            st.pyplot(plot_separation_density(df, 'radius_mean'))
            
        with st.expander("Análise de Separação: Tamanho e Extremidades"):
            st.write("Comparando as características de 'Pior Caso' que mais distinguem os tumores.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Análise: Área (Pior Caso)")
                fig_area = plot_comparative_boxplot(st.session_state.df, 'area_worst')
                st.pyplot(fig_area)
                
            with col2:
                st.subheader("Análise: Raio (Pior Caso)")
                fig_comparative = plot_comparative_boxplot(st.session_state.df, 'radius_worst')
                st.pyplot(fig_comparative)
                
        with st.expander("Mapa de Calor: Redundâncias e Relações"):
            st.write("Análise de como as variáveis se relacionam entre si e com o diagnóstico final.")
            st.pyplot(plot_correlation_heatmap(df))        

with tab_train_model:
    if st.session_state.df_train is not None:
        with st.expander("Treinar Modelo MLP"):
            if 'cancer_model' not in st.session_state:
                input_size = st.session_state.df_train.shape[1] - 1
                st.session_state.cancer_model = CancerMLP(input_size)

            if st.button("Iniciar Treinamento"):
                with st.spinner("Realizando treinamento... Isso pode levar alguns segundos."):
                    st.session_state.cancer_model.get_model_trainning(st.session_state.df_train)
                    st.session_state.cancer_model.evaluate_model(st.session_state.df_train) 
            
            
        with st.expander("Redução de Dimensionalidade: t-SNE"):
            if st.button("Gerar Gráfico t-SNE"):
                with st.spinner("Calculando projeções espaciais... Isso pode levar alguns segundos."):
                    df_train = clean_prepare_data(st.session_state.df_train)
                    fig_tsne = plot_tsne(df_train)
                    st.pyplot(fig_tsne)       