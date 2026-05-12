import torch
import torch.nn as nn
import torch.optim as optim
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.load_dataset import clean_prepare_data

class CancerMLP(nn.Module):
    def __init__(self, input_size):
        super(CancerMLP, self).__init__()
        self.scaler = StandardScaler()
        self.network = nn.Sequential(
            nn.Linear(input_size, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        return self.network(x)
    
    def run_trainning(self, df):
        X = df.drop(columns=['diagnosis']).values
        y = df['diagnosis'].values
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train_scaled = torch.FloatTensor(self.scaler.fit_transform(X_train))
        y_train_tensor = torch.FloatTensor(y_train).view(-1, 1)

        epochs = st.slider("Quantidade de Épocas:", 10, 500, 100, key="slider_epochs")
        lr = st.number_input("Taxa de Aprendizado:", value=0.01, format="%.3f", key="input_lr")
        
        criterion = nn.BCELoss()
        optimizer = optim.Adam(self.parameters(), lr=lr)
        
        losses = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for epoch in range(epochs):
            self.train()
            optimizer.zero_grad()
            
            outputs = self(X_train_scaled)
            loss = criterion(outputs, y_train_tensor)
            
            loss.backward()
            optimizer.step()
            
            losses.append(loss.item())
            progress_bar.progress((epoch + 1) / epochs)
            status_text.text(f"Época {epoch+1}/{epochs} - Perda: {loss.item():.4f}")
        
        st.success("Treinamento concluído!")
        
        return losses
    
    def plot_learning_curve(self, losses):
        fig, ax = plt.subplots(figsize=(18, 8))
        if losses is not None:
            ax.plot(losses, color='royalblue')
            ax.set_title("Curva de Aprendizado")
        
        return fig
    
    def get_model_trainning(self, df):
        if df is not None:
            temp_df = clean_prepare_data(df)
            losses = self.run_trainning(temp_df)
            st.pyplot(self.plot_learning_curve(losses))
            
    def evaluate_model(self, df):
        temp_df = df.copy()
        if temp_df['diagnosis'].dtype == 'object':
            temp_df['diagnosis'] = temp_df['diagnosis'].map({'M': 1, 'B': 0})
        
        X = temp_df.drop(columns=['diagnosis']).values
        y = temp_df['diagnosis'].values.astype(int)
        _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_test_scaled = torch.FloatTensor(self.scaler.transform(X_test))
        y_test_tensor = torch.FloatTensor(y_test).view(-1, 1)

        self.eval()
        with torch.no_grad():
            predictions = self(X_test_scaled)
            predicted_classes = (predictions > 0.5).float()
            correct = (predicted_classes == y_test_tensor).sum().item()
            accuracy = correct / y_test_tensor.size(0)
            
            st.metric("Acurácia Final no Teste", f"{accuracy*100:.2f}%")
            
