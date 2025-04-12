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
    ("check_lectures", None),
    ("check_exams", None),
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
    # ("preference", ""),
    ("vr", ""),
    ("liveInteraction", ""),
    ("immersive", ""),
    ("replacement", ""),
    ("aiAssistant", ""),
    ("aiProfessor", ""),
    ("about", ""),
    ("specific_course", ""),
    ("payed_courses", ""),
    ("payment", 0),
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
        "platforms_list" : ["Coursera", "Udemy", "edX", "LinkedIn Learning", "Khan Academy", "My university's platform",
                     "Youtube", "TikTok", "Others"],
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
        "multitasking": "How often do you multitask while learning?",
        "multitasking_list": ["Never", "Sometimes",  "Often", "Always"],
        "notes": "What kind of notes do you take during learning?",
        "notes_list": ["I don’t take notes", "Handwritten", "Digital (OneNote, Notion, etc.)", "Summaries", "Mind maps"],
        "best_course": "What is the best course you’ve taken? (it could be the name, a short description, or a link)",  
        "dropOut": "Have you ever dropped out of an online course?",
        "dropOutReason": "What was the reason you dropped out?",
        "dropOutReason_list": ["Too hard", "Too boring", "No time", "Not useful", "Others"],
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
        "warning_other_platform": "If 'Others' is selected, please specify the platform.",
        "warning_courses": "Please select at least one course type.",
        "warning_other_course": "If 'Others' is selected, please specify the course type.",
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
                "Technical (Programming, Data Science)": ("You are responsible for creating an online course about a new programming language called Xylon, used in Data Science and application development.\n\n"
            "💻 How would you structure this course to cover both the basic and advanced concepts related to programming in Xylon?\n\n"
            "💻 What methods or interactive elements would you include to make the course engaging and easy to follow for participants?\n\n"
            "💻 What are the essential aspects participants should master to effectively apply Xylon in real-world Data Science projects?"),

        "Business & Management": ("You are responsible for creating an online course in Business & Management.\n\n"
            "💼 How would you structure this course to provide both foundational knowledge and advanced strategies in Business & Management?\n\n"
            "💼 What interactive methods or activities would you include to keep the course engaging and help participants retain the information?\n\n"
            "💼 What are the key skills participants need to develop to excel in Business & Management?"),

        "Finance & Economics": ("You are responsible for creating an online course in Finance & Economics, aimed at helping people understand personal finance management and acquire basic economic knowledge.\n\n"
            "💰 How would you structure this course to cover the fundamentals of finance and economics?\n\n"
            "💰 What engaging elements or methods would you incorporate to make the course interesting and practical for the participants?\n\n"
            "💰 What are the essential financial and economic concepts participants should master to manage their personal finances effectively?"),

        "Linguistics & Foreign Languages": ("You are responsible for creating an online course aimed at improving intermediate Spanish language skills.\n\n"
            "🗣️ How would you structure this course to cover grammar and vocabulary effectively for intermediate learners?\n\n"
            "🗣️ What interactive techniques or activities would you include to make the learning process engaging and practical for the participants?\n\n"
            "🗣️ What are the key aspects of Spanish language learning that participants need to focus on to become fluent at an intermediate level?"),

        "Psychology & Human Behavior": ("You are responsible for creating an online course in Psychology & Human Behavior, aimed at helping participants understand human mental processes and behaviors.\n\n"
            "🧠 How would you structure this course to cover the fundamentals of psychology and human behavior?\n\n"
            "🧠 What engaging methods or activities would you use to make the course interactive and easier for participants to understand?\n\n"
            "🧠 What are the essential concepts of psychology that participants should master to apply in real-life scenarios?"),

        "Emerging Technologies (AI, Blockchain, etc.)": ("You are responsible for creating an online course about Artificial Intelligence (AI), aimed at helping participants understand its concepts and applications in various fields.\n\n"
            "🤖 How would you structure this course to progressively introduce complex concepts such as machine learning and neural networks?\n\n"
            "🤖 What interactive elements or real-world examples would you include to make the course engaging and applicable for participants?\n\n"
            "🤖 What are the key skills participants should acquire to apply AI techniques effectively in different industries?"),

        "Environment & Sustainability": ("You are responsible for creating an online course about Environmental Sustainability, aimed at raising awareness and teaching practical solutions for sustainability.\n\n"
            "🌱 How would you structure this course to cover both environmental science and sustainable practices?\n\n"
            "🌱 What interactive or practical elements would you include to make the course engaging and applicable for real-world sustainability solutions?\n\n"
            "🌱 What are the key concepts participants need to master to implement sustainable practices in their personal and professional lives?"),

        "Design & Graphics": ("You are responsible for creating an online course in Design & Graphics, aimed at developing visual design skills.\n\n"
            "🎨 How would you structure this course to teach both the basics and advanced techniques in design?\n\n"
            "🎨 What creative methods or hands-on activities would you include to make the course engaging and practical for participants?\n\n"
            "🎨 What are the key skills participants should develop to become proficient in graphic design?"),

        "Travel & Tourism": ("You are responsible for creating an online course about Travel & Tourism, aimed at those interested in exploring the tourism industry and travel management.\n\n"
            "🌍 How would you structure this course to provide essential knowledge about the travel and tourism industry?\n\n"
            "🌍 What interactive elements or activities would you incorporate to make the course engaging and helpful for aspiring professionals?\n\n"
            "🌍 What are the key aspects of the tourism industry that participants should master to succeed in this field?"),

        "Entrepreneurship": ("You are responsible for creating an online course about Entrepreneurship, aimed at helping individuals start and manage their own businesses.\n\n"
            "🚀 How would you structure this course to cover the foundational principles of entrepreneurship?\n\n"
            "🚀 What engaging elements or methods would you include to make the course interactive and insightful for participants?\n\n"
            "🚀 What are the key entrepreneurial skills that participants should develop to launch and grow a successful business?"),

        "Personal Development": ("You are responsible for creating an online course in Personal Development, aimed at helping individuals improve their skills and mindset.\n\n"
            "🌟 How would you structure this course to address key aspects of personal growth and self-improvement?\n\n"
            "🌟 What techniques or activities would you incorporate to make the course engaging and practical for participants?\n\n"
            "🌟 What are the essential skills or traits participants need to cultivate for personal and professional growth?"),

        "Arts & Humanities": ("You are responsible for creating an online course about Art History, aimed at helping participants appreciate and understand the significance of artwork in museums.\n\n"
            "🎨 How would you structure this course to cover the history of art and key movements?\n\n"
            "🎨 What interactive or hands-on elements would you include to make the course engaging and enjoyable for participants?\n\n"
            "🎨 What are the key artistic concepts participants should understand to interpret and appreciate art in museums?"),

        "Health & Medicine": ("You are responsible for creating an online course about Health and Medicine, aimed at promoting a balanced and healthy lifestyle.\n\n"
            "🩺 How would you structure this course to cover fundamental health concepts and wellness practices?\n\n"
            "🩺 What engaging methods or activities would you incorporate to make the course practical and interactive for participants?\n\n"
            "🩺 What are the key health habits or concepts that participants should master to improve their overall well-being?"),

        "Sports Activities": ("You are responsible for creating an online course about Sports Activities, aimed at promoting physical fitness and sports knowledge.\n\n"
            "🏅 How would you structure this course to teach participants essential sports skills and fitness practices?\n\n"
            "🏅 What interactive or hands-on activities would you include to make the course engaging and enjoyable for participants?\n\n"
            "🏅 What are the key fitness or sports skills that participants should develop to lead a healthy, active lifestyle?"),

        "Childcare & Family Life": ("You are responsible for creating an online course about Childcare and Family Life, aimed at helping parents and caregivers improve their skills.\n\n"
            "👶 How would you structure this course to cover fundamental childcare and family life skills?\n\n"
            "👶 What engaging methods or activities would you include to make the course interactive and practical for parents?\n\n"
            "👶 What are the key aspects of parenting and family life that participants should master to foster a healthy family environment?"),

        "Others": ("You are responsible for creating an online course about various niche topics. These could range from hobbies to interdisciplinary studies.\n\n"
            "🎀 How would you structure this course to allow participants to explore unique interests and expand their knowledge?\n\n"
            "🎀 What engaging elements or activities would you include to make the course interesting and practical for participants?\n\n"
            "🎀 What are the key skills or concepts that participants should focus on to gain a comprehensive understanding of the topic?"),

        "characters_about" : "maximum 1000 characters",
        "characters_course" : "200 - 1000 characters",
        "min_200" : "Please write at least 200 characters.",
        "max_1000" : "Please write a maximum of 1000 characters.",
        "requirement_length" : "Please write about the course creation in at least 200 characters and a maximum of 1000 characters.",
        "send_form" : "Thank you for the answers! Soon you'll see some charts about them!"

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
        "platforms_list" : ["Coursera", "Udemy", "edX", "LinkedIn Learning", "Khan Academy", "My university's platform",
                     "Youtube", "TikTok", "Altele"],
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
        "Tehnic (Programare, Data Science)": (
            "Ești responsabil de crearea unui curs online despre un limbaj de programare nou, numit Xylon, folosit în Data Science și dezvoltarea de aplicații.\n\n"
            "💻 Cum ai structura acest curs pentru a acoperi atât conceptele de bază, cât și cele avansate legate de programarea în Xylon?\n\n"
            "💻 Ce metode sau elemente interactive ai include pentru a face cursul captivant și ușor de urmărit pentru participanți?\n\n"
            "💻 Care sunt aspectele esențiale pe care participanții ar trebui să le stăpânească pentru a aplica eficient Xylon în proiecte reale de Data Science?"
        ),

        "Business & Management": (
            "Ești responsabil de crearea unui curs online pentru domeniul Business & Management.\n\n"
            "💡 Cum ai structura acest curs pentru a acoperi atât concepte fundamentale, cât și tehnici avansate de management?\n\n"
            "💡 Ce metode interactive ai folosi pentru a face cursul mai atractiv și mai relevant pentru participanți?\n\n"
            "💡 Care sunt abilitățile esențiale pe care participanții trebuie să le dezvolte pentru a deveni lideri de succes în domeniul business-ului?"
        ),

        "Finante & Economie": (
            "Ești responsabil de crearea unui curs online despre Finanțe și Economie, destinat celor care vor să își îmbunătățească gestionarea finanțelor personale.\n\n"
            "💰 Cum ai structura acest curs pentru a include atât concepte financiare fundamentale, cât și aspecte mai avansate de economie?\n\n"
            "💰 Ce elemente interactive ai adăuga pentru a ajuta participanții să aplice cunoștințele financiare în viața lor de zi cu zi?\n\n"
            "💰 Care sunt pașii esențiali pe care participanții trebuie să îi urmeze pentru a-și construi un plan financiar personalizat?"
        ),

        "Lingvistica & Limbi Straine": (
            "Ești responsabil de crearea unui curs online pentru învățarea limbii spaniole la un nivel intermediar.\n\n"
            "🗣️ Cum ai structura acest curs pentru a acoperi atât vocabularul esențial, cât și structurile gramaticale avansate?\n\n"
            "🗣️ Ce activități interactive ai adăuga pentru a ajuta participanții să învețe mai rapid și să aplice corect limba?\n\n"
            "🗣️ Care sunt pașii esențiali pentru a ajuta participanții să își îmbunătățească abilitățile de conversație și să înțeleagă nuanțele limbii?"
        ),

        "Psihologie & Comportament Uman": (
            "Ești responsabil de crearea unui curs online despre Psihologie și Comportament Uman, destinat celor care vor să înțeleagă mai bine comportamentele umane.\n\n"
            "🧠 Cum ai structura acest curs pentru a acoperi atât concepte fundamentale ale psihologiei, cât și teme avansate despre comportamentele umane?\n\n"
            "🧠 Ce activități interactive ai adăuga pentru a face cursul mai captivant și mai ușor de înțeles?\n\n"
            "🧠 Care sunt pașii esențiali pe care participanții trebuie să îi urmeze pentru a aplica cunoștințele de psihologie în viața lor personală și profesională?"
        ),

        "Tehnologii Emergente (AI, Blockchain, etc.)": (
            "Ești responsabil de crearea unui curs online despre Inteligența Artificială (AI), destinat celor care vor să înțeleagă aceste tehnologii emergente.\n\n"
            "🤖 Cum ai structura acest curs pentru a introduce concepte complexe treptat, astfel încât participanții să le înțeleagă pe măsură ce avansează?\n\n"
            "🤖 Ce activități interactive ai include pentru a face cursul mai captivant și aplicabil în domenii reale?\n\n"
            "🤖 Care sunt abilitățile esențiale pe care participanții trebuie să le dezvolte pentru a aplica tehnologiile AI în proiecte reale?"
        ),

        "Mediu & Sustenabilitate": (
            "Ești responsabil de crearea unui curs online despre Mediu și Sustenabilitate, destinat celor care vor să înțeleagă cum să protejeze planeta.\n\n"
            "🌍 Cum ai structura acest curs pentru a acoperi atât conceptele fundamentale ale ecologiei, cât și tehnici avansate de gestionare a resurselor naturale?\n\n"
            "🌍 Ce activități interactive ai adăuga pentru a ajuta participanții să aplice cunoștințele de sustenabilitate în viața lor de zi cu zi?\n\n"
            "🌍 Care sunt pașii esențiali pentru a încuraja participanții să își construiască un plan de acțiune pentru un stil de viață mai sustenabil?"
        ),

        "Design & Grafica": (
            "Ești responsabil de crearea unui curs online despre Design și Grafică, destinat celor care vor să învețe să creeze designuri vizuale de impact.\n\n"
            "🎨 Cum ai structura acest curs pentru a acoperi atât teorie, cât și aplicabilitatea designului în proiecte reale?\n\n"
            "🎨 Ce elemente interactive ai adăuga pentru a face procesul de învățare mai captivant și mai aplicabil?\n\n"
            "🎨 Care sunt abilitățile esențiale pe care participanții trebuie să le dezvolte pentru a crea designuri grafice profesioniste?"
        ),

        "Calatorii & Turism": (
            "Ești responsabil de crearea unui curs online despre Turism și Călătorii, destinat celor care vor să înțeleagă cum să planifice vacanțe și călătorii.\n\n"
            "✈️ Cum ai structura acest curs pentru a acoperi atât planificarea logistică a călătoriilor, cât și aspecte culturale ale destinațiilor?\n\n"
            "✈️ Ce activități interactive ai include pentru a ajuta participanții să își planifice vacanțele mai eficient?\n\n"
            "✈️ Care sunt pașii esențiali pentru a încuraja participanții să aleagă destinații de vacanță sustenabile și responsabile?"
        ),

        "Antreprenoriat": (
            "Ești responsabil de crearea unui curs online despre Antreprenoriat, destinat celor care vor să învețe cum să dezvolte o afacere de succes.\n\n"
            "🚀 Cum ai structura acest curs pentru a acoperi atât concepte fundamentale ale antreprenoriatului, cât și strategii avansate pentru a dezvolta o afacere?\n\n"
            "🚀 Ce metode interactive ai adăuga pentru a ajuta participanții să aplice rapid cunoștințele de antreprenoriat?\n\n"
            "🚀 Care sunt pașii esențiali pentru a ajuta participanții să dezvolte o strategie eficientă pentru afacerea lor?"
        ),

        "Dezvoltare Personala": (
            "Ești responsabil de crearea unui curs online despre Dezvoltare Personală, destinat celor care vor să își îmbunătățească abilitățile de viață.\n\n"
            "🌱 Cum ai structura acest curs pentru a acoperi atât aspecte fundamentale ale dezvoltării personale, cât și tehnici avansate pentru creșterea personală?\n\n"
            "🌱 Ce activități interactive ai adăuga pentru a ajuta participanții să aplice cunoștințele de dezvoltare personală?\n\n"
            "🌱 Care sunt pașii esențiali pe care participanții trebuie să îi urmeze pentru a dezvolta obiceiuri sănătoase și eficiente în viața lor?"
        ),

        "Arta & Stiinte Umaniste": (
            "Ești responsabil de crearea unui curs online despre Artă și Științe Umaniste, destinat celor care vor să înțeleagă cultura și istoria umană.\n\n"
            "🎨 Cum ai structura acest curs pentru a acoperi atât istoria artei, cât și impactul cultural al diferitelor mișcări artistice?\n\n"
            "🎨 Ce activități interactive ai include pentru a ajuta participanții să aprecieze mai bine arta și cultura?\n\n"
            "🎨 Care sunt pașii esențiali pentru a încuraja participanții să aprecieze arta și științele umaniste în viața lor de zi cu zi?"
        ),

        "Sanatate & Medicina": (
            "Ești responsabil de crearea unui curs online despre Sănătate și Medicină, destinat celor care vor să învețe cum să își îmbunătățească starea de sănătate.\n\n"
            "🩺 Cum ai structura acest curs pentru a include atât aspecte fundamentale ale sănătății, cât și metode avansate de prevenire a bolilor?\n\n"
            "🩺 Ce activități interactive ai adăuga pentru a ajuta participanții să aplice cunoștințele de sănătate în viața lor de zi cu zi?\n\n"
            "🩺 Care sunt pașii esențiali pentru a încuraja participanții să își îmbunătățească stilul de viață și să prevină bolile?"
        ),

        "Activitati Sportive": (
            "Ești responsabil de crearea unui curs online despre Activități Sportive, destinat celor care vor să învețe să practice sporturi în mod eficient și sănătos.\n\n"
            "🏃 Cum ai structura acest curs pentru a include atât tehnici fundamentale, cât și metode avansate de antrenament sportiv?\n\n"
            "🏃 Ce metode interactive ai adăuga pentru a ajuta participanții să aplice cunoștințele de sport în antrenamentele lor?\n\n"
            "🏃 Care sunt pașii esențiali pentru a încuraja participanții să își construiască un program de antrenament personalizat?"
        ),

        "Ingrijirea copilului si viata de familie": (
            "Ești responsabil de crearea unui curs online despre Îngrijirea Copilului și Viața de Familie, destinat celor care vor să învețe cum să își îngrijească copiii și familia.\n\n"
            "👶 Cum ai structura acest curs pentru a acoperi atât aspecte fundamentale ale îngrijirii copilului, cât și strategii avansate de educație parentală?\n\n"
            "👶 Ce activități interactive ai adăuga pentru a ajuta participanții să aplice cunoștințele despre viața de familie?\n\n"
            "👶 Care sunt pașii esențiali pentru a încuraja participanții să aplice metode eficiente de îngrijire a copiilor?"
        ),

        "Altele": (
            "Ești responsabil de crearea unui curs online pentru un domeniu general care nu se încadrează în categoriile deja menționate.\n\n"
            "❓ Cum ai structura acest curs pentru a acoperi atât concepte fundamentale, cât și tehnici avansate în domeniul respectiv?\n\n"
            "❓ Ce activități interactive ai adăuga pentru a face cursul mai captivant și mai aplicabil pentru participanți?\n\n"
            "❓ Care sunt abilitățile esențiale pe care participanții trebuie să le dezvolte pentru a deveni experți în acest domeniu?"
        ),

        "characters_about" : "maxim 1000 de caractere",
        "characters_course" : "200 - 1000 de caractere",
        "min_200" : "Te rog sa scrii minim 200 de caractere.",
        "max_1000" : "Te rog sa scrii maxim 1000 de caractere.",
        "requirement_length" : "Te rog sa spun despre crearea cursului in minim 200 de caractere si maxim 1000 de caractere.",	
        "send_form" : "Multumesc pentru raspunsuri! Curand vei putea vedea niste grafice cu acestea!"
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
    st.write(current_translations['part1'])
    age = st.slider(
        current_translations['age'], 
        0, 
        100, 
        value=st.session_state.age if 'age' in st.session_state else 25  
    )

    gender = st.radio(
        current_translations['gender'],
        current_translations["gender_list"],
        index=current_translations["gender_list"].index(st.session_state.gender) 
        if 'gender' in st.session_state and st.session_state.gender in current_translations["gender_list"] 
        else 0  
    )

    country_list = [country[1] for country in st.session_state.countries]
    country = st.selectbox(
        current_translations['country'],
        country_list,
        index=country_list.index(st.session_state.country) 
        if 'country' in st.session_state and st.session_state.country in country_list 
        else 0  
    )

    
    education = st.selectbox(
        current_translations['education'],
        current_translations["education_list"],
        index=current_translations["education_list"].index(st.session_state.education) 
        if 'education' in st.session_state and st.session_state.education in current_translations["education_list"] 
        else 0  
    )

    with st.form(key="form_page1"):
        next_button = st.form_submit_button(label=current_translations['next_button'])

        if next_button: 
            st.session_state.age = age
            st.session_state.gender = gender
            st.session_state.country = country
            st.session_state.education = education
   
            next_page()

