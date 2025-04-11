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
    ("dropOutReason", None),
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
        "gender_list": ["Male", "Female", "Non-binary/Third gender", "Prefer not to say"],  
        "yes_no": ["Yes", "No"],  
        "exam_list": ["All year long", "Exam session only"],
        "school_reasons_list": ["I only use my university's platform", "I want to learn extra", "I need extra information for my exams/papers",
                       "I don't understand from class", "Professors from online explain better",
                       "I don't go to classes"],
        "frequency_list": ["Daily", "A few times a week", "Once a week", "A few times a month", "Rarely"],
        "next_button": "Next",
        "country": "Where are you from?",
        "education": "What is your highest level of education?",
        "education_list": ["Primary School", "Middle School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"],
        "intro": """
        This survey will help us understand how people use e-learning platforms and why.  
        There are **3 different parts** to this survey:
        1. **Personal Information**
        2. **Your learning experience before and after starting using e-learning**
        3. **Design your own e-learning course** 

        It will not take more than 5-7 minutes to complete the survey.
        """,
        "start_button": "🚀 Let's get started!",
        "part1": "**Part 1: Personal Information**",	
        "part2": "**Part 2: Your learning experience.**\n\n"
        "✨ Please consider e-learning any online platform that provides educational information.",
        "part3": "**Part 3: Design your own e-learning course.**\n\n",
        "platforms": "Please select the e-learning platforms you use:",
        "specify_platform": "Please specify the other platforms you use:",
        "course_types": "Please select the types of courses you take:",
        "course_types_list": ["Technical (Programming, Data Science)", "Business & Management", "Finance & Economics", 
                              "Linguistics & Foreign Languages", "Psychology & Human Behavior", "Emerging Technologies (AI, Blockchain, etc.)", 
                              "Environment & Sustainability", "Design & Graphics", "Travel & Tourism", 
                              "Entrepreneurship", "Personal Development", "Arts & Humanities", "Health & Medicine", 
                              "Sports Activities", "Childcare & Family Life", "Others"],
        "specify_course": "Please specify the other courses you take:",
        "frequency": "How often do you visit e-learning platforms?",
        "purpose_list": ["Job Purposes", "Personal interest", "School purposes"],
        "learning_method_list": ["Pre-recorded videos", "Live online classes",
                                    "Podcasts",
                                    "Text-based courses", "Interactive exercises & projects"],
        "why_visit": "Why do you visit e-learning platforms?",
        "job": "What is your current job title?",
        "mandatory_courses": "Are these courses mandatory for your job?",
        "promotion_courses": "Do you think that online courses helped/will help you to get a promotion?",
        "school_reasons": "Why do you use e-learning for school purposes?",
        "check_lectures": "Do you check the course materials before classes?",
        "check_exams": "How often do you refer to e-learning materials for exams?",
        "your_grade_after": "Your grade:",
        "your_grade_before": "Your grade:",
        "out_of_after": "Out of:",
        "out_of_before": "Out of:",
        "grade_before": "What was your GPA before using e-learning?",
        "max_grade_before": "What is the maximum grade you could achieve?",
        "grade_after": "What is your GPA after using e-learning?",
        "max_grade_after": "What is the maximum grade you could achieve?",
        "payed_courses": "Do you take paid courses?",
        "payment": "How much are you willing to pay for an online course? (in EURO)",
        "learning_method": "What learning method do you prefer?",
        "certification": "How important is getting a certification?",
        "certification_list": ["Not important", "Somewhat important", "Very important"],
        "learning_preference": "Do you prefer structured courses or short videos?",
        "multitasking": "How often do you multitask while learning?",
        "multitasking_list": ["Never", "Sometimes",  "Often", "Always"],
        "notes": "What kind of notes do you take during learning?",
        "notes_list": ["I don’t take notes", "Handwritten", "Digital (OneNote, Notion, etc.)", "Summaries", "Mind maps"],
        "best_course": "What is the best course you’ve taken? (it could be the name, a short description, or a link)",  
        "dropOut": "Have you ever dropped out of an online course?",
        "dropOutReason": "What was the reason you dropped out?",
        "dropOutReason_list": ["Too hard", "Too boring", "No time", "Not useful", "Other"],
        "completion_rate": "What is your typical course completion rate? (in case you watch only short videos, how much of the video do you watch?)",
        "preference_onl": "Do you prefer online learning or face-to-face learning?",
        "preference_onl_list": ["Online", "Face-to-face"],
        "vr": "Would you be interested in using virtual reality for learning?",
        "live_interaction": "Would you like to have live interactions with instructors?",
        "immersive": "Would you be interested in immersive learning experiences?",
        "replacement": "Do you think AI will replace traditional professors?",
        "replacement_list": ["Yes", "No", "Hybrid model will dominate", "Not sure"],
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
        "warning_best_course": "Please provide the name of the best course you've taken.",
        "warning_dropOut": "Please specify the reason for dropping out.",

        "about1" : "What do you think about e-learning already existing materials about", 
        "about2" : "? Are they enough? Are you satisfiend with the online information you can find about this topic?",
        "scenario_tehnical": "Imagine you are learning Python programming. You start with basic syntax, then move on to data structures and algorithms. After completing the course, you can apply your skills by creating software applications or analyzing big data.",
        "Business & Management": "You are studying management theories and real-world business scenarios. You participate in group projects and learn how to manage teams, understand financial reports, and make strategic decisions for a company. This type of course prepares you for leadership roles in organizations.",
        "scenario_personal": "You are learning skills for personal growth, such as time management, emotional intelligence, and effective communication. After completing this course, you can improve your personal and professional relationships, manage stress, and achieve your personal goals.",
        "scenario_arts": "You are exploring history, philosophy, literature, and other creative subjects. You engage in discussions, read classic books, and participate in creative writing or art projects. These courses foster creativity and critical thinking while giving you a deeper understanding of human culture.",
        "scenario_health": "You're studying anatomy, healthcare management, or public health. You could be learning how to care for patients, manage healthcare organizations, or conduct health research. These courses prepare you to contribute to healthcare and improve the quality of life for individuals and communities.",
        "scenario_other": "You are learning about various subjects that don't fit into the above categories. This could include niche topics, hobbies, or interdisciplinary studies. These courses allow you to explore your interests and expand your knowledge in unique ways.",
        "characters" : "maximum 1000 characters"
    },
        "ro": {
        "age": "Ce varsta ai?",
        "gender": "Care este sexul tău?",
        "gender_list": ["Masculin", "Feminin", "Non-binary", "Prefer să nu spun"],
        "yes_no": ["Da", "Nu"],
        "exam_list": ["Pe tot parcursul anului", "Doar in sesiune/in perioada testelor"],	
        "school_reasons_list": ["Folosesc doar platforma universitatii/scolli (Moodle)", "Vreau sa invat in plus", "Am nevoie de informatii suplimentare pentru examene/lucrari",
                       "Nu inteleg din clasa", "Profesorii de online explica mai bine",
                       "Nu merg la cursuri/ore"],
        "frequency_list": ["Zilnic", "De cateva ori pe saptamana", "O data pe saptamana", "De cateva ori pe luna", "Rareori"],
        "learning_method_list": ["Videoclipuri pre-înregistrate", "Cursuri online live", "Podcast-uri",
                                    "Cursuri text", "Exercitii interactive & proiecte"],
        "next_button": "Următorul",
        "country": "In ce tara locuiesti?",
        "education": "Care este ultimul nivel de educație pe care l-ai obținut?",
        "education_list": ["Scoala Primara", "Scoala Generala", "Liceu", "Licenta", "Master", "Doctorat"],
        "intro": """
        Acest chestionar ne va ajuta să înțelegem cum se folosesc platformele de învățare online și de ce.
        Toate raspunsurile sunt anonime și vor fi folosite doar în scopuri de cercetare.  
        Există **3 părți** în acest chestionar:
        1. **Informații personale**
        2. **Experiența de învățare înainte și după utilizarea platformelor e-learning**
        3. **Devino propirul creator de cursuri online**

        Nu va dura mai mult de 5-7 minute pentru a completa chestionarul.
        """,
        "start_button": "🚀 Să începem!",
        "part1" : "**Partea 1: Informații personale**",
        "part2" : "**Partea 2: Experiența ta de învățare.** \n\n" 
        " ✨ Vom considera e-learning orice platforma online care ofera informatii educative. " , 
        "part3" : "**Partea 3: Devino propirul creator de cursuri online.**\n\n",
        "platforms": "Selecteaza platformele de e-learning pe care le folosesti (alege-le pe toate):",
        "specify_platform": "Te rog sa specifici ce alte platforme folosesti:",
        "course_types": "Selecteaza ce fel de cursuri urmaresti:",
        "course_types_list": ["Tehnic (Programare, Data Science)", "Business & Management", "Finante & Economie",
                              "Lingvistica & Limbi Straine", "Psihologie & Comportament Uman", 
                              "Tehnologii Emergente (AI, Blockchain, etc.)", "Mediu & Sustenabilitate", "Design & Grafica", 
                              "Calatorii & Turism", "Antreprenoriat", 
                              "Dezvoltare Personala", "Arta & Stiinte Umaniste", "Sanatate & Medicina", 
                              "Activitati Sportive",
                              "Ingrijirea copilului si viata de familie",  "Altele"],
        "specify_course": "Te rog sa specifici alte cursuri urmezi:",
        "frequency": "Cât de des utilizezi platformele de e-learning?", 
        "why_visit": "Care este motivul pentru care folosesti e-learnig-ul?",
        "purpose_list": ["Locul de munca", "Interes personal", "Scoala"],
        "job": "Ce ocupatie ai?",
        "mandatory_courses": "Cursuri online sunt obligatorii pentru locul de muncă?",
        "promotion_courses": "Credeti ca multumita cursurilor online ati obtiut/veti obtine o promovare?",
        "school_reasons": "Care este motivul pentru care urmaresti cursuri online pentru scoala?",
        "check_lectures": "Verifici materialele postate de profesori înainte de a fi predate?",
        "check_exams": "Cât de des consulti cursurile/lectiile postate de profesorii tai online?",
        "grade_before": "Care a fost media notelor tale înainte de a folosi e-learning-ului?",
        "your_grade_before": "Media notelor tale (inainte de utilizarea e-learning-ului):",
        "your_grade_after": "Media notelor tale: (dupa utilizarea e-learning-ului)",
        "out_of_before": "Din (media maxima ce poate fi obtinuta, inainte de utlizarea e-learning-ului):",
        "out_of_after": "Din (media maxima ce poate fi obtinuta, dupa utlizarea e-learning-ului):",
        "max_grade_before": "Care este media maximă a notelor pe care ai putea să o obții?",
        "grade_after": "Care este media notelor tale după utilizarea e-learning-ului?",
        "max_grade_after": "Care este media maximă a notelor pe care ai putea să o obții?",
        "learning_method": "Ce fel de cursuri online preferi?",
        "certification": "Cât de importantă este obținerea unui certificat dupa finalizarea unui curs online?",
        "certification_list": ["Nu este deloc important", "Este important", "Este foarte important"],	
        "payed_courses": "Majoritatea cursurilor pe care le urmezi sunt platite?",
        "payment": "Cât de mult ești dispus să plătești pentru un curs online? (in RON)",
        "multitasking": "Cat de des faci si alte activitati (multitasking) in timp ce urmaresti un curs online?",
        "multitasking_list": ["Niciodata", "Uneori",  "Adesea", "Intotdeauna"],
        "notes": "Ce tip de notițe iei în timpul cursurilor online?",
        "notes_list": ["Nu iau notite", "Scrise de mana", "Digitale (OneNote, Notion, etc.)", "Rezumate", "Mind maps"],
        "best_course": "Care este cel mai folositor curs pe care l-ai urmat? (poate fi numele, o scurta descriere sau link-ul)",
        "dropOut": "Ați renunțat vreodată la un curs online dupa ce l-ati inceput?",
        "dropOutReason": "Care a fost motivul?",
        "dropOutReason_list": ["Prea greu", "Prea plictisitor", "Nu am timp", "Nu este util", "Altul"],
        "completion_rate": "Ce procent reusesti sa finalizezi de obicei dintr-un curs? "
        "(in cazul in care urmaresti doar videoclipuri scurte, la cat la suta din videoclip te uiti?)",
        "preference_onl": "Preferi învățarea online sau față în față?",
        "preference_onl_list": ["Online", "In persoana"],
        "vr": "Ați fi interesat să folosiți realitatea virtuală pentru învățare? /n/n"
        "exemplu: cursuri de gatit in care sa poti interactiona cu bucataria virtuala",
        "live_interaction": "Ați dori să aveți interacțiuni live cu profesorii?",
        "immersive": "Ați fi interesat de experiențe de învățare imersive? /n/n"
        "exemplu: cursuri de istorie in care sa poti interactiona cu personajele istorice",
        "replacement": "Credeți că inteligenta artificala va înlocui profesorii tradiționali?",
        "replacement_list": ["Da", "Nu", "Model hibrid va domina", "Nu sunt sigur"],
        "ai_assistant": "Ați folosi un asistent de inteligenta articiala pentru învățare? /n/n "
        "exemplu: un chatbot care să răspundă la întrebările tale despre cursuri",
        "ai_professor": "Ați accepta sa ai ca profesor o inteligenta artificiala?",
        "back_button": "Înapoi",
        "warning_platforms": "Te rog sa selectezi cel puțin o platformă.",
        "warning_other_platform": "Ai selectat ca folosesti alte platforme decat cele mentionate, te rog sa le specifici.",
        "warning_courses": "Te rog sa selectezi cel puțin un tip de curs.",
        "warning_other_course": "Ai selectat ca urmaresti alte tipuri de cursuri decat cele mentionate, te rog sa le specifici.",
        "warning_usage": "Te rog sa selectezi cel puțin o opțiune de utilizare.",
        "warning_reasons": "Te rog sa selectezi cel puțin un motiv pentru utilizarea e-learning pentru scopuri școlare.",
        "warning_gpa": "Te rog sa completezi atât media notelor înainte, cât și după utilizarea e-learning.",
        "warning_job": "Te rog sa precizezi care este locul tau de munca.",
        "warning_mandatory": "Te rog să precizezi dacă cursurile sunt obligatorii pentru locul dumneavoastră de muncă.",
        "warning_promotion": "Te rog să precizezi cum consideri ca te vor ajuta/te-au ajutat cursurile online pentru o promovare.",
        "warning_notes": "Te rog să precizezi cel puțin o metodă prin care iei notițe.",
        "warning_best_course": "Te rog să precizezi numele, o scurta descriere sau link-ul celui mai folositor curs pe care l-ai urmat.",
        "warning_dropOut": "Te rog să precizezi de ce ai renuntat la cursuri online in trecut.",
        "about1": "Ce părere ai despre materialele de e-learning deja existente despre",
        "about2": "? Consideri ca sunt suficiente? Ești mulțumit(ă) de informațiile online pe care le poți găsi despre acest subiect?",
        "Tehnic (Programare, Data Science)": """Ești responsabil de crearea unui curs online pentru un limbaj de programare nou, numit **Xylon**, 
            folosit în Data Science și dezvoltarea de aplicații. \n\n
            Cursul va acoperi atât concepte fundamentale, cât și tehnici avansate. 
            💻 Ce module ai considera esențiale pentru a înțelege pe deplin acest limbaj? \n\n
            💻 Ar trebui să începi cu fundamentele sintaxei Xylon, să înveți cum să gestionezi datele folosind biblioteci precum XyData
            sau să explorezi metode avansate de procesare a datelor cu XyML? \n\n
            💻 Care ar fi pașii esențiali pentru a deveni un profesionist în Xylon?""",
        "Finante & Economie": """Ești responsabil de crearea unui curs online despre Finanțe și Economie, destinat celor care vor să înțeleagă cum să își gestioneze mai bine finanțele personale și să dobândească cunoștințe fundamentale despre economie. \n\n
            Cursul ar trebui să fie accesibil și util pentru oricine, indiferent de nivelul de cunoștințe. \n\n
            💰 Ce module ai include pentru a ajuta participanții să înțeleagă concepte financiare importante, cum ar fi economisirea, investițiile, bugetarea și gestionarea datoriilor? \n\n
            💰 Ar trebui să începi cu noțiuni de bază despre funcționarea piețelor financiare, impactul inflației sau managementul riscurilor financiare? \n\n
            💰 Care ar fi pașii esențiali pentru a-i ajuta să își construiască un plan financiar personalizat, adaptat scopurilor și situației lor economice?""",
        "Business & Management": """Ești responsabil de crearea unui curs online pentru un domeniu de Business & Management. 
            Cursul va acoperi atât concepte fundamentale, cât și tehnici avansate. 
            💡 Ce module ai include pentru a înțelege acest domeniu? \n\n
            💡 Ar trebui să începi cu fundamentele managementului, să înveți despre strategii de marketing și dezvoltare de afaceri, sau să explorezi teme avansate precum managementul financiar și leadership-ul organizațional? 
            💡 Care ar fi pașii esențiali pentru a deveni un profesionist în Business & Management?""",
        "Lingvistica & Limbi Straine" : """Ești responsabil de crearea unui curs online destinat celor care doresc să își îmbunătățească abilitățile lingvistice în limba spaniola, la un nivel mediu. \n\n
            Cursul ar trebui să fie accesibil și util pentru persoanele care au deja niste cunostinte de vocabular si gramatica, cu un accent pe avansarea la un nivel intermediar. \n\n
            🗣️ Ce module ai include pentru a ajuta participanții să își îmbunătățească vocabularul si să înțeleagă structurile gramaticale? \n\n
            🗣️ Ar trebui să începi cu noțiuni despre diferențele între limbajul formal și informal sau altele sunt bazele? \n\n
            🗣️ Care ar fi pașii esențiali pentru a-i sprijini să își construiască un plan de învățare personalizat?""",
        "Psihologie & Comportament Uman": """Ești responsabil de crearea unui curs online despre Psihologie și Comportament Uman, destinat celor care vor să înțeleagă mai bine comportamentele și procesele mentale ale oamenilor. \n\n
            Cursul ar trebui să fie accesibil celor care nu au cunoștințe avansate, dar vor să învețe concepte fundamentale ale psihologiei. \n\n
            🧠 Cum ai structura cursul pentru a fi clar și ușor de înțeles pentru toți participanții? \n\n
            🧠 Ce tipuri de materiale și activități ai include pentru a ajuta participanții să învețe eficient? \n\n
            🧠 Cum ai integra diversele concepte ale psihologiei pentru a le arăta participanților cum pot aplica aceste informații în viața lor de zi cu zi?""",
        "Tehnologii Emergente (AI, Blockchain, etc.)": """Ești responsabil de crearea unui curs online despre Inteligența Artificială (AI), destinat celor care vor să înțeleagă cum funcționează aceste tehnologii și cum pot fi aplicate în diverse domenii. \n\n
            Cursul va acoperi concepte fundamentale, cum ar fi învățarea automată și rețelele neuronale. \n\n
            🤖 Cum ai organiza cursul pentru a introduce progresiv concepte complexe, asigurându-te că participanții pot înțelege pas cu pas? \n\n
            🤖 Cum ai structura lecțiile pentru a include atât teorie, cât și aplicații practice? \n\n
            🤖 Ce tipuri de activități interactive sau exemple din viața reală ai integra pentru a ajuta participanții să aplice cunoștințele acumulate în contextul profesional?""",


        "Arta & Stiinte Umaniste": """Imaginați-ți că ești responsabil de crearea unui curs online despre Arta din muzee, destinat amatorilor care doresc să înțeleagă și să aprecieze lucrările expuse. 
            Cursul va explora capodoperele și istoria artei din diverse perioade. \n\n
            🎨 Ce module ai include pentru a ajuta participanții să înțeleagă contextul și importanța lucrărilor din muzee? \n\n
            🎨 Ar trebui să începi cu o introducere în cele mai celebre muzee și colecțiile lor, să explorezi stilurile artistice specifice fiecărei perioade istorice, sau să înveți cum să interpretezi lucrările de artă, începând cu cele mai accesibile și cunoscute? \n\n
            🎨 Care ar fi pașii esențiali pentru a încuraja participanții să aprecieze arta în muzee într-un mod personal și captivant?""", 
        "Sanatate & Medicina": """Ești responsabil de crearea unui curs online despre Sănătate, destinat celor care vor să adopte un stil de viață echilibrat. \n\n
            Cursul ar trebui să fie accesibil și util pentru oricine, indiferent de nivelul de cunoștințe. \n\n 
            🩺 Ce module ai include pentru a ajuta participanții să își îmbunătățească sănătatea? \n\n 
            🩺 Ar trebui să începi cu noțiuni de bază despre alimentație echilibrată, importanța mișcării zilnice, tehnici de gestionare a stresului sau obiceiuri sănătoase pentru somn? \n\n 
            🩺 Care ar fi pașii esențiali pentru a-i sprijini să își creeze propriul plan de sănătate și bunăstare, adaptat nevoilor lor?""",
        "Altele": """Inveti despre diverse subiecte. Acest lucru ar putea include subiecte de nișă, hobby-uri sau studii interdisciplinare. \n\n 
            Aceste cursuri îți permit să explorezi interesele și să îți extinzi cunoștințele în moduri unice. \n\n
            🎀 Cum ar trebui un profesor sa-si atraga cursantii? Sau un influencer care te invata ceva? \n\n
            🎀 Cum ar trebui sa fie cursul/videoclipul? 
            🎀 Cat de lung ti-ar placea sa fie si ce informatii sa contina? """,
        "characters" : "maxim 1000 de caractere"
    }
}

