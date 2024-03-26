import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titre de l'application
st.title('Analyse de données avec Streamlit')

# Chargement des données
uploaded_file = st.file_uploader("Charger un fichier CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('Aperçu des données :')
    st.write(data.head())

    # Afficher les statistiques descriptives
    st.write('Statistiques descriptives :')
    st.write(data.describe())

    # Sélectionner les colonnes pour la visualisation
    columns = st.multiselect('Sélectionner les colonnes', data.columns)

    # Créer les graphiques
    if columns:
        st.write('Graphiques :')
        for column in columns:
            st.write(f'## {column}')
            if data[column].dtype == 'object':
                st.write(data[column].plot(kind='bar'))
                st.pyplot()
            else:
                sns.histplot(data[column])
                st.pyplot()
            st.write('---')

    # Afficher la matrice de corrélation
    st.write('Matrice de corrélation :')
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    corr = numeric_data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    st.pyplot(clear_figure=True)
