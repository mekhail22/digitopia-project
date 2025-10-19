import streamlit as st

# ==============================
# Page Config
# ==============================
st.set_page_config(page_title="Grade 5 Learning App", page_icon="🎯", layout="wide")

# ==============================
# Global Styles (UI/UX)
# ==============================
def inject_base_css():
    st.markdown(
        """
        <style>
        /* خطوط عامة */
        html, body, [class*="css"]  {
            font-family: "Segoe UI", system-ui, -apple-system, "Cairo", "Noto Sans Arabic", Arial, sans-serif;
        }

        /* حاوية المحتوى */
        .main > div {
            padding-top: 1.2rem;
            padding-bottom: 2.2rem;
        }

        /* كروت لطيفة */
        .soft-card {
            background: rgba(255,255,255,0.85);
            border-radius: 18px;
            padding: 16px 18px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
            backdrop-filter: blur(6px);
            border: 1px solid rgba(255,255,255,0.45);
        }

        /* أزرار قوية غير شفافة */
        .stButton > button {
            background: #111 !important;
            color: #fff !important;
            border: 0 !important;
            border-radius: 12px !important;
            padding: 10px 16px !important;
            font-weight: 600 !important;
            transition: transform .04s ease-in-out, filter .1s ease-in-out;
        }
        .stButton > button:hover { filter: brightness(1.08); }
        .stButton > button:active { transform: translateY(1px) scale(0.99); background: #000 !important; }

        /* راديو واختيارات */
        div[role="radiogroup"] > label, .stSelectbox label, .stRadio label {
            font-weight: 600;
        }
        /* عناصر الراديو */
        div[role="radiogroup"] div[role="radio"] {
            background: rgba(255,255,255,0.9);
            border-radius: 12px;
            padding: 8px 12px;
            margin: 6px 0;
            border: 1px solid rgba(0,0,0,0.06);
        }
        div[role="radiogroup"] div[role="radio"]:hover {
            box-shadow: inset 0 0 0 2px rgba(0,0,0,0.08);
        }

        /* نتائج التصحيح */
        .result-green { color: #0a7d28; font-weight: 700; }
        .result-red   { color: #b00020; font-weight: 700; }

        /* عناوين */
        h1, h2, h3 { letter-spacing: .3px; }

        /* السايدبار */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0ea5e9 0%, #2563eb 60%, #1e293b 100%);
        }
        section[data-testid="stSidebar"] * {
            color: #fff !important;
        }
        section[data-testid="stSidebar"] .stProgress > div > div {
            background: rgba(255,255,255,0.9) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def set_background(page: str):
    """
    page: "lang" | "subject" | "math" | "science"
    لكل شاشة خلفية مختلفة باستخدام تدرجات آمنة (بدون صور خارجية).
    """
    gradients = {
        "lang": """
            background: radial-gradient(1200px 800px at 10% 10%, #fde68a 0%, rgba(253,230,138,0) 60%),
                        radial-gradient(1000px 700px at 90% 20%, #93c5fd 0%, rgba(147,197,253,0) 60%),
                        linear-gradient(180deg, #fdf2f8 0%, #e0f2fe 100%);
        """,
        "subject": """
            background: radial-gradient(1100px 900px at 15% 20%, #a7f3d0 0%, rgba(167,243,208,0) 55%),
                        radial-gradient(900px 700px at 85% 15%, #bfdbfe 0%, rgba(191,219,254,0) 55%),
                        linear-gradient(180deg, #f0f9ff 0%, #ecfeff 100%);
        """,
        "math": """
            background: radial-gradient(900px 700px at 12% 15%, #fca5a5 0%, rgba(252,165,165,0) 55%),
                        radial-gradient(900px 700px at 88% 10%, #fdba74 0%, rgba(253,186,116,0) 55%),
                        linear-gradient(180deg, #fff7ed 0%, #fee2e2 100%);
        """,
        "science": """
            background: radial-gradient(900px 700px at 12% 15%, #86efac 0%, rgba(134,239,172,0) 55%),
                        radial-gradient(900px 700px at 85% 10%, #93c5fd 0%, rgba(147,197,253,0) 55%),
                        linear-gradient(180deg, #ecfeff 0%, #dcfce7 100%);
        """,
    }
    st.markdown(
        f"""
        <style>
        .stApp {{
            {gradients.get(page, gradients["lang"])}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

inject_base_css()

# ==============================
# Texts (i18n)
# ==============================
TEXTS = {
    "ar": {
        "app_title": "🎯 تطبيق تعليمي للصف الخامس",
        "lang_title": "Select Language / اختر اللغة",
        "choose_lang": "اختر اللغة:",
        "ok": "موافق",
        "welcome": "اختر المادة وابدأ التعلم. لازم تجيب الدرجة الكاملة علشان تفتح المستوى التالي.",
        "math": "الرياضيات",
        "science": "العلوم",
        "choose_subject": "اختيار المادة",
        "current_level": "المستوى الحالي",
        "max_levels": "إجمالي المستويات",
        "points": "النقاط",
        "progress": "التقدّم",
        "back_home": "🔙 رجوع للقائمة الرئيسية",
        "select_level": "اختر مستوى للمراجعة أو الإكمال:",
        "must_full": "لازم الدرجة الكاملة لفتح المستوى التالي.",
        "no_questions": "لا توجد أسئلة لهذا المستوى حتى الآن.",
        "grade_btn": "تصحيح الإجابات ✅",
        "retry": "إعادة المحاولة 🔁",
        "next_level": "الانتقال للمستوى التالي ⏭️",
        "completed": "أتممت كل مستويات هذا الموضوع. أحسنت!",
        "score": "درجتك",
        "choose_answer": "اختر الإجابة:",
        "correct": "صحيح ✅",
        "wrong": "غلط ❌",
        "unanswered_warning": "من فضلك جاوب على كل الأسئلة قبل التصحيح.",
        "change_subject": "تغيير المادة 🔄",
        "q_word": "سؤال رقم",
        "summary": "ملخص التصحيح"
    },
    "en": {
        "app_title": "🎯 Grade 5 Learning App",
        "lang_title": "Select Language / اختر اللغة",
        "choose_lang": "Choose Language:",
        "ok": "OK",
        "welcome": "Choose a subject to start. You must score full marks to unlock the next level.",
        "math": "Math",
        "science": "Science",
        "choose_subject": "Choose Subject",
        "current_level": "Current Level",
        "max_levels": "Total Levels",
        "points": "Points",
        "progress": "Progress",
        "back_home": "🔙 Back to Main Menu",
        "select_level": "Select a level to review or continue:",
        "must_full": "Full score is required to unlock the next level.",
        "no_questions": "No questions for this level yet.",
        "grade_btn": "Grade Answers ✅",
        "retry": "Retry 🔁",
        "next_level": "Go to Next Level ⏭️",
        "completed": "You have completed all levels in this subject. Well done!",
        "score": "Your Score",
        "choose_answer": "Choose an answer:",
        "correct": "Correct ✅",
        "wrong": "Wrong ❌",
        "unanswered_warning": "Please answer all questions before grading.",
        "change_subject": "Change Subject 🔄",
        "q_word": "Question",
        "summary": "Grading Summary"
    }
}

# ==============================
# Session State Init
# ==============================
def init_state():
    ss = st.session_state
    if "lang" not in ss: ss.lang = None
    if "subject" not in ss: ss.subject = None                  # "math" | "science"
    if "levels" not in ss:
        # لكل مادة، لكل لغة، الحالة مستقلة (current, max_level, points)
        ss.levels = {
            "math_ar":    {"current": 1, "max_level": 3, "points": 0},
            "math_en":    {"current": 1, "max_level": 3, "points": 0},
            "science_ar": {"current": 1, "max_level": 3, "points": 0},
            "science_en": {"current": 1, "max_level": 3, "points": 0},
        }
    if "last_score" not in ss: ss.last_score = None
    if "last_total" not in ss: ss.last_total = None
    if "answers" not in ss: ss.answers = {}                   # تخزين اختيارات الأسئلة
    if "lang_pick_cache" not in ss: ss.lang_pick_cache = "العربية"

init_state()

# ==============================
# Questions Bank (AR + EN) — 3 levels × 10 questions لكل مادة/لغة
# ==============================
def Q_AR_MATH():
    return {
        1: [
            {"q": "٥ + ٣ =", "choices": ["٦", "٨", "٧", "٩"], "answer": "٨"},
            {"q": "٩ - ٤ =", "choices": ["٦", "٥", "٤", "٣"], "answer": "٥"},
            {"q": "٢ × ٣ =", "choices": ["٦", "٥", "٧", "٨"], "answer": "٦"},
            {"q": "١٢ ÷ ٤ =", "choices": ["٢", "٣", "٤", "٦"], "answer": "٣"},
            {"q": "٧ + ٨ =", "choices": ["١٥", "١٤", "١٦", "١٣"], "answer": "١٥"},
            {"q": "١٠ - ٧ =", "choices": ["٤", "٣", "٢", "٥"], "answer": "٣"},
            {"q": "٣ × ٤ =", "choices": ["١٢", "١٤", "١٠", "٩"], "answer": "١٢"},
            {"q": "١٨ ÷ ٣ =", "choices": ["٦", "٥", "٤", "٣"], "answer": "٦"},
            {"q": "٥ + ٩ =", "choices": ["١٥", "١٤", "١٣", "١٦"], "answer": "١٤"},
            {"q": "٨ - ٣ =", "choices": ["٤", "٥", "٦", "٧"], "answer": "٥"},
        ],
        2: [
            {"q": "١٥ + ٧ =", "choices": ["٢٢", "٢٣", "٢١", "٢٠"], "answer": "٢٢"},
            {"q": "٢٠ - ٩ =", "choices": ["١٢", "١١", "١٠", "٩"], "answer": "١١"},
            {"q": "٧ × ٦ =", "choices": ["٤٢", "٤٠", "٤٤", "٣٦"], "answer": "٤٢"},
            {"q": "٣٦ ÷ ٦ =", "choices": ["٧", "٦", "٥", "٤"], "answer": "٦"},
            {"q": "٩ + ١٣ =", "choices": ["٢٣", "٢٢", "٢١", "٢٠"], "answer": "٢٢"},
            {"q": "٥٠ - ٣٥ =", "choices": ["١٥", "١٤", "١٦", "١٣"], "answer": "١٥"},
            {"q": "٩ × ٤ =", "choices": ["٣٦", "٣٥", "٣٤", "٣٢"], "answer": "٣٦"},
            {"q": "٦٣ ÷ ٩ =", "choices": ["٧", "٨", "٦", "٥"], "answer": "٧"},
            {"q": "٣٠ + ٢٥ =", "choices": ["٥٥", "٥٤", "٥٣", "٥٦"], "answer": "٥٥"},
            {"q": "٤٥ - ١٩ =", "choices": ["٢٦", "٢٧", "٢٥", "٢٤"], "answer": "٢٦"},
        ],
        3: [
            {"q": "١٢ × ١٢ =", "choices": ["١٤٤", "١٥٦", "١٣٢", "١٢١"], "answer": "١٤٤"},
            {"q": "١٠٠ ÷ ٥ =", "choices": ["٢٠", "٢٥", "٣٠", "١٥"], "answer": "٢٠"},
            {"q": "٤٩ ÷ ٧ =", "choices": ["٦", "٧", "٨", "٥"], "answer": "٧"},
            {"q": "٨ × ٩ =", "choices": ["٧٢", "٧٣", "٧٤", "٧٠"], "answer": "٧٢"},
            {"q": "٢٠٠ - ١٥٠ =", "choices": ["٤٠", "٥٠", "٦٠", "٣٠"], "answer": "٥٠"},
            {"q": "٣ × ٢٥ =", "choices": ["٧٥", "٧٠", "٦٠", "٨٠"], "answer": "٧٥"},
            {"q": "١٥٠ ÷ ٣ =", "choices": ["٥٠", "٤٥", "٤٠", "٣٥"], "answer": "٥٠"},
            {"q": "١١ × ١١ =", "choices": ["١٢١", "١١١", "١٣٢", "١٠١"], "answer": "١٢١"},
            {"q": "٣٠٠ ÷ ١٠ =", "choices": ["٣٠", "٢٠", "٤٠", "٣٥"], "answer": "٣٠"},
            {"q": "٨٥ - ٦٩ =", "choices": ["١٦", "١٥", "١٧", "١٨"], "answer": "١٦"},
        ],
    }

def Q_EN_MATH():
    return {
        1: [
            {"q": "5 + 3 =", "choices": ["6", "8", "7", "9"], "answer": "8"},
            {"q": "9 - 4 =", "choices": ["6", "5", "4", "3"], "answer": "5"},
            {"q": "2 × 3 =", "choices": ["6", "5", "7", "8"], "answer": "6"},
            {"q": "12 ÷ 4 =", "choices": ["2", "3", "4", "6"], "answer": "3"},
            {"q": "7 + 8 =", "choices": ["15", "14", "16", "13"], "answer": "15"},
            {"q": "10 - 7 =", "choices": ["4", "3", "2", "5"], "answer": "3"},
            {"q": "3 × 4 =", "choices": ["12", "14", "10", "9"], "answer": "12"},
            {"q": "18 ÷ 3 =", "choices": ["6", "5", "4", "3"], "answer": "6"},
            {"q": "5 + 9 =", "choices": ["15", "14", "13", "16"], "answer": "14"},
            {"q": "8 - 3 =", "choices": ["4", "5", "6", "7"], "answer": "5"},
        ],
        2: [
            {"q": "15 + 7 =", "choices": ["22", "23", "21", "20"], "answer": "22"},
            {"q": "20 - 9 =", "choices": ["12", "11", "10", "9"], "answer": "11"},
            {"q": "7 × 6 =", "choices": ["42", "40", "44", "36"], "answer": "42"},
            {"q": "36 ÷ 6 =", "choices": ["7", "6", "5", "4"], "answer": "6"},
            {"q": "9 + 13 =", "choices": ["23", "22", "21", "20"], "answer": "22"},
            {"q": "50 - 35 =", "choices": ["15", "14", "16", "13"], "answer": "15"},
            {"q": "9 × 4 =", "choices": ["36", "35", "34", "32"], "answer": "36"},
            {"q": "63 ÷ 9 =", "choices": ["7", "8", "6", "5"], "answer": "7"},
            {"q": "30 + 25 =", "choices": ["55", "54", "53", "56"], "answer": "55"},
            {"q": "45 - 19 =", "choices": ["26", "27", "25", "24"], "answer": "26"},
        ],
        3: [
            {"q": "12 × 12 =", "choices": ["144", "156", "132", "121"], "answer": "144"},
            {"q": "100 ÷ 5 =", "choices": ["20", "25", "30", "15"], "answer": "20"},
            {"q": "49 ÷ 7 =", "choices": ["6", "7", "8", "5"], "answer": "7"},
            {"q": "8 × 9 =", "choices": ["72", "73", "74", "70"], "answer": "72"},
            {"q": "200 - 150 =", "choices": ["40", "50", "60", "30"], "answer": "50"},
            {"q": "3 × 25 =", "choices": ["75", "70", "60", "80"], "answer": "75"},
            {"q": "150 ÷ 3 =", "choices": ["50", "45", "40", "35"], "answer": "50"},
            {"q": "11 × 11 =", "choices": ["121", "111", "132", "101"], "answer": "121"},
            {"q": "300 ÷ 10 =", "choices": ["30", "20", "40", "35"], "answer": "30"},
            {"q": "85 - 69 =", "choices": ["16", "15", "17", "18"], "answer": "16"},
        ],
    }

def Q_AR_SCI():
    return {
        1: [
            {"q": "ما هو الكوكب الأحمر؟", "choices": ["الأرض", "المريخ", "المشتري", "الزهرة"], "answer": "المريخ"},
            {"q": "عدد كواكب المجموعة الشمسية =", "choices": ["٧", "٨", "٩", "٦"], "answer": "٨"},
            {"q": "أقرب كوكب للشمس =", "choices": ["عطارد", "الزهرة", "المريخ", "الأرض"], "answer": "عطارد"},
            {"q": "أكبر كوكب =", "choices": ["زحل", "المشتري", "أورانوس", "نبتون"], "answer": "المشتري"},
            {"q": "ما الغاز الذي نتنفسه؟", "choices": ["أكسجين", "هيدروجين", "نيتروجين", "هيليوم"], "answer": "أكسجين"},
            {"q": "أسرع حيوان بري =", "choices": ["الفهد", "الأسد", "الغزال", "النمر"], "answer": "الفهد"},
            {"q": "عدد قلوب الأخطبوط =", "choices": ["١", "٢", "٣", "٤"], "answer": "٣"},
            {"q": "مصدر ضوء القمر =", "choices": ["ذاته", "الشمس", "النجوم", "البرق"], "answer": "الشمس"},
            {"q": "أين تحدث عملية البناء الضوئي؟", "choices": ["الجذور", "الأوراق", "السيقان", "الزهور"], "answer": "الأوراق"},
            {"q": "كم عدد ألوان قوس قزح؟", "choices": ["٦", "٧", "٨", "٥"], "answer": "٧"},
        ],
        2: [
            {"q": "أكبر عضو في جسم الإنسان =", "choices": ["الكبد", "القلب", "الجلد", "الرئتان"], "answer": "الجلد"},
            {"q": "عدد عظام الإنسان البالغ =", "choices": ["٢٠٦", "٢٠٠", "٢١٠", "١٩٨"], "answer": "٢٠٦"},
            {"q": "الكوكب ذو الحلقات الشهيرة =", "choices": ["زحل", "أورانوس", "نبتون", "المشتري"], "answer": "زحل"},
            {"q": "الغاز اللازم للنبات في البناء الضوئي =", "choices": ["أكسجين", "ثاني أكسيد الكربون", "نيتروجين", "هيليوم"], "answer": "ثاني أكسيد الكربون"},
            {"q": "الحواس خمس، أي من التالي ليس حاسة؟", "choices": ["السمع", "اللمس", "التفكير", "الذوق"], "answer": "التفكير"},
            {"q": "درجة تجمد الماء النقي =", "choices": ["٠°م", "١٠°م", "١٠٠°م", "−٥°م"], "answer": "٠°م"},
            {"q": "أصغر عظمة في الجسم =", "choices": ["الركاب", "الفخذ", "الزند", "الكتف"], "answer": "الركاب"},
            {"q": "أكبر محيط =", "choices": ["الهادي", "الأطلسي", "الهندي", "المتجمد الشمالي"], "answer": "الهادي"},
            {"q": "الكوكب الأزرق هو =", "choices": ["الأرض", "نبتون", "أورانوس", "الزهرة"], "answer": "الأرض"},
            {"q": "الطاقة تُقاس بـ =", "choices": ["واط", "جول", "نيوتن", "فولت"], "answer": "جول"},
        ],
        3: [
            {"q": "أقرب نجم إلى الأرض =", "choices": ["الشمس", "الشعرى", "النجم القطبي", "قنطورس",], "answer": "الشمس"},
            {"q": "العنصر الأكثر وفرة في القشرة الأرضية =", "choices": ["الحديد", "الأكسجين", "السيليكون", "الألمنيوم"], "answer": "الأكسجين"},
            {"q": "وحدة القوة =", "choices": ["نيوتن", "جول", "واط", "أمبير"], "answer": "نيوتن"},
            {"q": "أصغر كواكب المجموعة الشمسية =", "choices": ["عطارد", "المريخ", "بلوتو (قزم)", "الزهرة"], "answer": "عطارد"},
            {"q": "كم لتر دم في جسم الإنسان (تقريبًا) =", "choices": ["٥", "٦", "٧", "٤"], "answer": "٥"},
            {"q": "أكبر غدة في جسم الإنسان =", "choices": ["الكبد", "البنكرياس", "الدرقية", "اللعابية"], "answer": "الكبد"},
            {"q": "عدد أضلاع الإنسان =", "choices": ["٢٤", "٢٢", "٢٠", "٢٦"], "answer": "٢٤"},
            {"q": "الغاز الذي يحمي من الأشعة فوق البنفسجية =", "choices": ["الأوزون", "الأكسجين", "ثاني أكسيد الكربون", "النيتروجين"], "answer": "الأوزون"},
            {"q": "حالة للمادة لها شكل وحجم ثابت =", "choices": ["الصلبة", "السائلة", "الغازية", "البلازما"], "answer": "الصلبة"},
            {"q": "تحول السائل إلى غاز يسمى =", "choices": ["تبخر", "تكاثف", "انصهار", "تجمد"], "answer": "تبخر"},
        ],
    }

def Q_EN_SCI():
    return {
        1: [
            {"q": "Which planet is called the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
            {"q": "Planets in the Solar System =", "choices": ["7", "8", "9", "6"], "answer": "8"},
            {"q": "Closest planet to the Sun =", "choices": ["Mercury", "Venus", "Mars", "Earth"], "answer": "Mercury"},
            {"q": "Largest planet =", "choices": ["Saturn", "Jupiter", "Uranus", "Neptune"], "answer": "Jupiter"},
            {"q": "Gas humans need to breathe =", "choices": ["Oxygen", "Hydrogen", "Nitrogen", "Helium"], "answer": "Oxygen"},
            {"q": "Fastest land animal =", "choices": ["Cheetah", "Lion", "Gazelle", "Leopard"], "answer": "Cheetah"},
            {"q": "Octopus has how many hearts? =", "choices": ["1", "2", "3", "4"], "answer": "3"},
            {"q": "Moon’s light source =", "choices": ["Itself", "Sun", "Stars", "Lightning"], "answer": "Sun"},
            {"q": "Where does photosynthesis happen?", "choices": ["Roots", "Leaves", "Stems", "Flowers"], "answer": "Leaves"},
            {"q": "How many rainbow colors?", "choices": ["6", "7", "8", "5"], "answer": "7"},
        ],
        2: [
            {"q": "Largest organ in the human body =", "choices": ["Liver", "Heart", "Skin", "Lungs"], "answer": "Skin"},
            {"q": "Adult human bones count =", "choices": ["206", "200", "210", "198"], "answer": "206"},
            {"q": "Planet famous for rings =", "choices": ["Saturn", "Uranus", "Neptune", "Jupiter"], "answer": "Saturn"},
            {"q": "Gas needed by plants for photosynthesis =", "choices": ["Oxygen", "Carbon dioxide", "Nitrogen", "Helium"], "answer": "Carbon dioxide"},
            {"q": "Which is NOT a sense?", "choices": ["Hearing", "Touch", "Thinking", "Taste"], "answer": "Thinking"},
            {"q": "Freezing point of pure water =", "choices": ["0°C", "10°C", "100°C", "-5°C"], "answer": "0°C"},
            {"q": "Smallest bone in the body =", "choices": ["Stapes", "Femur", "Ulna", "Scapula"], "answer": "Stapes"},
            {"q": "Largest ocean =", "choices": ["Pacific", "Atlantic", "Indian", "Arctic"], "answer": "Pacific"},
            {"q": "The Blue Planet is =", "choices": ["Earth", "Neptune", "Uranus", "Venus"], "answer": "Earth"},
            {"q": "Energy is measured in =", "choices": ["Watt", "Joule", "Newton", "Volt"], "answer": "Joule"},
        ],
        3: [
            {"q": "Closest star to Earth =", "choices": ["Sun", "Sirius", "Polaris", "Alpha Centauri"], "answer": "Sun"},
            {"q": "Most abundant element in Earth’s crust =", "choices": ["Iron", "Oxygen", "Silicon", "Aluminum"], "answer": "Oxygen"},
            {"q": "Unit of force =", "choices": ["Newton", "Joule", "Watt", "Ampere"], "answer": "Newton"},
            {"q": "Smallest planet in the Solar System =", "choices": ["Mercury", "Mars", "Pluto (dwarf)", "Venus"], "answer": "Mercury"},
            {"q": "Approximate liters of blood in humans =", "choices": ["5", "6", "7", "4"], "answer": "5"},
            {"q": "Largest gland in the human body =", "choices": ["Liver", "Pancreas", "Thyroid", "Salivary"], "answer": "Liver"},
            {"q": "How many human ribs? =", "choices": ["24", "22", "20", "26"], "answer": "24"},
            {"q": "Gas shielding from UV rays =", "choices": ["Ozone", "Oxygen", "CO₂", "Nitrogen"], "answer": "Ozone"},
            {"q": "State with fixed shape & volume =", "choices": ["Solid", "Liquid", "Gas", "Plasma"], "answer": "Solid"},
            {"q": "Liquid → Gas process =", "choices": ["Evaporation", "Condensation", "Melting", "Freezing"], "answer": "Evaporation"},
        ],
    }

# تحزيم بنك الأسئلة في dict موحد
QUESTIONS = {
    "math_ar": Q_AR_MATH(),
    "math_en": Q_EN_MATH(),
    "science_ar": Q_AR_SCI(),
    "science_en": Q_EN_SCI(),
}

# ==============================
# Helpers
# ==============================
def subject_key(lang: str, subject_internal: str) -> str:
    # subject_internal: "math" | "science"
    return f"{subject_internal}_{'ar' if lang=='ar' else 'en'}"

def reset_subject():
    st.session_state.subject = None
    st.session_state.last_score = None
    st.session_state.last_total = None
    st.session_state.answers = {}
    st.rerun()

def render_progress_sidebar(lang: str):
    t = TEXTS[lang]
    st.sidebar.title(t["progress"])
    # عرض progress للمادتين بحسب اللغة المختارة فقط
    keys = [f"math_{'ar' if lang=='ar' else 'en'}", f"science_{'ar' if lang=='ar' else 'en'}"]
    for key in keys:
        label = TEXTS[lang]["math"] if key.startswith("math") else TEXTS[lang]["science"]
        info = st.session_state.levels[key]
        st.sidebar.write(f"**{label}** — {t['current_level']}: {info['current']}/{info['max_level']} | {t['points']}: {info['points']}")
        st.sidebar.progress(min(info["current"]/info["max_level"], 1.0))
    st.sidebar.markdown("---")
    if st.session_state.subject:
        if st.sidebar.button(t["back_home"], use_container_width=True):
            reset_subject()

def grading_summary_block(items, lang: str):
    # items: list[ (index(1-based), is_correct:bool, correct_answer:str) ]
    t = TEXTS[lang]
    st.subheader(t["summary"])
    # عرض على شكل قائمة ملونة
    for idx, ok, corr in items:
        if lang == "ar":
            if ok:
                st.markdown(f"<div class='soft-card'><span class='result-green'>✅ {t['q_word']} {idx} — صحيح</span></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='soft-card'><span class='result-red'>❌ {t['q_word']} {idx} — غلط</span><br/><small>الإجابة الصحيحة: <b>{corr}</b></small></div>", unsafe_allow_html=True)
        else:
            if ok:
                st.markdown(f"<div class='soft-card'><span class='result-green'>✅ {t['q_word']} {idx} — Correct</span></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='soft-card'><span class='result-red'>❌ {t['q_word']} {idx} — Wrong</span><br/><small>Correct answer: <b>{corr}</b></small></div>", unsafe_allow_html=True)

# ==============================
# Language Gate
# ==============================
def language_gate():
    if st.session_state.lang is None:
        set_background("lang")
        st.title(TEXTS["ar"]["lang_title"])
        st.caption("Language first • اختر اللغة أولًا")
        # اختيارات سريعة
        c1, c2 = st.columns(2)
        with c1:
            if st.button("العربية", use_container_width=True):
                st.session_state.lang = "ar"
                st.rerun()
        with c2:
            if st.button("English", use_container_width=True):
                st.session_state.lang = "en"
                st.rerun()
        st.stop()

# ==============================
# Subject Menu
# ==============================
def subject_menu(lang: str):
    t = TEXTS[lang]
    set_background("subject")
    st.title(t["app_title"])
    st.caption(t["welcome"])
    render_progress_sidebar(lang)

    st.subheader(t["choose_subject"])
    c1, c2 = st.columns(2)
    chosen = None
    with c1:
        if st.button(("📐 " + t["math"]), use_container_width=True):
            chosen = "math"
    with c2:
        if st.button(("🔬 " + t["science"]), use_container_width=True):
            chosen = "science"

    if chosen:
        st.session_state.subject = chosen
        st.rerun()

# ==============================
# Quiz Runner
# ==============================
def run_quiz(lang: str, subject_internal: str):
    # subject_internal: "math" | "science"
    # key: subject_lang
    skey = subject_key(lang, subject_internal)
    info = st.session_state.levels[skey]
    level = info["current"]

    # خلفية حسب المادة
    set_background("math" if subject_internal == "math" else "science")

    t = TEXTS[lang]
    render_progress_sidebar(lang)

    # عنوان
    subj_label = t["math"] if subject_internal == "math" else t["science"]
    st.header(f"{subj_label} — {t['current_level']} {level}/{info['max_level']}")

    # اختيار مستوى للمراجعة (اختياري)
    available = list(range(1, info["current"] + 1))
    col_top = st.container()
    with col_top:
        st.markdown("<div class='soft-card'>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(t["current_level"], f"{info['current']}/{info['max_level']}")
        with c2:
            st.metric(t["points"], info["points"])
        with c3:
            if st.button(t["change_subject"], use_container_width=True):
                reset_subject()
        st.markdown("</div>", unsafe_allow_html=True)

    # اختيار مستوى لفتح أسئلة مستوى سابق (مراجعة)
    chosen_level = st.selectbox(
        f"{subj_label} — {t['select_level']}",
        available,
        index=len(available) - 1,
        key=f"sel-level-{skey}"
    )

    questions = QUESTIONS[skey][chosen_level]
    if not questions:
        st.info(t["no_questions"])
        return

    st.write(t["must_full"])

    key_prefix = f"{skey}-L{chosen_level}"
    # حفظ اختيارات المستخدم لكل سؤال
    if key_prefix not in st.session_state.answers:
        st.session_state.answers[key_prefix] = [None]*len(questions)

    # نموذج الأسئلة
    with st.form(f"form-{key_prefix}", clear_on_submit=False):
        for i, q in enumerate(questions, start=1):
            st.markdown(f"**{(TEXTS['ar']['q_word'] if lang=='ar' else TEXTS['en']['q_word'])} {i}:** {q['q']}")
            sel = st.radio(
                t["choose_answer"],
                q["choices"],
                index= (q["choices"].index(st.session_state.answers[key_prefix][i-1]) if st.session_state.answers[key_prefix][i-1] in q["choices"] else None),
                key=f"{key_prefix}-q{i}",
                horizontal=False,
            )
            st.session_state.answers[key_prefix][i-1] = sel
            st.markdown("---")
        submitted = st.form_submit_button(t["grade_btn"])

    # عند الضغط على تصحيح
    if submitted:
        selections = st.session_state.answers[key_prefix]
        # التحقق من الإجابة على كل الأسئلة
        if any(s is None for s in selections):
            st.warning(t["unanswered_warning"])
            return

        # التصحيح
        score = 0
        total = len(questions)
        summary_items = []  # (idx, is_correct, correct_answer)
        for i, q in enumerate(questions, start=1):
            ok = selections[i-1] == q["answer"]
            if ok: score += 1
            summary_items.append((i, ok, q["answer"]))

        # عرض النتيجة
        st.subheader(f"**{t['score']}: {score}/{total}**")

        # ملخص موحد (سؤال رقم ... صح/غلط) مع الألوان
        grading_summary_block(summary_items, lang)

        # حفظ آخر نتيجة
        st.session_state.last_score = score
        st.session_state.last_total = total

        # منطق فتح المستوى التالي
        if score == total:
            # إضافة النقاط
            st.session_state.levels[skey]["points"] += score

            # لو لسه فيه مستوى أعلى — زوّد current
            if st.session_state.levels[skey]["current"] < st.session_state.levels[skey]["max_level"]:
                st.session_state.levels[skey]["current"] += 1

        # أزرار بعد التصحيح
        # شرطك: لو 10/10 -> يظهر انتقال فقط. لو أقل -> يظهر إعادة فقط.
        btn_col1, btn_col2 = st.columns(2)
        if st.session_state.last_score == st.session_state.last_total:
            with btn_col1:
                # ظهر زر النقل فقط
                if st.button(t["next_level"], use_container_width=True, key=f"next-{key_prefix}"):
                    # لو اخترنا مستوى قديم ونجح 10/10، ننتقل للمستوى الحالي (قد يكون ارتفع بالفعل)
                    st.rerun()
        else:
            with btn_col2:
                # ظهر زر إعادة فقط
                if st.button(t["retry"], use_container_width=True, key=f"retry-{key_prefix}"):
                    # تفريغ اختيارات المستوى المختار فقط
                    st.session_state.answers[key_prefix] = [None]*len(questions)
                    st.session_state.last_score = None
                    st.session_state.last_total = None
                    st.rerun()

# ==============================
# App Flow
# ==============================
def main():
    language_gate()
    lang = st.session_state.lang
    # اختيار المادة إذا لم تُحدد
    if st.session_state.subject is None:
        subject_menu(lang)
        return

    # تشغيل الكويز
    subj_internal = st.session_state.subject  # "math" | "science"
    run_quiz(lang, subj_internal)

if __name__ == "__main__":
    main()
