import streamlit as st
from country_list import countries_for_language

st.set_page_config(page_title="survey", page_icon="📋", layout="centered")


if "page" not in st.session_state or st.session_state.get("force_restart", False):
    st.session_state.page = 1
    st.session_state.force_restart = False

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

def reset_page():
    st.session_state.page = 1
    st.session_state.force_restart = True
    
keys_to_initialize = [
    ("page", 1),
    ("language", "en"),
    ("countries", countries_for_language("en")),
    ("age", None),
    ("gender", None),
    ("country", None),
    ("education", None),
    ("selected_platforms", []),
    ("other_platform", ""),
    ("selected_courses", []),
    ("other_course", ""),
    ("selected_usage", []),
    ("job", ""),
    ("mandatory", ""),
    ("promotion", ""),
    ("selected_reasons", []),
    ("grade_before", None),
    ("max_grade_before", None),
    ("grade_after", None),
    ("max_grade_after", None),
    ("learning_method", ""),
    ("certification", ""),
    ("multitasking", ""),
    ("notes", []),
    ("bestCourse", ""),
    ("dropOut", ""),
    ("dropOutReason", ""),
    ("completationRate", 50),
    ("preference", ""),
    ("vr", ""),
    ("liveInteraction", ""),
    ("immersive", ""),
    ("replacement", ""),
    ("aiAssistant", ""),
    ("aiProfessor", ""),
]

for key, default_value in keys_to_initialize:
    if key not in st.session_state:
        st.session_state[key] = default_value

