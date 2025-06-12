# 🧬 BODY-MORPH

**BODY-MORPH** is a modern AI-powered fitness planner that generates personalized workout and nutrition plans using Google Gemini AI.

Transform Your Body, Transform Your Life 💪

---
## DEMO
1. Welcome & User Input Form

When you fire up BODY-MORPH, you’re greeted with a clean header, branded logo, and tagline. Below is the card container where users enter their Name, Age, Gender, Height, and Weight to kick things off.

![Screenshot 2025-06-13 025448](https://github.com/user-attachments/assets/08dbb118-d8e1-4825-9df2-d50583d5541c)
2. Advanced Profile Inputs

Scroll down for the rest of the form: Activity Level, Fitness Goal, Fitness Level, Diet Preference, Allergies, and any Health Conditions you need the plan to respect.
![Screenshot 2025-06-13 025502](https://github.com/user-attachments/assets/ae5c4cf2-48fc-4bca-98bc-e68d1bdeee34)

3. Personalized Plan Generation

After clicking Generate My Plan, the app greets you by name, calculates your BMI (with an emoji-style badge), and confirms your weight category before diving into the details. 1-Week Calisthenics Split (Part 1)
The first half of your tailored 7-day calisthenics program: Monday through Wednesday, showing focus areas (Pull/Core, Legs/Push, Rest) along with exercises, sets, reps, and rest intervals. 1-Week Calisthenics Split (Part 2)

![Screenshot 2025-06-13 025637](https://github.com/user-attachments/assets/d980df59-0672-4e98-a872-b0a4762c4775)

Finishing out Thursday–Sunday, including core/pull, leg/push, full-body days, and active recovery, so you know exactly what to do each day.

4. Gut-Friendly Diet Plan Intro

Jump into the Lactose-Free, Non-Vegetarian diet framework. A quick reminder to adjust portions based on your unique caloric needs.
![Screenshot 2025-06-13 025651](https://github.com/user-attachments/assets/96a24717-f5df-4d69-af1d-552c91eff3e2)

5. Meal Options Table

Five swap-and-mix options for Breakfast, Lunch, and Dinner—from oatmeal and yogurt to chicken stir-fries and salmon—designed to support gut health and muscle recovery.
![Screenshot 2025-06-13 025702](https://github.com/user-attachments/assets/a8ebf879-4ef7-4529-bf4d-12ddf8806ba1)

6. BMI Interpretation & Health Tips

More than just numbers. This section breaks down what your BMI means and gives you actionable bullet-point advice on body composition, strength training, consistency, and balanced nutrition.
![Screenshot 2025-06-13 025713](https://github.com/user-attachments/assets/fc2ca8ec-98b2-4c0c-9242-7f1449ce41eb)

7. Hydration, Digestion & Download

Finish strong with hydration and digestion best practices (probiotics, prebiotics, stress management) plus a one-click Download as PDF so you can take your custom plan anywhere.

![Screenshot 2025-06-13 025729](https://github.com/user-attachments/assets/5bded0b2-951b-4ced-a01d-18874e9e333a)


## ✨ Features

- 🎨 Clean, modern UI with green health-focused theme
- 🏋️ Personalized **1-week calisthenics workout split**
- 🥗 **Gut-friendly diet plans** with multiple meal options
- 📊 BMI calculation and health interpretation
- 💧 Hydration and digestion recommendations
- 📄 **PDF download** of your complete plan
- 🔐 Secure - no data stored, privacy protected
- 📱 Mobile-responsive design

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/vigneshkriishna/BODY-MORPH.git
cd BODY-MORPH
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set up your Google API key
1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.streamlit/secrets.toml` file:
```toml
[default]
GOOGLE_API_KEY = "your_api_key_here"
```

### 4️⃣ Run the application
```bash
streamlit run app.py
```

---

## 📋 How to Use

1. **Fill out the form** with your personal details:
   - Name, age, gender
   - Height and weight
   - Activity level and fitness goals
   - Diet preferences and health conditions

2. **Generate your plan** - Click the "🚀 Generate My Plan" button

3. **Review your personalized plan** including:
   - Weekly workout schedule
   - Gut-friendly meal plans
   - BMI analysis and health tips
   - Hydration guidelines

4. **Download as PDF** - Save your complete plan for offline access

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI**: Google Gemini 1.5 Flash
- **PDF Generation**: FPDF
- **Styling**: Custom CSS with responsive design
- **Deployment**: Ready for Streamlit Cloud

---

## 📱 Mobile Responsive

BODY-MORPH is optimized for all devices:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Laptops and desktops

---

## ⚠️ Disclaimer

This application provides general fitness and nutrition suggestions based on the information you provide. It is not medical advice and should not replace consultation with healthcare professionals. Always consult with a doctor before starting any new fitness or diet program.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Developer

Created by **@Vignesh** 

🌟 If you find this helpful, please star the repository!
