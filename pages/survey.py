import streamlit as st
from country_list import countries_for_language
import time
from urllib.parse import quote
import requests

st.set_page_config(page_title="survey")

if "page" not in st.session_state:
    st.session_state.page = 1
if "other_platform" not in st.session_state:
    st.session_state.other_platform = ""
if "other_course" not in st.session_state:
    st.session_state.other_course = ""
if "selected_platforms" not in st.session_state:
    st.session_state.selected_platforms = []
if "selected_courses" not in st.session_state:
    st.session_state.selected_courses = []

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

st.title("Share your experience with e-learning platforms! 📚" )

if st.session_state.page == 1:
    st.write("## 🌐 Please choose the language of the survey:")

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 2])  # Adjust the column sizes for centering

    with col1:  
        button_ro = st.button("Romana", use_container_width=True)

    with col2:  
        button_en = st.button("English", use_container_width=True)

    if button_ro:
        st.session_state.language = "ro"
        #next_page()
    elif button_en:
        st.session_state.language = "en"
        next_page()
    

elif st.session_state.page == 2:
    
    st.write("""
    This survey will help us understand how people use e-learning platforms and why.  
    There are **3 different parts** to this survey:
    1. **Personal Information**
    2. **Your E-learning Experience + Before & After E-learning**
    3. **What type of e-learning you prefer** 

    It will not take more than 5-7 minutes to complete the survey.
    """)


    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  # Center column for the button
        st.markdown("###")  # Adds some vertical space
        button_start = st.button("🚀 Let's get started!", use_container_width=True)

    if button_start:
        next_page()

elif st.session_state.page == 3:
    with st.form(key="form_page1"):
        st.write("### Part 1: Personal Information")
        
        age = st.slider("How old are you?", 0, 100)

        gender = st.radio("What is your gender?", 
                         ["Male", "Female", "Non-binary/Third gender", "Prefer not to say"])


        country_list = [country[1] for country in countries_for_language('en')]
        country = st.selectbox("Where are you from?", country_list)

        education_list = ["Middle School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"]
        education = st.selectbox("What is your highest level of education?", education_list)

        next_button = st.form_submit_button(label="Next")
        
        if next_button:
            st.session_state.age = age
            st.session_state.country = country
            st.session_state.education = education
            next_page()



