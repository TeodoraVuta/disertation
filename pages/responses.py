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
        return pd.DataFrame()  # Returnează un DataFrame gol în cazul unei erori
    query = "SELECT * FROM survey_responses"
    df = pd.read_sql(query, conn)
    close_db_connection(conn, cursor)
    return df

def plot_age_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], kde=True, bins=20, color='skyblue')
    plt.title('Distribuția vârstei utilizatorilor', fontsize=14)
    plt.xlabel('Vârstă', fontsize=12)
    plt.ylabel('Frecvență', fontsize=12)
    st.pyplot(plt)

# Vizualizare date - grafic cu distribuția educației
def plot_education_distribution(df):
    plt.figure(figsize=(10, 6))
    education_counts = df['education'].value_counts()
    sns.barplot(x=education_counts.index, y=education_counts.values, palette='viridis')
    plt.title('Distribuția nivelului de educație', fontsize=14)
    plt.xlabel('Nivel de educație', fontsize=12)
    plt.ylabel('Număr de utilizatori', fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt)


def plot_education_distribution(df):
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

    df['educatie_standard'] = df['education'].replace(educatie_standard)

    education_counts = df['educatie_standard'].value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=education_counts.index, y=education_counts.values, palette='viridis')
    plt.title('Distribuția nivelului de educație', fontsize=14)
    plt.xlabel('Nivel de educație', fontsize=12)
    plt.ylabel('Număr de utilizatori', fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt)


# Pagina principală
def main():
    st.title('Vizualizare date Survey')

    # Extrage datele din baza de date
    df = get_survey_data()

    # Grafice
    st.subheader('Distribuția vârstei utilizatorilor')
    plot_age_distribution(df)

    st.subheader('Distribuția nivelului de educație')
    plot_education_distribution(df)

if __name__ == '__main__':
    main()



st.write("In the making...  ")
