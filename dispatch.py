import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Création d'un DataFrame pour stocker les données
df = pd.DataFrame(columns=['Période', 'Groupe', 'Opérateurs'])

# Fonction pour ajouter un dispatch
def ajouter_dispatch(periode, groupe, operateurs):
    global df
    nouvelle_ligne = pd.DataFrame({'Période': [periode], 'Groupe': [groupe], 'Opérateurs': [operateurs]})
    df = pd.concat([df, nouvelle_ligne], ignore_index=True)

# Interface utilisateur pour l'ajout de dispatch
st.header("Ajout de dispatch")
periode = st.date_input("Période de début")
groupe = st.text_input("Nom du groupe")
operateurs = st.text_area("Liste des opérateurs (un par ligne)")

if st.button("Ajouter dispatch"):
    ajouter_dispatch(periode, groupe, operateurs.split('\n'))
    st.success("Dispatch ajouté avec succès!")

# Interface utilisateur pour la consultation
st.header("Consultation des dispatchs")
date_debut = st.date_input("Date de début")
date_fin = st.date_input("Date de fin")
operateur = st.selectbox("Sélectionner un opérateur", df['Opérateurs'].explode().unique())

if st.button("Consulter"):
    resultats = df[(df['Période'] >= date_debut) & (df['Période'] <= date_fin)]
    resultats = resultats[resultats['Opérateurs'].apply(lambda x: operateur in x)]
    st.write(resultats)
