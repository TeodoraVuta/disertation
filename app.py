import streamlit as st
import mysql.connector

# st.set_page_config(page_title="My Streamlit App", layout="wide")

def get_db_connection():
    conn = mysql.connector.connect(
        host="sql7.freesqldatabase.com",
        user="sql7774673",
        password="RuH8UTgrJt", 
        database="sql7774673",
        port=3306
    )

    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS survey_responses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            age INT,
            gender VARCHAR(50),
            country VARCHAR(100),
            education VARCHAR(100),
            selected_platforms TEXT,
            selected_courses TEXT,
            preference VARCHAR(100),
            selected_usage TEXT,
            job VARCHAR(1000),
            mandatory VARCHAR(10),
            promotion VARCHAR(10),
            reasons_for_choosing_course TEXT,
            check_lectures VARCHAR(10),
            check_exams VARCHAR(10),
            grade_before FLOAT,
            max_grade_before FLOAT,
            grade_after FLOAT,
            max_grade_after FLOAT,
            learning_method VARCHAR(100),
            frequency VARCHAR(100),
            payed_courses VARCHAR(10),
            payment INT,
            best_course VARCHAR(500),
            dropout_status VARCHAR(10),
            dropout_reason VARCHAR(100),
            completion_rate VARCHAR(50),
            certification VARCHAR(100),
            notes TEXT,
            multitasking VARCHAR(50),
            vr_usage VARCHAR(10),
            live_interaction VARCHAR(10),
            immersive_learning VARCHAR(10),
            replacement VARCHAR(10),
            ai_assistant VARCHAR(10),
            ai_professor VARCHAR(10),
            about_course TEXT,
            specific_course TEXT,
            submission_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    return conn, cursor  
    

st.write("In the making...  ")
st.write("Platformele tale preferate de e-learning intr-un singur loc! ")

platforms = {
    "Coursera": [
        {"title": "Machine Learning by Andrew Ng", "url": "https://www.youtube.com/watch?v=Gv9_4yMHFhI"},
        {"title": "The Science of Well-Being", "url": "https://www.youtube.com/watch?v=93L4j-_7Wpg"},
    ],
    "Udemy": [
        {"title": "100 Days of Code: The Complete Python Pro Bootcamp", "url": "https://www.youtube.com/watch?v=1gP5t6zMf5k"},
        {"title": "Web Development Bootcamp", "url": "https://www.youtube.com/watch?v=0yW4o9QJ3t4"},
    ],
    "edX": [
        {"title": "CS50: Introduction to Computer Science", "url": "https://www.youtube.com/watch?v=8mAITcNt710"},
        {"title": "Data Science MicroMasters", "url": "https://www.youtube.com/watch?v=Gp6TdpEUN3s"},
    ],
}

# Coloane pentru cele 3 platforme
col1, col2, col3 = st.columns(3)

for col, (platform, videos) in zip([col1, col2, col3], platforms.items()):
    with col:
        st.subheader(platform)
        for video in videos:
            st.markdown(f"**{video['title']}**")
            st.video(video['url'])  # Înlocuiește URL-ul cu linkul YouTube direct
            st.markdown("---")
