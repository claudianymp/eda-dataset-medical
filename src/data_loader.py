import pandas as pd
import pydicom
import os
import kaggle
import streamlit as st

@st.cache_data
def load_csv_to_dataframe(skip_bad_lines=False): #etapa de Seleção e carregamento da base de dados - KDD
    """Lê arquivo csv e carrega do dataframe."""
    path = './data/train.csv'
    if os.path.exists(path):
        if skip_bad_lines:
            return pd.read_csv(f'{path}', sep=',', on_bad_lines='skip')
        else:
            return pd.read_csv(f'{path}', sep=',')
    return None;
    
def download_sample_data(limit=10):
    """Baixa o CSV e uma amostra de imagens do Kaggle."""
    comp = 'vinbigdata-chest-xray-abnormalities-detection'
    path = './data'
    
    if not os.path.exists(path): os.makedirs(path)
    # Tente estas variações no seu pd.read_csv:
    df = load_csv_to_dataframe(path, True)
    
    # Baixar amostra de DICOMs (apenas se não existirem)
    sample_ids = df['image_id'].unique()[:limit]
    for img_id in sample_ids:
        file = f'train/{img_id}.dicom'
        if not os.path.exists(f'{path}/{file}'):
            kaggle.api.competition_download_file(comp, file, path=path)
    return df

def load_dicom(path):
    """Lê metadados e pixels de um arquivo DICOM."""
    ds = pydicom.dcmread(path)
    return ds

