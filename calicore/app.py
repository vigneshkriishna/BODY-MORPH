import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import io
from docx import Document  # Requires 'python-docx' package, not 'docx'
from fpdf import FPDF

# Load the API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/fitness.png", width=80)
    st.markdown(
        """
        <div style='
            background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 100%);
            border-radius: 10px;
            padding: 1.2em 0.5em 1em 0.5em;
            margin-bottom: 1em;
            box-shadow: 0 2px 8px #b2ebf2;
        '>
            <h2 style='color:#fff;font-weight:700;margin-bottom:0.2em;'>CaliCore AI</h2>
            <div style='color:#e3f2fd;font-size:1em;'>
                Your trusted AI-powered Calisthenics & Gut Health Planner.<br>
                <span style='font-size:0.95em;color:#b2ebf2;'>Personalized. Science-backed. Confidential.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown(
        """
        <div style='color:#1976D2;font-weight:600;margin-bottom:0.5em;'>Instructions:</div>
        <ul style='margin-bottom:0;color:#607d8b;'>
            <li>Fill in your details</li>
            <li>Click <b>Generate Plan</b></li>
            <li>Download your personalized PDF</li>
        </ul>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown(
        """
        <div style='font-size:0.95em;color:#607d8b;'>
            Powered by <img src='https://upload.wikimedia.org/wikipedia/commons/4/4a/Logo_2022_Google.svg' width='60' style='vertical-align:middle'/> Gemini
        </div>
        """,
        unsafe_allow_html=True
    )
    st.caption("<span style='color:#90a4ae;'>© 2024 CaliCore. All rights reserved.</span>", unsafe_allow_html=True)

# --- Main UI ---
st.markdown(
    """
    <div style='
        background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 100%);
        border-radius: 12px;
        padding: 1.2em 0.5em 1em 0.5em;
        margin-bottom: 1.5em;
        box-shadow: 0 2px 12px #b2ebf2;
    '>
        <h1 style='text-align: center; color: #fff; font-weight:700; margin-bottom:0.2em;'>
            💪 CaliCore - Calisthenics + Gut Health Planner
        </h1>
        <div style='text-align:center; color:#e3f2fd; font-size:1.1em; margin-bottom:0.2em;'>
            Get a science-based, AI-personalized 1-week calisthenics and gut-friendly nutrition plan.<br>
            <span style='color:#b2ebf2;'>Your data is confidential and used only for plan generation.</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<hr style='border-top:1px solid #b2ebf2;'>", unsafe_allow_html=True)

# --- Input Card ---
st.markdown("#### <span style='color:#2193b0'>👤 Personal & Fitness Information</span>", unsafe_allow_html=True)

name = st.text_input("Full Name")
age = st.number_input("Age", min_value=10, max_value=100, step=1)
sex = st.selectbox("Sex", ["Male", "Female", "Other"])
height_cm = st.number_input("Height (cm)", min_value=100, max_value=250)
weight_kg = st.number_input("Weight (kg)", min_value=30, max_value=200)
medical_conditions = st.text_area("Medical Conditions", placeholder="e.g., acidity, IBS, etc.")
goal = st.text_input("Fitness Goal", placeholder="e.g., build core strength, lose fat")
level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
diet_pref = st.selectbox("Diet Preference", ["None", "Vegetarian", "Vegan", "High Protein", "Low Carb"])

st.markdown("<br>", unsafe_allow_html=True)

submit = st.button("🚀 Generate Plan", use_container_width=True)

# Calculate BMI
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

# Interpret BMI
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

if submit:
    if not all([name, age, height_cm, weight_kg, goal]):
        st.warning("⚠️ Please fill in all required fields to get your personalized plan.")
    else:
        with st.spinner("🧠 Generating your science-backed plan..."):
            bmi = calculate_bmi(height_cm, weight_kg)
            bmi_status = interpret_bmi(bmi)

            # 🔥 Gemini Prompt
            prompt = f"""
You're a certified calisthenics coach and registered gut nutritionist.

Based on the following user:
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

Do the following:
1. Give a **1-week workout split** in a table for {level.lower()} level.
2. Generate a **diet plan** with 3 meals (breakfast, lunch, dinner). For each meal, give **5 different options**, gut-friendly and aligned with {diet_pref}.
3. Show **BMI interpretation and tips**.
4. Suggest **hydration and digestion tips**.

Format EVERYTHING in markdown tables, be clean, professional, and motivational. Use evidence-based recommendations.
"""

            try:
                response = model.generate_content(prompt)
                st.success(f"✅ Your personalized plan is ready, {name}!")

                # --- Output Card ---
                st.markdown(
                    """
                    <div style='
                        background: #f8fdff;
                        border-radius: 10px;
                        box-shadow: 0 2px 8px #e0f7fa;
                        padding: 1.5em 2em 1.5em 2em;
                        margin-bottom: 2em;
                        max-width: 800px;
                        margin-left: auto;
                        margin-right: auto;
                    '>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<div style='background: linear-gradient(90deg, #e0f7fa 0%, #b2ebf2 100%);"
                    f"padding:1em;border-radius:8px;border:1px solid #b2ebf2;margin-bottom:1em;'>"
                    f"<span style='font-size:1.2em;color:#1976D2;'>📊 <b>BMI:</b> <code>{bmi}</code> — <i>{bmi_status}</i></span>"
                    f"</div>",
                    unsafe_allow_html=True
                )
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)

                # --- Export option: PDF only ---
                st.markdown(
                    """
                    <div style='
                        background: #fff;
                        border-radius: 10px;
                        box-shadow: 0 2px 8px #e0f7fa;
                        padding: 1.2em 2em 1.2em 2em;
                        margin-bottom: 2em;
                        max-width: 600px;
                        margin-left: auto;
                        margin-right: auto;
                    '>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown("#### 📤 <span style='color:#2193b0'>Export Your Plan</span>", unsafe_allow_html=True)

                def markdown_to_pdf(md_text):
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_auto_page_break(auto=True, margin=15)
                    pdf.set_font("Arial", size=12)
                    for line in md_text.split('\n'):
                        # Replace unsupported characters for PDF export
                        safe_line = line.encode('latin-1', 'replace').decode('latin-1')
                        pdf.multi_cell(0, 10, safe_line)
                    # Get PDF as bytes and wrap in BytesIO
                    pdf_bytes = pdf.output(dest='S').encode('latin-1')
                    return io.BytesIO(pdf_bytes)

                pdf_bytes = markdown_to_pdf(response.text)
                st.download_button(
                    label="⬇️ Download as PDF",
                    data=pdf_bytes,
                    file_name=f"{name}_calicore_plan.pdf",
                    mime="application/pdf",
                    help="Download your personalized plan as a PDF file"
                )
                st.markdown("</div>", unsafe_allow_html=True)

                st.markdown(
                    "<div style='font-size:0.95em;color:#607d8b;margin-top:2em;'>"
                    "Disclaimer: This plan is for informational purposes only and does not replace professional medical advice. "
                    "Consult a healthcare provider before starting any new fitness or nutrition program."
                    "</div>",
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"❌ Sorry, something went wrong: {e}")
