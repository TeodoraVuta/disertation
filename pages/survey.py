import streamlit as st
from country_list import countries_for_language

st.set_page_config(page_title="Survey")

# Initialize session state variables
session_vars = {
    "page": 1,
    "other_platform": "",
    "other_course": "",
    "selected_platforms": [],
    "selected_courses": [],
    "selected_usage": []
}
for key, value in session_vars.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Navigation functions
def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

# Page 1: Language Selection
if st.session_state.page == 1:
    st.title("Share your experience with e-learning platforms! 📚")
    st.write("## 🌐 Choose the language of the survey:")
    
    col1, col2 = st.columns(2)
    with col1:  
        if st.button("Romana", use_container_width=True):
            st.session_state.language = "ro"
    with col2:  
        if st.button("English", use_container_width=True):
            st.session_state.language = "en"
            next_page()

# Page 2: Introduction
elif st.session_state.page == 2:
    st.write("""
    This survey will help us understand how people use e-learning platforms and why.
    There are **3 parts**:
    1. **Personal Information**
    2. **Your E-learning Experience**
    3. **E-learning Preferences**
    
    It takes about **5-7 minutes** to complete.
    """)
    
    if st.button("🚀 Let's get started!"):
        next_page()

# Page 3: Personal Information
elif st.session_state.page == 3:
    with st.form(key="form_page1"):
        st.write("### Part 1: Personal Information")
        
        st.session_state.age = st.slider("How old are you?", 0, 100)
        st.session_state.gender = st.radio("What is your gender?", ["Male", "Female", "Non-binary/Third gender", "Prefer not to say"])
        
        country_list = [country[1] for country in countries_for_language('en')]
        st.session_state.country = st.selectbox("Where are you from?", country_list)

        education_levels = ["Middle School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"]
        st.session_state.education = st.selectbox("What is your highest level of education?", education_levels)
        
        if st.form_submit_button("Next"):
            next_page()

# Page 4: E-learning Experience
elif st.session_state.page == 4:
    st.write("### Part 2: Your E-learning Experience")
    
    platforms = ["Coursera", "Udemy", "edX", "LinkedIn Learning", "Khan Academy", "My university's platform", 
                 "YouTube", "TikTok", "Other", "I don't use e-learning platforms"]
    st.session_state.selected_platforms = st.multiselect("Select the e-learning platforms you use:", platforms, default=st.session_state.selected_platforms)
    
    if "I don't use e-learning platforms" not in st.session_state.selected_platforms:
        if "Other" in st.session_state.selected_platforms:
            st.session_state.other_platform = st.text_input("Specify other platform(s):", value=st.session_state.other_platform)
        
        course_types = ["Technical (Programming, Data Science)", "Business & Management", "Personal Development", 
                        "Arts & Humanities", "Health & Medicine", "Other"]
        st.session_state.selected_courses = st.multiselect("What types of courses do you take?", course_types, default=st.session_state.selected_courses)

        if "Other" in st.session_state.selected_courses:
            st.session_state.other_course = st.text_input("Specify other course type:", value=st.session_state.other_course)
        
        st.session_state.frequency = st.selectbox("How often do you use e-learning platforms?", ["Daily", "A few times a week", "Once a week", "A few times a month", "Rarely"])
        
        st.session_state.selected_usage = st.multiselect("Why do you use e-learning platforms?", ["Job Purposes", "Personal Interest", "School Purposes"], default=st.session_state.selected_usage)
    
        if "School Purposes" in st.session_state.selected_usage:
            st.session_state.selected_reasons = st.multiselect("Why did you start using e-learning for studying?", 
                ["University platform only", "To learn extra", "For exams/papers", "To understand better", "Better explanations online", "Don't attend classes"])

        st.session_state.learning_preference = st.radio("Do you prefer structured courses or self-paced learning?", 
            ["Structured", "Self-Paced", "A mix of both"], index=st.session_state.get("learning_preference", 0))
        
        st.session_state.satisfaction = st.slider("Rate your satisfaction with online courses (1=Not satisfied, 5=Very satisfied)", 1, 5)
        
        st.session_state.learning_method = st.radio("Preferred learning method:", ["Pre-recorded", "Live classes", "Text-based", "Interactive"])
        
        st.session_state.certification = st.radio("Importance of certification:", ["Very important", "Somewhat important", "Not important"])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_page()
    with col2:
        if st.button("Next"):
            next_page()

# Page 5: E-learning Platform Design
elif st.session_state.page == 5:
    st.write("### Part 3: Design Your Ideal E-learning Platform!")
    
    scenarios = {
        "Technical (Programming, Data Science)": "You are learning Python programming...",
        "Business & Management": "You study management theories...",
        "Personal Development": "You learn time management and communication...",
        "Arts & Humanities": "You explore history, philosophy, and literature...",
        "Health & Medicine": "You study healthcare management and anatomy...",
        "Other": "You explore a completely new field..."
    }
    
    if st.session_state.selected_courses:
        first_course = st.session_state.selected_courses[0]
        if first_course in scenarios:
            st.write(scenarios[first_course])
            st.text_area(f"What do you think about videos about {first_course}? Share your ideas:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_page()
    with col2:
        if st.button("Submit"):
            st.write("### ✅ Thank you for your responses!")
