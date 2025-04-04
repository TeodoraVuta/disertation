import streamlit as st
from country_list import countries_for_language
from urllib.parse import quote

st.set_page_config(page_title="survey")

if "page" not in st.session_state:
    st.session_state.page = 1

keys_to_initialize = [
    ("other_platform", ""),
    ("other_course", ""),
    ("selected_platforms", []),
    ("selected_courses", []),
    ("selected_usage", []),
    ("job", ""),
    ("mandatory", ""),
    ("selected_reasons", []),
    ("learning_preference", 0),
    ("promotion", ""),
    ("grade_before", ""),
    ("max_grade_before", ""),
    ("grade_after", ""),
    ("max_grade_after", ""),
    ("learning_method", ""),
    ("certification", ""),
    ("multitasking", ""),
    ("notes", []),
    ("bestCourse", ""),
    ("dropOut", ""),
    ("dropOutReason", ""),
    ("completationRate", 0),
    ("vr", ""),
    ("liveInteraction", ""),
    ("immersive", ""),
    ("replacement", ""),
    ("aiAssistant", ""),
    ("aiProfessor", "")
]

for key, default_value in keys_to_initialize:
    if key not in st.session_state:
        st.session_state[key] = default_value



def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

st.title("Share your experience with e-learning platforms! 📚")

