import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_diagnosis_distribution(df):
    fig, ax = plt.subplots(figsize=(18, 10))
    
    if df is not None:
        sns.countplot(
            data=df, 
            x='diagnosis', 
            color='steelblue',
            ax=ax,
            width=0.5
        )
        
        ax.set_xlabel('Diagnóstico (0: Benigno, 1: Maligno)', fontsize=12)
        ax.set_ylabel('Contagem de Amostras', fontsize=12)
        
        total = len(df)
        for p in ax.patches:
            percentage = f'{100 * p.get_height() / total:.1f}%'
            
            x = p.get_x() + p.get_width() / 2
            y = p.get_height()
            
            ax.annotate(
                percentage, 
                (x, y), 
                ha='center', 
                va='bottom', 
                fontsize=12, 
                fontweight='bold',
                xytext=(0, 7), 
                textcoords='offset points'
            )
        
        fig.tight_layout()
    
    return fig


def plot_feature_distribution(df, feature_name):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if df is not None:
        sns.histplot(df[feature_name], kde=True, color='steelblue', ax=ax)
        ax.set_title(f'Distribuição de {feature_name}', fontsize=14)
    
    return fig

def plot_outlier_boxplot(df, coluna_selecionada):
        fig_box, ax_box = plt.subplots(figsize=(10, 5))
        
        if df is not None:
            sns.boxplot(x=df[coluna_selecionada], color='steelblue', ax=ax_box)
            ax_box.set_title(f'Identificação de Outliers: {coluna_selecionada}')
        
        return fig_box