current_language = st.session_state.language
current_translations = translations[current_language]
platforms = ["Coursera", "Udemy", "edX", "LinkedIn Learning", "Khan Academy", "My university's platform",
                     "Youtube", "TikTok", "Other"]

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
    st.write(current_translations['part1'])
    age = st.slider(current_translations['age'], 0, 100)
    st.session_state.age = age
    gender = st.radio(current_translations['gender'],
                      current_translations["gender_list"])
    country_list = [country[1] for country in st.session_state.countries]
    country = st.selectbox(current_translations['country'], country_list)
    st.session_state.country = country
    education = st.selectbox(current_translations['education'], current_translations["education_list"])
    st.session_state.education = education

    with st.form(key="form_page1"):
        next_button = st.form_submit_button(label=current_translations['next_button'])

        if next_button:    
            next_page()

elif st.session_state.page == 4:
    st.markdown(current_translations['part2'])

    selected_platforms = st.multiselect(
        current_translations['platforms'], platforms)
    if "Other" in selected_platforms or "Altele" in selected_platforms: 
        other_platform = st.text_input(current_translations['specify_platform'],
                                       value=st.session_state.other_platform)
        if other_platform.strip():
            selected_platforms = [p for p in selected_platforms if p != "Other"]
            selected_platforms.append(other_platform)
        else:
            st.error(current_translations['warning_other_platform'])
    else:
        other_platform = ""
    st.write("Selected:", selected_platforms)


   
    selected_courses = st.multiselect(
        current_translations['course_types'], current_translations["course_types_list"])
    if "Other" in selected_courses or "Altele" in selected_courses:
        other_course = st.text_input(current_translations['specify_course'],
                                       value=st.session_state.other_course)
        if other_course.strip():
            selected_courses = [p for p in selected_courses if p != "Other"]
            selected_courses.append(other_course)
        else:
            st.error(current_translations['warning_other_course'])
    else:
        other_course = ""
    
    st.write("Selected:", selected_courses)

    preference = st.radio(current_translations['preference_onl'], 
                              current_translations["preference_onl_list"])

    st.write(current_translations['why_visit'])

    if "selected_usage" not in st.session_state:
        st.session_state.selected_usage = []

    selected_usage = []


    for option in current_translations["purpose_list"]:
        if st.checkbox(option, value=(option in st.session_state.selected_usage), key=f"usage_{option}"):
            selected_usage.append(option)

    # st.session_state.selected_usage = selected_usage


    if "Job Purposes" in selected_usage or "Locul de munca" in selected_usage:
        col1, col2, col3 = st.columns([0.05, 0.9, 0.05])

        with col2:

            st.markdown("### 💼")

            job = st.text_input(
                current_translations['job'],
                value=st.session_state.job if 'job' in st.session_state else ""
            )

            mandatory = st.radio(
                current_translations["mandatory_courses"],
                current_translations["yes_no"],
                index=current_translations["yes_no"].index(st.session_state.mandatory)
                if 'mandatory' in st.session_state and st.session_state.mandatory in current_translations["yes_no"]
                else 0
            )

            promotion = st.radio(
                current_translations["promotion_courses"],
                current_translations["yes_no"],
                index=current_translations["yes_no"].index(st.session_state.promotion)
                if 'promotion' in st.session_state and st.session_state.promotion in current_translations["yes_no"]
                else 0
            )

            st.markdown("</div>", unsafe_allow_html=True)
    else:
        job = ""
        mandatory = ""
        promotion = ""



    if "School purposes" in selected_usage or "Scoala" in selected_usage:
        col1, col2, col3 = st.columns([0.05, 0.9, 0.05])

        with col2:
            st.markdown("### 🎓 ")

            reasons = st.multiselect(
                current_translations['school_reasons'],
                current_translations["school_reasons_list"],
                default=st.session_state.selected_reasons
            )

            beforeClasses = st.radio(
                current_translations['check_lectures'],
                current_translations["yes_no"]
            )

            exams = st.radio(
                current_translations['check_exams'],
                current_translations["exam_list"]
            )

            st.write(current_translations['grade_before'])
            col_a, col_b = st.columns(2)
            with col_a:
                grade_before = st.text_input(current_translations["your_grade_before"])
            with col_b:
                max_grade_before = st.text_input(current_translations["out_of_before"])

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
            col_c, col_d = st.columns(2)
            with col_c:
                grade_after = st.text_input(current_translations["your_grade_after"])
            with col_d:
                max_grade_after = st.text_input(current_translations["out_of_after"])

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

            st.markdown("</div>", unsafe_allow_html=True)

    else:
        reasons = []
        beforeClasses = None
        exams = None
        grade_before = None
        max_grade_before = None
        grade_after = None
        max_grade_after = None

    

    learning_method = st.radio(current_translations['learning_method'],
                                    current_translations["learning_method_list"])

    frequency = st.radio(current_translations['frequency'],
                          current_translations["frequency_list"])
    
    payed_courses = st.radio(
        current_translations['payed_courses'],
        current_translations["yes_no"],)
    if payed_courses == "Da":
        payment = st.slider(current_translations['payment'], 0, 10000, 100)
    if payed_courses == "Yes":
        payment = st.slider(current_translations['payment'], 0, 2000, 100)
    else:
        payment = 0
    bestCourse = st.text_input(current_translations['best_course'] , value="")
    dropOut = st.radio(current_translations['dropOut'], current_translations["yes_no"])
    if dropOut == "Yes" or dropOut == "Da":
        dropOutReason = st.radio(
        current_translations['dropOutReason'],
        current_translations["dropOutReason_list"])
    completationRate = st.slider(current_translations['completion_rate'],
    0, 100, 50)
    certification = st.radio(current_translations['certification'],
                            current_translations["certification_list"])

  
    notes = st.multiselect(
            current_translations['notes'],
            current_translations["notes_list"])
    
    multitasking = st.radio(
            current_translations['multitasking'],
            current_translations["multitasking_list"])
    
    st.write("### Would you try?")
    vr = st.radio(current_translations['vr'], 
                  current_translations['yes_no'])
    liveInteraction = st.radio(current_translations['live_interaction'],
                  current_translations['yes_no'])
    immersive = st.radio(current_translations['immersive'],
                  current_translations['yes_no'])
    replacement = st.radio(current_translations['replacement'],
                  current_translations["replacement_list"])
    aiAssistant = st.radio(current_translations['ai_assistant'],
                  current_translations['yes_no'])
    aiProfessor = st.radio(current_translations['ai_professor'],
                  current_translations['yes_no'])

    with st.form(key="form_navigation"):
        col1, col2, col3 = st.columns(3)
        with col1:
                next_button = st.form_submit_button("Next")
                if next_button:
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
                    if dropOut == "Yes":
                        st.session_state.dropOutReason = dropOutReason
                    else:
                        st.session_state.dropOutReason = None
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
                    elif "Yes" in st.session_state.dropOut:
                        if st.session_state.dropOutReason is None:
                            st.warning(current_translations['warning_dropOut'])
                    else:
                        next_page()
        with col3:
            back_button = st.form_submit_button(current_translations['back_button'])
            if back_button:
                prev_page()


elif st.session_state.page == 5:
    st.write(current_translations["part3"])

    if st.session_state.selected_courses:
        first_course = st.session_state.selected_courses

        category_str = ", ".join(first_course)

        st.write(f"{current_translations['about1']} {category_str} {current_translations['about2']}")
        st.text_area(current_translations["characters"], key="about_course")

        st.write({current_translations[category_str]})
    
    with st.form(key="form_submition"):
        col1, col2, col3 = st.columns(3)
        with col1:
            next_button = st.form_submit_button("Submit")
        with col2: 
            back_button = st.form_submit_button(current_translations['back_button'])
                
    
    
    if next_button:
        st.success("Form submitted successfully!")
        st.balloons()
    if back_button:
        prev_page()





    


    