elif st.session_state.page == 4:
    st.markdown(current_translations['part2'])

    selected_platforms = st.multiselect(
        current_translations['platforms'], current_translations["platforms_list"])
    if "Others" in selected_platforms or "Altele" in selected_platforms: 
        other_platform = st.text_input(current_translations['specify_platform'],
                                       value=st.session_state.other_platform)
        if other_platform.strip():
            selected_platforms = [p for p in selected_platforms if p not in ["Others", "Altele"]]
            selected_platforms.append(other_platform)
        else:
            st.error(current_translations['warning_other_platform'])
    else:
        other_platform = ""
    st.write("Selected:", selected_platforms)

   
    selected_courses = st.multiselect(
        current_translations['course_types'], current_translations["course_types_list"])
    if "Others" in selected_courses or "Altele" in selected_courses:
        other_course = st.text_input(current_translations['specify_course'],
                                       value=st.session_state.other_course)
        if other_course.strip():
            selected_courses = [p for p in selected_courses if p not in ["Others", "Altele"]]
            selected_courses.append(other_course)
        else:
            st.error(current_translations['warning_other_course'])
    else:
        other_course = ""
    
    st.write("Selected:", selected_courses)

    preference = st.radio(
    current_translations['preference_onl'], 
    current_translations["preference_onl_list"],
    index=current_translations["preference_onl_list"].index(
        st.session_state.get("preference", current_translations["preference_onl_list"][0])
    )
)
    st.write(current_translations['why_visit'])

    if "selected_usage" not in st.session_state:
        st.session_state.selected_usage = []

    selected_usage = []


    for option in current_translations["purpose_list"]:
        if st.checkbox(option, value=(option in st.session_state.selected_usage), key=f"usage_{option}"):
            selected_usage.append(option)


    if "Job Purposes" in selected_usage or "Locul de munca" in selected_usage:
        col1, col2, col3 = st.columns([0.05, 0.9, 0.05])

        with col2:

            st.markdown("### 💼")

            job = st.text_input(
                current_translations['job'],
                value=st.session_state.get("job", "")
                )

            mandatory_value = st.session_state.get("mandatory", "")
            mandatory = st.radio(
                current_translations["mandatory_courses"],
                current_translations["yes_no"],
                index=current_translations["yes_no"].index(mandatory_value)
                if mandatory_value in current_translations["yes_no"]
                else 0
                )
            
            promotion_value = st.session_state.get("promotion", "")
            promotion = st.radio(
                current_translations["promotion_courses"],
                current_translations["yes_no"],
                index=current_translations["yes_no"].index(promotion_value)
                if promotion_value in current_translations["yes_no"]
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
                default=st.session_state.get('selected_reasons', [])
            )

            beforeClasses = st.radio(
                current_translations['check_lectures'],
                current_translations["yes_no"],
                index=current_translations["yes_no"].index(st.session_state.get('beforeClasses', current_translations["yes_no"][0]))
            )


            exams = st.radio(
                current_translations['check_exams'],
                current_translations["exam_list"],
                index=current_translations["exam_list"].index(st.session_state.get('exams', current_translations["exam_list"][0]))
                )
            st.write(current_translations['grade_before'])
            col_a, col_b = st.columns(2)
            with col_a:
                grade_before = st.text_input(
                    current_translations["your_grade_before"],
                    value=st.session_state.get('grade_before', '')  # Default to an empty string if no value is stored
                )            
            with col_b:
                max_grade_before = st.text_input(
                    current_translations["out_of_before"], 
                    value=st.session_state.get('max_grade_before', '')  # Default to an empty string if no value is stored
                )

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
                grade_after = st.text_input(
                    current_translations["your_grade_after"],
                    value=st.session_state.get('grade_after', '')
                )
            with col_d:
                max_grade_after = st.text_input(
                    current_translations["out_of_after"], 
                    value=st.session_state.get('max_grade_after', '')
                )

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

    

    learning_method = st.radio(
       current_translations['learning_method'],
       current_translations["learning_method_list"],
       index=current_translations["learning_method_list"].index(st.session_state.learning_method)
       if 'learning_method' in st.session_state and st.session_state.learning_method in current_translations["learning_method_list"]
       else 0  
    )       

    frequency = st.radio(
    current_translations['frequency'],
    current_translations["frequency_list"],
    index=current_translations["frequency_list"].index(st.session_state.frequency)
    if 'frequency' in st.session_state and st.session_state.frequency in current_translations["frequency_list"]
    else 0  
    )

    
    payed_courses = st.radio(
    current_translations['payed_courses'],
    current_translations["yes_no"],
    index=current_translations["yes_no"].index(st.session_state.payed_courses)
    if 'payed_courses' in st.session_state and st.session_state.payed_courses in current_translations["yes_no"]
    else 0  
    )
    
    if 'payment' in st.session_state:
        saved_payment = st.session_state.payment
    else:
        saved_payment = 100 

    if payed_courses == "Da":
        payment = st.slider(
            current_translations['payment'], 
            0, 
            10000, 
            saved_payment  
        )
    elif payed_courses == "Yes":
        
        payment = st.slider(
            current_translations['payment'], 
            0, 
            2000, 
            saved_payment  
        )
    else:
        payment = 0



    bestCourse = st.text_input(
    current_translations['best_course'],
    value=st.session_state.bestCourse if 'bestCourse' in st.session_state else ""
    
    ) 

    dropOut = st.radio(
    current_translations['dropOut'],
    current_translations["yes_no"],
    index=current_translations["yes_no"].index(st.session_state.dropOut)
    if 'dropOut' in st.session_state and st.session_state.dropOut in current_translations["yes_no"]
    else 0
    )

    if dropOut == "Yes" or dropOut == "Da":
        dropOutReason = st.radio(
            current_translations['dropOutReason'],
        current_translations["dropOutReason_list"],
        index=current_translations["dropOutReason_list"].index(st.session_state.dropOutReason)
        if 'dropOutReason' in st.session_state and st.session_state.dropOutReason in current_translations["dropOutReason_list"]
        else 0
        )
    else:
        dropOutReason = None

    completationRate = st.slider(
        current_translations['completion_rate'], 0, 100, 
        st.session_state.completationRate if 'completationRate' in st.session_state else 50
    )


    certification = st.radio(
        current_translations['certification'],
        current_translations["certification_list"],
        index=current_translations["certification_list"].index(st.session_state.certification)
        if 'certification' in st.session_state and st.session_state.certification in current_translations["certification_list"]
        else 0 
    )


  
    notes = st.multiselect(
        current_translations['notes'],
        current_translations["notes_list"],
        default=st.session_state.notes if 'notes' in st.session_state else []
    )

    
    multitasking = st.radio(
        current_translations['multitasking'],
        current_translations["multitasking_list"],
        index=current_translations["multitasking_list"].index(st.session_state.multitasking)
        if 'multitasking' in st.session_state and st.session_state.multitasking in current_translations["multitasking_list"]
        else 0
    )
    
    st.write("### Would you try?")
    vr = st.radio(
    current_translations['vr'], 
    current_translations['yes_no'],
    index=current_translations['yes_no'].index(st.session_state.vr)
    if 'vr' in st.session_state and st.session_state.vr in current_translations['yes_no']
    else 0
    )

    liveInteraction = st.radio(
        current_translations['live_interaction'],
        current_translations['yes_no'],
        index=current_translations['yes_no'].index(st.session_state.liveInteraction)
        if 'liveInteraction' in st.session_state and st.session_state.liveInteraction in current_translations['yes_no']
        else 0
    )

    immersive = st.radio(
        current_translations['immersive'],
        current_translations['yes_no'],
        index=current_translations['yes_no'].index(st.session_state.immersive)
        if 'immersive' in st.session_state and st.session_state.immersive in current_translations['yes_no']
        else 0
    )

    replacement = st.radio(
        current_translations['replacement'],
        current_translations["replacement_list"],
        index=current_translations["replacement_list"].index(st.session_state.replacement)
        if 'replacement' in st.session_state and st.session_state.replacement in current_translations["replacement_list"]
        else 0
    )

    aiAssistant = st.radio(
        current_translations['ai_assistant'],
        current_translations['yes_no'],
        index=current_translations['yes_no'].index(st.session_state.aiAssistant)
        if 'aiAssistant' in st.session_state and st.session_state.aiAssistant in current_translations['yes_no']
        else 0
    )

    aiProfessor = st.radio(
        current_translations['ai_professor'],
        current_translations['yes_no'],
        index=current_translations['yes_no'].index(st.session_state.aiProfessor)
        if 'aiProfessor' in st.session_state and st.session_state.aiProfessor in current_translations['yes_no']
        else 0
    )


    with st.form(key="form_navigation"):
        col1, col2, col3 = st.columns(3)
        with col1:
                next_button = st.form_submit_button(current_translations['next_button'])
                if next_button:
                    st.session_state.selected_platforms = selected_platforms  
                    st.session_state.selected_courses = selected_courses  
                    st.session_state.selected_usage = selected_usage  
                    st.session_state.job = job
                    st.session_state.mandatory = mandatory
                    st.session_state.promotion = promotion
                    st.session_state.selected_reasons = reasons
                    st.session_state.check_lectures = beforeClasses
                    st.session_state.check_exams = exams
                    st.session_state.grade_before = grade_before
                    st.session_state.max_grade_before = max_grade_before
                    st.session_state.grade_after = grade_after
                    st.session_state.max_grade_after = max_grade_after
                    st.session_state.learning_method = learning_method
                    st.session_state.certification = certification
                    st.session_state.multitasking = multitasking
                    st.session_state.notes = notes
                    st.session_state.bestCourse = bestCourse
                    st.session_state.frequency = frequency
                    st.session_state.payed_courses = payed_courses
                    st.session_state.payment = payment
                    st.session_state.dropOut = dropOut
                    # if dropOut == "Yes" or dropOut == "Da":
                    #     st.session_state.dropOutReason = dropOutReason
                    # else:
                    #     st.session_state.dropOutReason = None
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
                    elif "Others" in st.session_state.selected_platforms or "Altele" in st.session_state.selected_platforms and not st.session_state.other_platform.strip():
                        st.warning(current_translations['warning_other_platform'])
                    elif not st.session_state.selected_courses:
                        st.warning(current_translations['warning_courses'])
                    elif "Others" in st.session_state.selected_courses or "Altele" in st.session_state.selected_courses and not st.session_state.other_course.strip():
                        st.warning(current_translations['warning_other_course'])
                    elif not st.session_state.selected_usage:
                        st.warning(current_translations['warning_usage'])
                    elif "School purposes" in st.session_state.selected_usage or "Scoala" in st.session_state.selected_usage:
                        if not st.session_state.selected_reasons:
                            st.warning(current_translations['warning_reasons'])
                        elif not grade_before or not max_grade_before or not grade_after or not max_grade_after:
                            st.warning(current_translations['warning_gpa'])
                    elif "Job Purposes" in st.session_state.selected_usage or "Locul de munca" in st.session_state.selected_usage:
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
                    # elif "No" in st.session_state.dropOut or "Nu" in st.session_state.dropOut:
                    #     if st.session_state.dropOutReason is None:
                    #         st.warning(current_translations['warning_dropOut'])
                    else:
                    # st.write("NU VREAU SA MERG")
                        next_page()
        with col3:
            back_button = st.form_submit_button(current_translations['back_button'])
            if back_button:
                prev_page()


