import streamlit as st
from db_utils import get_db_connection, close_db_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📋 Răspunsuri colectate")

def get_survey_data():
    conn, cursor = get_db_connection()
    if conn is None:
        st.error("Nu s-a putut stabili conexiunea la baza de date.")
        return pd.DataFrame()  
    query = "SELECT * FROM survey_responses"
    df = pd.read_sql(query, conn)
    close_db_connection(conn, cursor)
    return df

df = get_survey_data()

educatie_standard = {
    "Bachelor's Degree": "Licență",
    "Licenta": "Licență",
    "Licen??" : "Licență",
    "licență": "Licență",
    "Master's Degree": "Master",
    "Master": "Master",
    "masterat": "Master",
    "High School": "Liceu",
    "Liceu": "Liceu",
    "PhD": "Doctorat",
    "Doctorat": "Doctorat", 
    "?coala Primar?" : "Școală Primară",
    "?coala General?" : "Școală Generală",
}
    
gender_standard = {
    "Female": "Feminin",
    "Male": "Masculin",
    "Non-binary/Third gender": "Non-binary",
    "Prefer not to say" : "Prefer să nu spun",
    "Feminin" : "Feminin",
    "Masculin" : "Masculin",
    "Non-binar/Al treilea gen" : "Non-binary",
    "Prefer s? nu spun" : "Prefer să nu spun",
}

df['educatie_standard'] = df['education'].replace(educatie_standard)

education_counts = df['educatie_standard'].value_counts()
education_options = ['Toate'] + list(df['educatie_standard'].dropna().unique())


df['gender_standard'] = df['gender'].replace(gender_standard)

gender_counts = df['gender_standard'].value_counts()

if not df.empty:
    col_filters, col_table = st.columns([1, 3])  

    with col_filters:
        selected_sex = st.selectbox("Selectează sexul:", options=df['gender_standard'].dropna().unique())
        selected_education = st.selectbox("Selectează nivelul de educație:", options=df['educatie_standard'].dropna().unique())

    if selected_education == 'Toate':
        filtered_df = df[df['gender_standard'] == selected_sex]
    else:
        filtered_df = df[
            (df['gender_standard'] == selected_sex) &
            (df['educatie_standard'] == selected_education)
        ]

    filtered_df = df[
        (df['gender_standard'] == selected_sex) &
        (df['educatie_standard'] == selected_education)
    ]

    with col_table:
        st.dataframe(filtered_df, use_container_width=True)
else:
    st.warning("Nu există date disponibile pentru afișare.")

