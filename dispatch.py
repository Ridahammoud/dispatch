import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Définition des équipes
team_1_Christian = ["Abdelaziz Hani Ddamir", "Aboubacar Tamadou", "Alhousseyni Dia", "Berkant Ince",
                    "Boubakar Sidiki Ouedrago", "Boubou Gassama", "Chamsoudine Abdoulwahab", "Dagobert Ewane Jene",
                    "Dione Mbaye", "Doro Diaw", "Enrique Aguey - Zinsou", "Fabien Prevost", "Fabrice Nelien", 
                    "Idrissa Yatera", "Jabbar Arshad", "Jacques-Robert Bertrand", "Karamoko Yatabare", 
                    "Mahamadou Niakate", "Mamadou Bagayogo", "Mamadou  Kane", "Mohamed Lamine Saad", "Moussa Soukouna",
                    "Pascal Nouaga", "Rachid Ramdane", "Taha Hsine", "Tommy Lee Casdard", "Volcankan Ince", 
                    "Youssef Mezouar", "Youssouf Wadiou", "Elyas Bouzar", "Reda Jdi"]

team_2_Hakim = ["Abdoul Ba", "Aladji Sakho", "Amadou Sow", "Arfang Cisse", "Bouabdellah Ayad", 
                "Cheickne Kebe", "Dany Chantre", "David Diockou N'Diaye", "Dylan Baron", "Fabien Tsop Nang", 
                "Fabrice Badibengi", "Faker Ajili", "Fodie Koita Camara", "Gaetan Girard", "Idy Barro", 
                "Aboubacar Cisse", "Johnny Michaud", "Ladji Bamba", "Mamadou Fofana", "Mamadou Kane", 
                "Mamadou Sangare", "Mamadou Soumare", "Mohamed Bouchleh", "Mostefa Mokhtari", "Nassur Ibrahim", 
                "Riadh Moussa", "Saim Haroun Bhatti", "Samir Chikh", "Tony Allot", "Walter Tavares"]

# Combinaison des deux équipes
all_operators = team_1_Christian + team_2_Hakim

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

# Utilisation de st.multiselect pour choisir les opérateurs
operateurs = st.multiselect("Sélectionner les opérateurs (entre 3 et 7)", options=all_operators)

# Vérification du nombre d'opérateurs sélectionnés
if 3 <= len(operateurs) <= 7:
    if st.button("Ajouter Dispatch"):
        ajouter_dispatch(debut_periode, fin_periode, operateurs)
        st.success("Dispatch ajouté avec succès!")
else:
    st.error("Veuillez sélectionner entre 3 et 7 opérateurs.")

# Section pour la consultation des dispatchs
st.header("Consultation des Dispatchs")
date_consultation = st.date_input("Sélectionner une date")
operateur_consultation = st.selectbox("Sélectionner un opérateur", options=all_operators)

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
