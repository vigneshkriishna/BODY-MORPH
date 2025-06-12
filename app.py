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

# --- Black & White Styling ---
st.markdown("""
    <style>
        .css-1d391kg {padding: 0rem 2rem;}
        .block-container {padding-top: 1rem; padding-bottom: 2rem;}
        .css-18e3th9 {
            background-color: #000 !important;
            color: #fff !important;
            box-shadow: none !important;
        }
        .css-1v3fvcr {display: none;}

        html, body, [class*="css"] {
            background-color: #000;
            color: #fff;
            font-family: 'Helvetica Neue', sans-serif;
        }

        h1, h2, h3, h4 {
            color: #fff;
            margin-bottom: 0.3em;
        }

        .stButton button {
            background-color: #fff;
            color: #000;
            border-radius: 8px;
            font-weight: 700;
            padding: 0.5em 1.5em;
        }

        .stButton button:hover {
            background-color: #999;
            color: #000;
        }

        input, textarea, select {
            background-color: #111 !important;
            border: 1.5px solid #fff !important;
            border-radius: 6px !important;
            padding: 0.4em !important;
            color: #fff !important;
            font-weight: 500 !important;
        }

        input::placeholder, textarea::placeholder {
            color: #aaa !important;
            font-style: italic;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <div style='text-align: center; padding: 1.5em 0 1em 0;'>
        <h1>🧬 BODY-MORPH</h1>
        <p style='font-size: 1.1em; color: #aaa;'>Your AI-fueled journey to gut health & core transformation</p>
    </div>
""", unsafe_allow_html=True)

# --- User Info Form ---
with st.form("user_info_form", clear_on_submit=True):
    st.markdown("### 👤 Your Info")
    name = st.text_input("Full Name", value="", placeholder="Enter your full name")
    age = st.number_input("Age", min_value=10, max_value=100, step=1, value=20)
    sex = st.selectbox("Sex", ["", "Male", "Female", "Other"])
    height_cm = st.number_input("Height (cm)", min_value=100, max_value=250, step=1)
    weight_kg = st.number_input("Weight (kg)", min_value=30, max_value=200, step=1)
    medical_conditions = st.text_area("Medical Conditions", placeholder="e.g., acidity, IBS...")
    goal = st.text_input("Fitness Goal", placeholder="e.g., build core strength, lose fat")
    level = st.selectbox("Fitness Level", ["", "Beginner", "Intermediate", "Advanced"])
    diet_pref = st.selectbox("Diet Preference", ["", "Vegetarian", "Vegan", "High Protein", "Low Carb"])
    submitted = st.form_submit_button("🚀 Generate Plan")

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
        st.warning("⚠️ Please fill in all required fields.")
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
- Fitness Level: {level}
- Goal: {goal}
- Diet Preference: {diet_pref}
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
                st.success(f"✅ Plan ready for {name}!")
                st.markdown(f"#### 📊 BMI: `{bmi}` — *{bmi_status}*")
                st.markdown(response.text)

                # --- PDF Generation ---
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
