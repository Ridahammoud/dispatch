import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Création d'un DataFrame pour stocker les données
df = pd.DataFrame(columns=['Début Période', 'Fin Période', 'Opérateurs'])

# Fonction pour ajouter un dispatch
def ajouter_dispatch(debut_periode, fin_periode, operateurs):
    global df
    nouvelle_ligne = pd.DataFrame({
        'Début Période': [debut_periode],
        'Fin Période': [fin_periode],
        'Opérateurs': [operateurs]
    })
    df = pd.concat([df, nouvelle_ligne], ignore_index=True)

# Interface utilisateur
st.title("Gestion des Dispatchs d'Opérateurs")

# Section pour l'ajout de dispatch
st.header("Ajout de Dispatch")
debut_periode = st.date_input("Date de début de période")
fin_periode = st.date_input("Date de fin de période", value=debut_periode + timedelta(days=14))
operateurs = st.text_area("Liste des opérateurs (un par ligne)")

if st.button("Ajouter Dispatch"):
    operateurs_list = operateurs.split('\n')
    if 3 <= len(operateurs_list) <= 7:
        ajouter_dispatch(debut_periode, fin_periode, operateurs_list)
        st.success("Dispatch ajouté avec succès!")
    else:
        st.error("Le nombre d'opérateurs doit être entre 3 et 7.")

# Section pour la consultation des dispatchs
st.header("Consultation des Dispatchs")
date_consultation = st.date_input("Sélectionner une date")
operateur_consultation = st.selectbox("Sélectionner un opérateur", 
                                      df['Opérateurs'].explode().unique() if not df.empty else [])

if st.button("Consulter"):
    resultats = df[
        (df['Début Période'] <= date_consultation) & 
        (df['Fin Période'] >= date_consultation)
    ]
    resultats = resultats[resultats['Opérateurs'].apply(lambda x: operateur_consultation in x)]
    if not resultats.empty:
        st.write("Résultats de la consultation :")
        st.write(resultats)
    else:
        st.info("Aucun dispatch trouvé pour cette date et cet opérateur.")

# Affichage de tous les dispatchs (pour vérification)
if not df.empty:
    st.header("Tous les Dispatchs")
    st.write(df)
