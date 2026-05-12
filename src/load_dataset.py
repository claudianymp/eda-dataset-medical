import pandas as pd
import streamlit as st
import numpy as np

@st.cache_data
def load_csv_to_dataframe(path):
    df = pd.read_csv(path)
    df = df.replace([np.inf, -np.inf], np.nan)
    
    return df

def load_info_dataset(df):
  if df is not None:
    df_info = pd.DataFrame({
        "Coluna": df.columns,
        "Tipo de Dado": [str(t) for t in df.dtypes.values],
        "Valores Não Nulos": df.count().values,
        "Valores Nulos": df.isnull().sum().values
    })
    st.table(df_info)

    st.write(f"**Total de registros:** {df.shape[0]} | **Total de colunas:** {df.shape[1]}")

def load_statistics_summary(df):
    if df is not None:
        st.dataframe(df.describe().T, width='stretch')
        st.markdown("""
        * **Count:** Total de amostras não nulas.
        * **Mean (Média):** Valor médio aritmético (útil para ver o 'tamanho padrão' do tumor).
        * **Std (Desvio Padrão):** O quanto os dados variam. Valores altos indicam grande diversidade clínica.
        * **Min/Max:** Os limites extremos observados na amostra.
        * **25%, 50%, 75% (Quartis):** Ajudam a identificar a distribuição. O **50% (Mediana)** mostra o valor central, sendo menos sensível a outliers que a média.
        """)   
        
def clean_prepare_data(df):
    temp_df = None
    if df is not None:
        temp_df = df.copy()
        temp_df = temp_df.dropna(subset=['diagnosis'])
        if temp_df['diagnosis'].dtype == 'object':
            temp_df['diagnosis'] = temp_df['diagnosis'].map({'M': 1, 'B': 0})
        
        temp_df = temp_df.dropna(subset=['diagnosis'])
        temp_df['diagnosis'] = temp_df['diagnosis'].astype(int)
        
        temp_df = temp_df.fillna(temp_df.mean())
    
    return temp_df 
    