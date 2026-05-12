import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

def plot_diagnosis_distribution(df):
    fig, ax = plt.subplots(figsize=(18, 8))
    
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

def plot_feature_distribution(df, column):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if df is not None:
        sns.histplot(df[column], kde=True, color='steelblue', ax=ax)
        ax.set_title(f'Distribuição de {column}', fontsize=14)
    
    return fig

def plot_outlier_boxplot(df, coluna_selecionada):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if df is not None:
            sns.boxplot(x=df[coluna_selecionada], color='steelblue', ax=ax)
            ax.set_title(f'Identificação de Outliers: {coluna_selecionada}')
        
        return fig

def plot_separation_density(df, column):
    fig, ax = plt.subplots(figsize=(18, 8))
    
    if df is not None:
        sns.kdeplot(data=df, x=column, hue='diagnosis', fill=True, 
                palette='coolwarm', alpha=0.5, common_norm=False, ax=ax)
    
        ax.set_title(f'Poder de Separação: {column}', fontsize=14)
        ax.set_xlabel(column, fontsize=12)
        ax.set_ylabel('Densidade', fontsize=12)
        
    return fig

def plot_comparative_boxplot(df, column):
    fig, ax = plt.subplots(figsize=(18, 8))
    
    if df is not None:
        sns.boxplot(data=df, x='diagnosis', y=column, palette='coolwarm', ax=ax)
        
        ax.set_title(f'Distribuição por Classe: {column}', fontsize=14, pad=15)
        ax.set_xlabel('Diagnóstico (0: Benigno, 1: Maligno)', fontsize=12)
        ax.set_ylabel(f'Valor de {column}', fontsize=12)
    
    return fig

def plot_correlation_heatmap(df):
    fig, ax = plt.subplots(figsize=(18, 8))
    cols = ['radius_mean','area_mean','radius_worst','area_worst','perimeter_mean','fractal_dimension_se',
            'texture_mean','symmetry_mean','compactness_worst','concavity_worst','diagnosis']
    
    if df is not None:
        corr = df[cols].corr()
        sns.heatmap(
            corr, 
            annot=True,      
            fmt=".2f",       
            cmap='RdBu_r', 
            center=0,        
            linewidths=.5, 
            ax=ax
        )
        ax.set_title('Matriz de Correlação das Variáveis', fontsize=16, pad=20)
        
    return fig

def plot_tsne(df):
    X = df.drop(columns=['diagnosis'])
    y = df['diagnosis']

    X_scaled = StandardScaler().fit_transform(X)

    # perplexity: número de vizinhos (geralmente entre 5 e 50)
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    X_embedded = tsne.fit_transform(X_scaled)

    fig, ax = plt.subplots(figsize=(18, 8))
    sns.scatterplot(
        x=X_embedded[:, 0], 
        y=X_embedded[:, 1], 
        hue=y, 
        palette='coolwarm', 
        alpha=0.7, 
        ax=ax
    )
    
    ax.set_title('Visualização t-SNE: Agrupamento de Tumores', fontsize=15)
    ax.set_xlabel('t-SNE Componente 1')
    ax.set_ylabel('t-SNE Componente 2')
    ax.legend(title='Diagnóstico (0:B, 1:M)')
    
    return fig