elif st.session_state.page == 4:

    st.write("### Part 2: Your E-learning Experience")

    platforms = ["Coursera", "Udemy", "edX", "LinkedIn Learning", "Khan Academy", "Other"]
    st.session_state.selected_platforms = st.multiselect(
        "Select the e-learning platforms you use:", platforms, default=st.session_state.selected_platforms
    )

    if "Other" in st.session_state.selected_platforms:
        st.session_state.other_platform = st.text_input("Please specify the other platform(s) you use:", value=st.session_state.other_platform)
    else:
        st.session_state.other_platform = "" 

    course_types = ["Technical (Programming, Data Science)", "Business & Management", 
                "Personal Development", "Arts & Humanities", "Health & Medicine", "Other"]
    st.session_state.selected_courses = st.multiselect(
    "What types of courses do you usually take?", course_types, default=st.session_state.selected_courses
)

    if "Other" in st.session_state.selected_courses:
        st.session_state.other_course = st.text_input("Please specify the type of course:", value=st.session_state.other_course)
    else:
        st.session_state.other_course = ""  

    frequency = st.selectbox("How often do you use e-learning platforms?", 
                             ["Daily", "A few times a week", "Once a week", "A few times a month", "Rarely"])
    
    usage = st.selectbox("Do you use e-learning platforms for school purposes or personal interest?",
                         ["Personal interest", "School purposes", "Both"])
    if(usage == "School purposes" or usage == "Both"): 

        reasons = ["I wanted to learn extra", "I needed extra information for my exams", 
               "I did not undestand from class", "Professors from online explain better", 
               "I don't go to classes"]
        st.session_state.selected_reasons = st.multiselect(
        "Why did you start using e-learning as a method of studying?", reasons
    )

        st.write("### What was your average GPA before using e-learning platforms?")
        col1, col2 = st.columns(2)

        with col1:
            grade_before = st.text_input("Your grade:", key="grade_before")

        with col2:
            max_grade_before = st.text_input("Out of:", key="max_grade_before")

        if grade_before and max_grade_before:
            try:
                grade_before = float(grade_before)
                max_grade_before = float(max_grade_before)
                if grade_before > max_grade_before:
                    st.error("The grade cannot be higher than the maximum possible grade.")
                elif grade_before < 0 or max_grade_before <= 0:
                    st.error("Grades must be positive numbers.")
                else:
                    st.success(f"Recorded: {grade_before} out of {max_grade_before}")
            except ValueError:  
                    st.error("Please enter valid numeric values.")

        st.write("### What was your average GPA after starting using e-learning platforms?")
        col1, col2 = st.columns(2)

        with col1:
            grade_after = st.text_input("Your grade:", key="grade_after")

        with col2:
            max_grade_after = st.text_input("Out of:", key="max_grade_after")

        if grade_after and max_grade_after:
            try:
                grade_after = float(grade_after)
                max_grade_after = float(max_grade_after)
                if grade_after > max_grade_after:
                    st.error("The grade cannot be higher than the maximum possible grade.")
                elif grade_after < 0 or max_grade_after <= 0:
                    st.error("Grades must be positive numbers.")
                else:
                    st.success(f"Recorded: {grade_after} out of {max_grade_after}")
            except ValueError:  
                    st.error("Please enter valid numeric values.")
        
 

    satisfaction = st.slider("How satisfied are you with online courses? (1 = Not satisfied, 5 = Very satisfied)", 1, 5)

    learning_method = st.radio("Which learning method do you prefer?", 
                               ["Pre-recorded video courses", "Live online classes", 
                                "Text-based courses", "Interactive exercises & projects"])
    
    certification = st.radio("How important is getting a certificate from an online course?", 
                             ["Very important", "Somewhat important", "Not important"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button(label="Next"):
            if not st.session_state.selected_platforms:
                st.warning("Please select at least one platform.")
            elif not st.session_state.selected_courses:
                st.warning("Please select at least one type of course.")
            elif usage == "School purposes" or usage == "Both":
                if not st.session_state.selected_reasons:
                    st.warning("Please select at least one reason for using e-learning platforms.")
                elif not grade_before or not max_grade_before or not grade_after or not max_grade_after:
                    st.warning("Please enter your GPA before and after using e-learning platforms.")
            else:
                st.session_state.frequency = frequency
                st.session_state.satisfaction = satisfaction
                st.session_state.learning_method = learning_method
                st.session_state.certification = certification
                next_page()

    with col2:
        if st.button(label="Back"):
            prev_page()

elif st.session_state.page == 5:
    st.write("### Part 3: It's your turn to create your own online platform!")

    scenarios = {
    "Technical (Programming, Data Science)": """Imagine you are learning Python programming. You start with basic syntax, 
    then move on to data structures and algorithms. After completing the course, you can apply your skills by creating software 
    applications or analyzing big data.""",
    
    "Business & Management": """You are studying management theories and real-world business scenarios. 
    You participate in group projects and learn how to manage teams, understand financial reports, and make strategic decisions 
    for a company. This type of course prepares you for leadership roles in organizations.""",
    
    "Personal Development": """You are learning skills for personal growth, such as time management, emotional intelligence, 
    and effective communication. After completing this course, you can improve your personal and professional relationships, 
    manage stress, and achieve your personal goals.""",
    
    "Arts & Humanities": """You are exploring history, philosophy, literature, and other creative subjects. 
    You engage in discussions, read classic books, and participate in creative writing or art projects. These courses foster creativity 
    and critical thinking while giving you a deeper understanding of human culture.""",
    
    "Health & Medicine": """You're studying anatomy, healthcare management, or public health. 
    You could be learning how to care for patients, manage healthcare organizations, or conduct health research. 
    These courses prepare you to contribute to healthcare and improve the quality of life for individuals and communities.""",
    
    "Other": """You’re exploring a completely new field of knowledge! This could range from courses on sustainability, entrepreneurship, 
    languages, to anything that sparks your interest. You get to be a pioneer in a niche area, learning something unique and specialized."""
}
    if st.session_state.selected_courses:
        first_course = st.session_state.selected_courses[0]

        if first_course in scenarios:
            st.write(scenarios[first_course])

            user_response = st.text_area(f"What do you think about videos about {first_course}? Please share your thoughts and tell us "
                                     "what you'd include in these videos:")




    col1, col2 = st.columns(2)
    with col1:
        if st.button(label="Back"):
            prev_page()
    with col2:
        if st.button(label="Submit"):
            st.write("### ✅ Thank you for your responses!")
            



    # with col3:
    #     if st.button(label="Submit"):
    #         st.write("### ✅ Thank you for your responses!")
    #         st.write(f"- Age: {st.session_state.age}")
    #         st.write(f"- Country: {st.session_state.country}")
    #         st.write(f"- Education: {st.session_state.education}")
    #         st.write(f"- Platforms Used: {', '.join(st.session_state.selected_platforms)}")
    #         if "Other" in st.session_state.selected_platforms and st.session_state.other_platform:
    #             st.write(f"- Other Platform(s): {st.session_state.other_platform}")
    #         st.write(f"- Course Types: {', '.join(st.session_state.selected_courses)}")
    #         if "Other" in st.session_state.selected_courses and st.session_state.other_course:
    #             st.write(f"- Other Course Type: {st.session_state.other_course}")
    #         st.write(f"- Frequency: {frequency}")
    #         st.write(f"- Satisfaction: {satisfaction}")
    #         st.write(f"- Learning Method: {learning_method}")
    #         st.write(f"- Certification Importance: {certification}")