translations = {
    "en": {
        "age": "How old are you?",
        "gender": "What is your gender?",
        "gender_list": ["Male", "Female", "Non-binary/Third gender", "Prefer not to say"],        "next_button": "Next",
        "country": "Where are you from?",
        "education": "What is your highest level of education?",
        "intro": """
        This survey will help us understand how people use e-learning platforms and why.  
        There are **3 different parts** to this survey:
        1. **Personal Information**
        2. **Your learning experience before and after starting using e-learning**
        3. **Design your own e-learning course** 

        It will not take more than 5-7 minutes to complete the survey.
        """,
        "start_button": "🚀 Let's get started!",
        "platforms": "Please select the e-learning platforms you use:",
        "course_types": "Please select the types of courses you take:",
        "frequency": "How often do you visit e-learning platforms?",
        "why_visit": "Why do you visit e-learning platforms?",
        "job": "What is your current job title?",
        "mandatory_courses": "Are these courses mandatory for your job?",
        "promotion_courses": "Are you taking courses to get a promotion?",
        "school_reasons": "Why do you use e-learning for school purposes?",
        "check_lectures": "Do you check the course materials before classes?",
        "check_exams": "How often do you refer to e-learning materials for exams?",
        "grade_before": "What was your GPA before using e-learning?",
        "max_grade_before": "What is the maximum grade you could achieve?",
        "grade_after": "What is your GPA after using e-learning?",
        "max_grade_after": "What is the maximum grade you could achieve?",
        "learning_method": "What learning method do you prefer?",
        "certification": "How important is getting a certification?",
        "learning_preference": "Do you prefer structured courses or short videos?",
        "multitasking": "How often do you multitask while learning?",
        "notes": "What kind of notes do you take during learning?",
        "best_course": "What is the best course you’ve taken?",
        "dropOut": "Have you ever dropped out of an online course?",
        "dropOutReason": "What was the reason you dropped out?",
        "completion_rate": "What is your typical course completion rate?",
        "preference_onl": "Do you prefer online learning or face-to-face learning?",
        "vr": "Would you be interested in using virtual reality for learning?",
        "live_interaction": "Would you like to have live interactions with instructors?",
        "immersive": "Would you be interested in immersive learning experiences?",
        "replacement": "Do you think AI will replace traditional professors?",
        "ai_assistant": "Would you use an AI assistant for learning?",
        "ai_professor": "Would you accept an AI professor?",
        "back_button": "Back",
        "warning_platforms": "Please select at least one platform.",
        "warning_other_platform": "If 'Other' is selected, please specify the platform.",
        "warning_courses": "Please select at least one course type.",
        "warning_other_course": "If 'Other' is selected, please specify the course type.",
        "warning_usage": "Please select at least one usage option.",
        "warning_reasons": "Please select at least one reason for using e-learning for school purposes.",
        "warning_gpa": "Please provide both your GPA before and after using e-learning.",
        "warning_job": "Please specify your job title.",
        "warning_mandatory": "Please indicate whether the courses are mandatory for your job.",
        "warning_promotion": "Please indicate whether you are taking courses for a promotion.",
        "warning_notes": "Please select at least one note-taking method.",
        "warning_best_course": "Please provide the name of the best course you've taken."
    },
    "ro": {
        "age": "Câți ani ai?",
        "gender": "Care este genul tău?",
        "gender_list": ["Masculin", "Feminin", "Non-binary", "Prefer să nu spun"],
        "next_button": "Următorul",
        "country": "Din ce țară ești?",
        "education": "Care este cel mai înalt nivel de educație pe care l-ai obținut?",
        "intro": """
        Acest chestionar ne va ajuta să înțelegem cum folosesc oamenii platformele de învățare online și de ce.  
        Există **3 părți** în acest chestionar:
        1. **Informații personale**
        2. **Experiența de învățare înainte și după utilizarea platformelor de învățare online**
        3. **Crearea unui curs de învățare online propriu**

        Nu va dura mai mult de 5-7 minute pentru a completa chestionarul.
        """,
        "start_button": "🚀 Să începem!",
        "platforms": "Selectați platformele de învățare online pe care le utilizați:",
        "course_types": "Selectați tipurile de cursuri pe care le urmăriți:",
        "frequency": "Cât de des vizitați platformele de învățare online?",
        "why_visit": "De ce vizitați platformele de învățare online?",
        "job": "Care este titlul dumneavoastră profesional?",
        "mandatory_courses": "Aceste cursuri sunt obligatorii pentru locul dumneavoastră de muncă?",
        "promotion_courses": "Urmăriți cursuri pentru a obține o promovare?",
        "school_reasons": "De ce utilizați e-learning pentru scopuri școlare?",
        "check_lectures": "Verificați materialele cursurilor înainte de lecții?",
        "check_exams": "Cât de des consultați materialele pentru examene?",
        "grade_before": "Care a fost media dumneavoastră înainte de a folosi e-learning?",
        "max_grade_before": "Care este nota maximă pe care ați putea să o obțineți?",
        "grade_after": "Care este media dumneavoastră după utilizarea e-learning?",
        "max_grade_after": "Care este nota maximă pe care ați putea să o obțineți?",
        "learning_method": "Ce metodă de învățare preferați?",
        "certification": "Cât de importantă este obținerea unei certificări?",
        "learning_preference": "Preferiți cursuri structurate sau videoclipuri scurte?",
        "multitasking": "Cât de des multitasking în timpul învățării?",
        "notes": "Ce tip de notițe luați în timpul învățării?",
        "best_course": "Care este cel mai bun curs pe care l-ați urmat?",
        "dropOut": "Ați renunțat vreodată la un curs online?",
        "dropOutReason": "Care a fost motivul renunțării?",
        "completion_rate": "Care este rata dumneavoastră tipică de finalizare a cursurilor?",
        "preference_onl": "Preferi învățarea online sau față în față?",
        "vr": "Ați fi interesat să folosiți realitatea virtuală pentru învățare?",
        "live_interaction": "Ați dori să aveți interacțiuni live cu instructorii?",
        "immersive": "Ați fi interesat de experiențe de învățare imersive?",
        "replacement": "Credeți că AI va înlocui profesorii tradiționali?",
        "ai_assistant": "Ați folosi un asistent AI pentru învățare?",
        "ai_professor": "Ați accepta un profesor AI?",
        "back_button": "Înapoi",
        "warning_platforms": "Vă rugăm să selectați cel puțin o platformă.",
        "warning_other_platform": "Dacă ați selectat 'Altele', vă rugăm să specificați platforma.",
        "warning_courses": "Vă rugăm să selectați cel puțin un tip de curs.",
        "warning_other_course": "Dacă ați selectat 'Altele', vă rugăm să specificați tipul de curs.",
        "warning_usage": "Vă rugăm să selectați cel puțin o opțiune de utilizare.",
        "warning_reasons": "Vă rugăm să selectați cel puțin un motiv pentru utilizarea e-learning pentru scopuri școlare.",
        "warning_gpa": "Vă rugăm să completați atât media înainte, cât și după utilizarea e-learning.",
        "warning_job": "Vă rugăm să specificați titlul dumneavoastră de job.",
        "warning_mandatory": "Vă rugăm să indicați dacă cursurile sunt obligatorii pentru locul dumneavoastră de muncă.",
        "warning_promotion": "Vă rugăm să indicați dacă urmați cursuri pentru o promovare.",
        "warning_notes": "Vă rugăm să selectați cel puțin o metodă de notițe.",
        "warning_best_course": "Vă rugăm să furnizați numele celui mai bun curs pe care l-ați urmat."
    }
}

