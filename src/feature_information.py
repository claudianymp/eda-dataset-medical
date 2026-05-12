from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

def get_pca_loadings(df, target_col='diagnosis'):
    """
    Calcula o peso de cada variável no primeiro Componente Principal.
    """
    X = df.drop(columns=[target_col])
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca = PCA(n_components=2)
    pca.fit(X_scaled)
    
    loadings = pd.DataFrame(
        pca.components_.T, 
        columns=['PC1', 'PC2'], 
        index=X.columns
    )
    return loadings.sort_values(by='PC1', ascending=False)