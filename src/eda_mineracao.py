import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def load_histograma(df):
    coluna_alvo = 'class_name'
    if coluna_alvo in df.columns:
        contagem = df[coluna_alvo].value_counts()
        
        st.subheader("Histograma de Frequência")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(
            data=df, 
            y='class_name', 
            order=df['class_name'].value_counts().index,
            color='steelblue',
            ax=ax
        )
        
        ax.set_title("Frequência de Ocorrência por Classe")
        ax.set_xlabel("Quantidade de Casos")
        ax.set_ylabel("Patologia")
        
        st.pyplot(fig)
        
        st.subheader("Tabela de Frequência das Patologias")
        freq_df = pd.DataFrame({
            "Frequência Absoluta": contagem,
            "Percentual (%)": (df[coluna_alvo].value_counts(normalize=True) * 100).round(2)
        })
        st.table(freq_df)
    else:
        st.error(f"Coluna '{coluna_alvo}' não encontrada no dataset.")


