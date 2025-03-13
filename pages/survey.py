import streamlit as st
from country_list import countries_for_language
import plotly.express as px


st.set_page_config(page_title="survey", page_icon="📈", layout="wide")

st.title("Share your experience with e-learning platforms!")

with st.form(key='my_form'):
    st.write("Please fill out the form below.")
    age = st.slider("How old are you?", 0, 100)

    country_list = [country[1] for country in countries_for_language('en')]
    country = st.selectbox("Where are you from?", country_list)
    education_list = ["Middle School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"]
    education = st.selectbox("What is your highest level of education?", education_list)
    submit_button = st.form_submit_button(label='Submit')