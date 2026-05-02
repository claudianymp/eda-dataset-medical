import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_info_dataset(df):
    st.subheader("Informações Gerais")
    
    df_info = pd.DataFrame({
                "Coluna": df.columns,
                "Tipo de Dado": df.dtypes.values,
                "Valores Não Nulos": df.count().values,
                "Valores Nulos": df.isnull().sum().values
            })
    st.table(df_info)
    
    st.write(f"**Total de registros:** {df.shape[0]} | **Total de colunas:** {df.shape[1]}")

@st.cache_data
def limpar_dados(df): #etapa de Limpeza - KDD
    df = df.fillna(0)
    
    cols_coord = ['x_min', 'y_min', 'x_max', 'y_max']
    for col in cols_coord:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    return df
        
def load_estatistica_bruta(df):
    st.subheader("Estatística Descritiva do Dataset")
    st.table(df.describe(include='all').T)
