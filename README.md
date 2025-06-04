# CaliCore AI 

**CaliCore AI** is a modern Streamlit web application that generates a personalized 1-week calisthenics and gut health plan using Google Gemini AI.  
Users enter their personal, fitness, and dietary details in a clean, single-column form.  
The app displays a professional, visually appealing plan summary, BMI, and allows users to export their plan as a PDF.

---

## Features

- Clean, modern UI with a blue/teal color palette
- Personalized 1-week calisthenics workout split
- Gut-friendly, evidence-based diet plan with multiple meal options
- BMI calculation and interpretation
- Hydration and digestion tips
- Export your plan as a PDF
- All user data is confidential and never stored

---

## Demo

![CaliCore Screenshot](https://img.icons8.com/fluency/96/fitness.png)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/calicore.git
cd calicore
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your environment variables

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

**Do not commit your `.env` file to GitHub.**

### 4. Run the app

```bash
streamlit run app.py
```

---

## Deployment

You can deploy this app for free using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push your code to GitHub.
2. Go to Streamlit Cloud, connect your repo, and set `app.py` as the main file.
3. Add your `GOOGLE_API_KEY` as a secret in the Streamlit Cloud settings.

---

## Technologies Used

- [Streamlit](https://streamlit.io/)
- [Google Gemini AI](https://ai.google.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [fpdf](https://pypi.org/project/fpdf/)
- [python-docx](https://pypi.org/project/python-docx/)

---

## License

MIT License

---

## Disclaimer

This app is for informational purposes only and does not replace professional medical advice.  
Consult a healthcare provider before starting any new fitness or nutrition program.

---