elif st.session_state.page == 5:
    st.write(current_translations["part3"])

    if st.session_state.selected_courses:
        first_course = st.session_state.selected_courses[0]

        st.write(f"{current_translations['about1']} {first_course} {current_translations['about2']}")
        
        about = st.text_area(current_translations["characters_about"], key="about_input_unique")

        st.write(current_translations[first_course])
        user_input = st.text_area(current_translations["characters_course"], key="user_input_unique")

        # if user_input.strip():
        #     try:
        #         if len(user_input) <= 200:
        #             st.error(current_translations["min_200"])
        #         elif len(user_input) >= 1000:
        #             st.error(current_translations["max_1000"])
        #         # else:
        #         #     st.success(current_translations["valid_input"])
        #     except ValueError:
        #         st.error("An error occurred")

    with st.form(key="form_submition"):
        col1, col2, col3 = st.columns(3)
        with col1:
            next_button = st.form_submit_button("Submit")
        with col2:
            back_button = st.form_submit_button(current_translations['back_button'])

    if next_button:
        st.session_state.about = about  
        st.session_state.specific_course = user_input  


        st.write("### Summary of Your Answers:")

        # Page 3 responses
        st.write(f"**Age:** {st.session_state.age}")
        st.write(f"**Gender:** {st.session_state.gender}")
        st.write(f"**Country:** {st.session_state.country}")
        st.write(f"**Education Level:** {st.session_state.education}")

        # Additional responses (from your example)
        st.write(f"**Selected Platforms:** {', '.join(st.session_state.selected_platforms)}")
        st.write(f"**Selected Courses:** {', '.join(st.session_state.selected_courses)}")
        st.write(f"**Usage:** {st.session_state.selected_usage}")
        st.write(f"**Job:** {st.session_state.job}")
        st.write(f"**Mandatory:** {st.session_state.mandatory}")
        st.write(f"**Promotion:** {st.session_state.promotion}")
        st.write(f"**Reasons for Choosing Course:** {', '.join(st.session_state.selected_reasons)}")
        st.write(f"**Check Lectures:** {st.session_state.check_lectures}")
        st.write(f"**Check Exams:** {st.session_state.check_exams}")
        st.write(f"**Grade Before:** {st.session_state.grade_before}")
        st.write(f"**Max Grade Before:** {st.session_state.max_grade_before}")
        st.write(f"**Grade After:** {st.session_state.grade_after}")
        st.write(f"**Max Grade After:** {st.session_state.max_grade_after}")
        st.write(f"**Learning Method:** {st.session_state.learning_method}")
        st.write(f"**Frequency:** {st.session_state.frequency}")
        st.write(f"**Paid Courses:** {st.session_state.payed_courses}")
        st.write(f"**Payment:** {st.session_state.payment}")

        st.write(f"**Best Course:** {st.session_state.bestCourse}")
        st.write(f"**Dropout Status:** {st.session_state.dropOut}")
        # if st.session_state.dropOut == "Yes" or st.session_state.dropOut == "Da":
        st.write(f"**Dropout Reason:** {st.session_state.dropOutReason}")
        st.write(f"**Completion Rate:** {st.session_state.completationRate}")
        st.write(f"**Certification:** {st.session_state.certification}")
        st.write(f"**Notes:** {st.session_state.notes}")
        st.write(f"**Multitasking:** {st.session_state.multitasking}")
        st.write(f"**Preference:** {st.session_state.preference}")
        st.write(f"**VR Usage:** {st.session_state.vr}")
        st.write(f"**Live Interaction:** {st.session_state.liveInteraction}")
        st.write(f"**Immersive Learning:** {st.session_state.immersive}")
        st.write(f"**Replacement:** {st.session_state.replacement}")
        st.write(f"**AI Assistant:** {st.session_state.aiAssistant}")
        st.write(f"**AI Professor:** {st.session_state.aiProfessor}")
        st.write(f"**About Course:** {st.session_state.about}")
        st.write(f"**Specific Course:** {st.session_state.specific_course}")


        st.success(current_translations["send_form"])
        st.balloons()

        # if len(st.session_state.specific_course) <= 200 or len(st.session_state.specific_course) >= 1000:
        #     st.warning(current_translations["requirement_length"])
        # else:
        #     st.success(current_translations["send_form"])
        #     st.balloons()

    if back_button:
        prev_page()






    


    

