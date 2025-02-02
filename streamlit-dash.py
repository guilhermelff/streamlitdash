import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do aplicativo
st.title("Meu Data App com Streamlit")

# Seção para upload do arquivo CSV
st.header("Carregar arquivo CSV")
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Leitura do CSV
    df = pd.read_csv(uploaded_file)
    
    # Exibir as primeiras linhas do DataFrame
    st.subheader("Visualização dos Dados")
    st.write(df.head())
    
    # Exibir informações estatísticas
    st.subheader("Estatísticas Descritivas")
    st.write(df.describe())
    
    # Listar colunas disponíveis
    st.subheader("Colunas Disponíveis")
    st.write(df.columns.tolist())
    
    # Verificar colunas numéricas para plotar um histograma
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()
    
    if numeric_columns:
        # Seleção da coluna numérica
        coluna = st.selectbox("Selecione uma coluna numérica para plotar um histograma", numeric_columns)
        
        # Criação do histograma
        fig, ax = plt.subplots()
        ax.hist(df[coluna].dropna(), bins=20, color="blue", alpha=0.7)
        ax.set_title(f"Histograma da coluna {coluna}")
        ax.set_xlabel(coluna)
        ax.set_ylabel("Frequência")
        
        # Exibir o gráfico no Streamlit
        st.pyplot(fig)
    else:
        st.write("Não há colunas numéricas disponíveis para plotar o histograma.")