if st.session_state.page == 1:
    st.write("## 🌐 Please choose the language of the survey:")

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 2])

    with col1:
        button_ro = st.button("Romana", use_container_width=True)

    with col2:
        button_en = st.button("English", use_container_width=True)

    if button_ro:
        st.session_state.language = "ro"
        # next_page()
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

    with col2:
        st.markdown("###")
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

    platforms = ["Coursera", "Udemy", "edX", "LinkedIn Learning", "Khan Academy", "My university's platform",
                 "Youtube", "TikTok", "Other"]
    platforms = st.multiselect(
        "Select the e-learning platforms (one or more) you use:", platforms, default=st.session_state.selected_platforms
    )

    if "Other" in st.session_state.selected_platforms:
        other_platform = st.text_input("Please specify the other platform(s) you use:",
                                                         value=st.session_state.other_platform)
        platforms.append(other_platform)
    else:
        other_platform = ""

    course_types = ["Technical (Programming, Data Science)", "Business & Management",
                    "Personal Development", "Arts & Humanities", "Health & Medicine", "Other"]
    selected_courses = st.multiselect(
        "What types of courses do you usually take? (select one or more)", course_types, default=st.session_state.selected_courses
    )

    if "Other" in st.session_state.selected_courses:
        other_course = st.text_input("Please specify the type of course:",
                                                       value=st.session_state.other_course)
        selected_courses.append(other_course)
    else:
        other_course = ""

    frequency = st.radio("How often do you use e-learning platforms?",
                              ["Daily", "A few times a week", "Once a week", "A few times a month", "Rarely"])

    st.write("Why do you visit e-learning platforms?")
    usage_options = ["Job Purposes", "Personal interest", "School purposes"]

    selected_usage = []
    for option in usage_options:
        if st.checkbox(option, value=(option in st.session_state.selected_usage)):
            selected_usage.append(option)        

    if "Job Purposes" in st.session_state.selected_usage:
        job = st.text_input("What is your job?", value=st.session_state.job)
        mandatory = st.radio("Is it mandatory to take online courses for your job?", ["Yes", "No"])
        promotion = st.radio("Do you think that taking online courses will help/helped you get a promotion?", ["Yes", "No"])
    else:
        job = ""
        mandatory = ""
        promotion = ""

    if "School purposes" in st.session_state.selected_usage:
        reasons = ["I only use my university's platform", "I want to learn extra", "I need extra information for my exams/papers",
                   "I don't understand from class", "Professors from online explain better",
                   "I don't go to classes"]
        st.session_state.selected_reasons = st.multiselect(
            "Why did you start using e-learning as a method of studying?", reasons, default=st.session_state.selected_reasons
        )

        beforeClasses = st.radio("Do you usually check your lectures before class?", ["Yes", "No"])
        exams = st.radio("Do you usually check your lectures all year long or "
        "only in the exam sessions?", ["All year long", "Exam session only"])
        

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
    else:
        reasons = []
        beforeClasses = None
        exams = None
        grade_before = None
        max_grade_before = None
        grade_after = None
        max_grade_after = None
            
    learning_method = st.radio("Which learning method do you prefer?",
                                ["Pre-recorded video courses", "Live online classes",
                                 "Text-based courses", "Interactive exercises & projects"])

    certification = st.radio("How important is getting a certificate from an online course?",
                              ["Very important", "Somewhat important", "Not important"])
    
    learning_preference = st.radio(
        "Do you prefer structured courses (with clear modules and longer time to complete) or short videos?",
        ["Structured courses", "Short videos", "Both"])
    
    multitasking = st.radio(
        "Do you multitask while taking an online course?",
        ["Never", "Sometimes",  "Often", "Always"])
    
    notes = st.multiselect(
        "How do you usually take notes when studying online? (select one or more)",
        ["I don’t take notes", "Handwritten", "Digital (OneNote, Notion, etc.)", "Summaries", "Mind maps"])
    
    bestCourse = st.text_input("What was the best course you took? "
    "(it can be a link, the name, or a short description)", value="")

    dropOut = st.radio("Have you ever dropped out of an online course?", ["Yes", "No"])
    if dropOut == "Yes":
        dropOutReason = st.radio(
        "Why did you drop out?",
        ["Too hard", "Too boring", "No time", "Not useful", "Other"])
    
    completationRate = st.slider("What percentage of the course do you usually complete?",
    0, 100, 50)

    preference = st.radio("Do you prefere online courses or face-to-face courses?", 
                          ["Online", "Face-to-face"])
    
    st.write("### Would you try?")
    vr = st.radio("Would you try VR or AI-based online learning if available?", 
                  ["Yes", "No"])
    liveInteraction = st.radio("Would you be interested in live, interactive simulations for learning (e.g., virtual labs, business simulations)?",
                  ["Yes", "No"])
    immersive = st.radio("Would you participate in a fully immersive virtual campus for online education?",
                  ["Yes", "No"])
    replacement = st.radio("Do you think that e-learning platforms will replace traditional education?",
                  ["Yes", "No", "Hybride model will dominate", "Not sure"])
    aiAssistant = st.radio("Would you use an AI assistant to help you with your online courses?",
                  ["Yes", "No"])
    aiProfessor = st.radio("Do you think the AI will replace the professors in the future?",
                  ["Yes", "No"])
    


    col1, col2 = st.columns(2)

    with col1:
        if st.button(label="Next"):
        # Update session state with current selections
            st.session_state.selected_platforms = platforms  # from the multiselect input
            st.session_state.selected_courses = selected_courses  # from the multiselect input
            st.session_state.selected_usage = selected_usage  # from the checkbox inputs

            # Handle other field updates
            st.session_state.job = job
            st.session_state.mandatory = mandatory
            st.session_state.promotion = promotion
            st.session_state.selected_reasons = reasons
            st.session_state.grade_before = grade_before
            st.session_state.max_grade_before = max_grade_before
            st.session_state.grade_after = grade_after
            st.session_state.max_grade_after = max_grade_after
            st.session_state.learning_method = learning_method
            st.session_state.certification = certification
            st.session_state.multitasking = multitasking
            st.session_state.notes = notes
            st.session_state.bestCourse = bestCourse
            st.session_state.dropOut = dropOut
            st.session_state.dropOutReason = dropOutReason
            st.session_state.completationRate = completationRate
            st.session_state.preference = preference
            st.session_state.vr = vr
            st.session_state.liveInteraction = liveInteraction
            st.session_state.immersive = immersive
            st.session_state.replacement = replacement
            st.session_state.aiAssistant = aiAssistant
            st.session_state.aiProfessor = aiProfessor

            # Now check the validation conditions
            if not st.session_state.selected_platforms:
                st.warning("Please select at least one platform.")
            elif "Other" in st.session_state.selected_platforms and not st.session_state.other_platform.strip():
                st.warning("Please specify the other platform(s) you use.")
            elif not st.session_state.selected_courses:
                st.warning("Please select at least one type of course.")
            elif "Other" in st.session_state.selected_courses and not st.session_state.other_course.strip():
                st.warning("Please specify the courses you take.")
            elif "School purposes" in st.session_state.selected_usage:
                if not st.session_state.selected_reasons:
                    st.warning("Please select at least one reason for using e-learning platforms.")
                elif not grade_before or not max_grade_before or not grade_after or not max_grade_after:
                    st.warning("Please enter your GPA before and after using e-learning platforms.")
            else:
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
            # Custom HTML and CSS for pop-up effect, smaller size, and disappearing after 6 seconds
            st.markdown("""
            <style>
                .popup {
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background-color: #28a745;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 8px;
                    font-size: 16px;
                    font-weight: bold;
                    display: inline-block;
                    width: 60%;
                    text-align: center;
                    animation: popup 1s ease-in-out;
                }

                @keyframes popup {
                    0% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
                    100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
                }

                .bar {
                    height: 5px;
                    background-color: #34b3a0;
                    border-radius: 5px;
                    animation: progressBar 5s linear forwards;
                }

                @keyframes progressBar {
                    0% { width: 0; }
                    100% { width: 100%; }
                }
            </style>
            <div class="popup">
                🎉 Thank you for your responses! Your input is valuable! 😊
                <div class="bar"></div>
            </div>
            <script>
                setTimeout(function() {
                    document.querySelector('.popup').style.display = 'none';
                }, 6000);
            </script>
            """, unsafe_allow_html=True)
            st.balloons()
