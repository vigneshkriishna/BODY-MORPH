import streamlit as st
import google.generativeai as genai
import io
from fpdf import FPDF

# Set API key securely
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Page config
st.set_page_config(page_title="BODY-MORPH | AI Fitness Planner", layout="centered", initial_sidebar_state="collapsed")

# Simple styling
st.markdown("""
    <style>
        /* Clean header */
        .main-header {
            text-align: center;
            margin-bottom: 2rem;
            padding: 1rem;
            border-bottom: 3px solid #4CAF50;
            background: #f8f9fa;
            border-radius: 10px;
        }
        
        .main-header h1 {
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
            color: #2E7D32;
        }
        
        .main-header h3 {
            color: #666;
            font-weight: bold;
            margin-top: 0;
        }
        
        /* Simple button */
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 600 !important;
        }
        
        .stButton button:hover {
            background-color: #45a049 !important;
        }
        
        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .main-header h1 {
                font-size: 2.5rem !important;
            }
            
            .main-header h3 {
                font-size: 1.1rem !important;
            }
            
            .stTextInput input, .stNumberInput input, .stTextArea textarea {
                font-size: 16px !important;
            }
        }
        
        /* Hide Streamlit branding */
        .css-1v3fvcr {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Header with responsive styling
st.markdown("""
    <div class='main-header'>
        <h1>🧬 <strong>BODY-MORPH</strong></h1>
        <h3>Transform Your Body, Transform Your Life</h3>
    </div>
""", unsafe_allow_html=True)

# --- User Info Form ---
with st.form(key='user_info_form', clear_on_submit=True):
    name = st.text_input('Name', placeholder='Enter your full name')
    age = st.number_input('Age', min_value=10, max_value=100, step=1, value=None)
    sex = st.selectbox('Gender', ['', 'Male', 'Female', 'Other'])
    height_cm = st.number_input('Height (cm)', min_value=100, max_value=250, step=1, value=None)
    weight_kg = st.number_input('Weight (kg)', min_value=30, max_value=200, step=1, value=None)
    activity_level = st.selectbox('Activity Level', ['', 'Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active'])
    goal = st.text_input('Fitness Goal', placeholder='e.g., build core strength, lose fat')
    level = st.selectbox('Fitness Level', ['', 'Beginner', 'Intermediate', 'Advanced'])
    diet_pref = st.selectbox('Diet Preference', ['', 'Vegetarian', 'Vegan', 'High Protein', 'Low Carb', 'Non Vegetarian'])
    allergies = st.text_input('Allergies', placeholder='e.g., lactose, gluten')
    medical_conditions = st.text_area('Health Conditions', placeholder='e.g., acidity, IBS...')
    submitted = st.form_submit_button('🚀 Generate My Plan')

# --- BMI Helpers ---
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

# --- On Form Submit ---
if submitted:
    if not all([name, age, height_cm, weight_kg, goal]):
        st.error("Please fill in all the required fields.")
    else:
        with st.spinner("🧠 Crafting your personalized plan..."):
            bmi = calculate_bmi(height_cm, weight_kg)
            bmi_status = interpret_bmi(bmi)
            prompt = f"""
You're a certified calisthenics coach and registered gut nutritionist.

User Details:
- Name: {name}
- Age: {age}
- Sex: {sex}
- Height: {height_cm} cm
- Weight: {weight_kg} kg
- BMI: {bmi} ({bmi_status})
- Activity Level: {activity_level}
- Fitness Level: {level}
- Goal: {goal}
- Diet Preference: {diet_pref}
- Allergies: {allergies}
- Medical Issues: {medical_conditions if medical_conditions else "None"}

Instructions:
1. Provide a **1-week workout split** in a table.
2. Generate a **gut-friendly diet plan** (breakfast, lunch, dinner), with 5 options each.
3. Offer **BMI interpretation + health tips**.
4. Add **hydration & digestion suggestions**.
Format neatly in markdown tables.
"""
            try:
                response = model.generate_content(prompt)
                st.subheader(f"✅ Plan ready for {name}!")
                st.markdown(f"#### 📊 BMI: `{bmi}` — *{bmi_status}*")
                st.write(response.text)

                def markdown_to_pdf(md_text):
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_auto_page_break(auto=True, margin=15)
                    pdf.set_font("Arial", size=12)
                    for line in md_text.split('\n'):
                        safe_line = line.encode('latin-1', 'replace').decode('latin-1')
                        pdf.multi_cell(0, 10, safe_line)
                    return io.BytesIO(pdf.output(dest='S').encode('latin-1'))

                pdf_bytes = markdown_to_pdf(response.text)
                st.markdown("### 📥 Download Your Plan")
                st.download_button(
                    label="⬇️ Download as PDF",
                    data=pdf_bytes,
                    file_name=f"{name}_BodyMorph_Plan.pdf",
                    mime="application/pdf"
                )

                st.caption("⚠️ This is not medical advice. Always consult a healthcare provider before starting any diet/fitness plan.")
            except Exception as e:
                st.error(f"❌ Oops! Something went wrong: {e}")