current_language = st.session_state.language
current_translations = translations[current_language]

st.title("Share your experience with e-learning platforms! 📚")


st.markdown("""
    <style>
    body {
        background-color: #f0f4ff;
    }
    .language-title {
        text-align: center;
        font-size: 28px;
        color: #1a237e;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
    }

    </style>
""", unsafe_allow_html=True)

if st.session_state.page == 1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='language-title'> Select your language</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>🌍🌎🌏</div>", unsafe_allow_html=True)
    st.markdown("<div class='language-title'> Alegeți limba preferată</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        button_ro = st.button("Română", use_container_width=True)
    with col2:
        button_en = st.button("English", use_container_width=True)

    if button_ro:
        st.session_state.language = "ro"
        st.session_state.countries = countries_for_language("ro")
        next_page()

    if button_en:
        st.session_state.language = "en"
        st.session_state.countries = countries_for_language("en")
        next_page()


elif st.session_state.page == 2:
    st.write(current_translations['intro'])

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("###")
        button_start = st.button(current_translations['start_button'], use_container_width=True)

    if button_start:
        next_page()

elif st.session_state.page == 3:
    with st.form(key="form_page1"):
        st.write("### Part 1: Personal Information")

        age = st.slider(current_translations['age'], 0, 100)
        st.session_state.age = age

        gender = st.radio(current_translations['gender'],
                          current_translations["gender_list"])

        country_list = [country[1] for country in st.session_state.countries]
        country = st.selectbox(current_translations['country'], country_list)
        st.session_state.country = country

        education_list = ["Middle School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"]
        education = st.selectbox(current_translations['education'], education_list)
        st.session_state.education = education

        next_button = st.form_submit_button(label=current_translations['next_button'])

        if next_button:    
            next_page()

elif st.session_state.page == 4:
    st.write("### Part 2: Your E-learning Experience")

    platforms = ["Coursera", "Udemy", "edX", "LinkedIn Learning", "Khan Academy", "My university's platform",
                 "Youtube", "TikTok", "Other"]
    
    selected_platforms = st.multiselect(
        current_translations['platforms'], platforms)
    
    if "Other" in selected_platforms:
        other_platform = st.text_input("Please specify the other platform(s) you use:",
                                       value=st.session_state.other_platform)
        if other_platform:  
            selected_platforms = [p for p in selected_platforms if p != "Other"]
            selected_platforms.append(other_platform)
    else:
        other_platform = ""
    
    st.write("Selected:", selected_platforms)

    course_types = ["Technical (Programming, Data Science)", "Business & Management",
                    "Personal Development", "Arts & Humanities", "Health & Medicine", "Other"]
    selected_courses = st.multiselect(
        current_translations['course_types'], course_types)
    
    if "Other" in selected_courses:
        other_course = st.text_input("Please specify the type of course:",
                                       value=st.session_state.other_course)
        if other_course:  
            selected_courses = [p for p in selected_courses if p != "Other"]
            selected_courses.append(other_course)
    else:
        other_course = ""

    requency = st.radio(current_translations['frequency'],
                              ["Daily", "A few times a week", "Once a week", "A few times a month", "Rarely"])

    st.write(current_translations['why_visit'])
    usage_options = ["Job Purposes", "Personal interest", "School purposes"]
    selected_usage = []
    for option in usage_options:
        if st.checkbox(option, value=(option in st.session_state.selected_usage)):
            selected_usage.append(option)  

    if "Job Purposes" in selected_usage:
        job = st.text_input(current_translations['job'], value=st.session_state.job)
        mandatory = st.radio("Is it mandatory to take online courses for your job?", ["Yes", "No"])
        promotion = st.radio("Do you think that taking online courses will help/helped you get a promotion?", ["Yes", "No"])
    else:
        job = ""
        mandatory = ""
        promotion = ""

    if "School purposes" in selected_usage:
        reasons = ["I only use my university's platform", "I want to learn extra", "I need extra information for my exams/papers",
                   "I don't understand from class", "Professors from online explain better",
                   "I don't go to classes"]
        st.session_state.selected_reasons = st.multiselect(
            current_translations['school_reasons'], reasons, default=st.session_state.selected_reasons
        )
        beforeClasses = st.radio(current_translations['check_lectures'], ["Yes", "No"])
        exams = st.radio(current_translations['check_exams'], ["All year long", "Exam session only"])

        st.write(current_translations['grade_before'])
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
        st.write(current_translations['grade_after'])
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
    
    learning_method = st.radio(current_translations['learning_method'],
                                ["Pre-recorded video courses", "Live online classes",
                                 "Text-based courses", "Interactive exercises & projects"])

    certification = st.radio(current_translations['certification'],
                              ["Very important", "Somewhat important", "Not important"])
    
    learning_preference = st.radio(
        current_translations['learning_preference'],
        ["Structured courses", "Short videos", "Both"])
    
    multitasking = st.radio(
        current_translations['multitasking'],
        ["Never", "Sometimes",  "Often", "Always"])
    
    notes = st.multiselect(
        current_translations['notes'],
        ["I don’t take notes", "Handwritten", "Digital (OneNote, Notion, etc.)", "Summaries", "Mind maps"])
    
    bestCourse = st.text_input(current_translations['best_course'] , value="")

    dropOut = st.radio(current_translations['dropOut'], ["Yes", "No"])
    if dropOut == "Yes":
        dropOutReason = st.radio(
        current_translations['dropOutReason'],
        ["Too hard", "Too boring", "No time", "Not useful", "Other"])
    
    completationRate = st.slider(current_translations['completion_rate'],
    0, 100, 50)

    preference = st.radio(current_translations['preference_onl'], 
                          ["Online", "Face-to-face"])
    
    st.write("### Would you try?")
    vr = st.radio(current_translations['vr'], 
                  ["Yes", "No"])
    liveInteraction = st.radio(current_translations['live_interaction'],
                  ["Yes", "No"])
    immersive = st.radio(current_translations['immersive'],
                  ["Yes", "No"])
    replacement = st.radio(current_translations['replacement'],
                  ["Yes", "No", "Hybride model will dominate", "Not sure"])
    aiAssistant = st.radio(current_translations['ai_assistant'],
                  ["Yes", "No"])
    aiProfessor = st.radio(current_translations['ai_professor'],
                  ["Yes", "No"])
    col1, col2 = st.columns(2)

    with col1:
        if st.button(label=current_translations['next_button']):
            st.session_state.selected_platforms = selected_platforms  
            st.session_state.selected_courses = selected_courses  
            st.session_state.selected_usage = selected_usage  
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

            if not st.session_state.selected_platforms:
                st.warning(current_translations['warning_platforms'])
            elif "Other" in st.session_state.selected_platforms and not st.session_state.other_platform.strip():
                st.warning(current_translations['warning_other_platform'])
            elif not st.session_state.selected_courses:
                st.warning(current_translations['warning_courses'])
            elif "Other" in st.session_state.selected_courses and not st.session_state.other_course.strip():
                st.warning(current_translations['warning_other_course'])
            elif not st.session_state.selected_usage:
                st.warning(current_translations['warning_usage'])
            elif "School purposes" in st.session_state.selected_usage:
                if not st.session_state.selected_reasons:
                    st.warning(current_translations['warning_reasons'])
                elif not grade_before or not max_grade_before or not grade_after or not max_grade_after:
                    st.warning(current_translations['warning_gpa'])
            elif "Job Purposes" in st.session_state.selected_usage:
                if not st.session_state.job.strip():
                    st.warning(current_translations['warning_job'])
                elif not st.session_state.mandatory.strip():
                    st.warning(current_translations['warning_mandatory'])
                elif not st.session_state.promotion.strip():
                    st.warning(current_translations['warning_promotion'])
            elif not st.session_state.notes:
                st.warning(current_translations['warning_notes'])
            elif not st.session_state.bestCourse.strip():
                st.warning(current_translations['warning_best_course'])
            
            else:
                next_page()

    with col2:
        if st.button(label=current_translations['back_button']):
            prev_page()




    




