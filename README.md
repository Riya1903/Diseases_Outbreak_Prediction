# Diseases_Outbreak_Prediction
🩺 Prediction of Disease Outbreak using Machine Learning
This project is a Streamlit-based web application designed to predict the likelihood of Diabetes, Heart Disease, and Parkinson's Disease using pre-trained machine learning models. It enables users to enter medical data and receive real-time disease risk predictions, assisting in early detection and proactive healthcare measures.
## 🚀 Features

✅ 1. Diabetes Prediction
**Predicts diabetes risk based on input parameters such as:
- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
 - Age

❤️ 2. Heart Disease Prediction
**Evaluates heart disease risk using:
- Age, Sex, and Chest Pain Type
- Resting Blood Pressure & Serum Cholesterol
- Fasting Blood Sugar Levels
- Resting Electrocardiographic Results
- Maximum Heart Rate Achieved
- Exercise-Induced Angina & ST Depression
- Slope of Peak Exercise ST Segment
- Major Vessels Colored by Fluoroscopy
9) Thalassemia Test Results

🧠 3. Parkinson’s Disease Prediction
** Analyzes voice-related features to detect Parkinson’s symptoms:
- Fundamental Frequency (MDVP:Fo, MDVP:Fhi, MDVP:Flo)
- Jitter and Shimmer Parameters
- Harmonics-to-Noise Ratio (HNR)

- Recurrence Period Density Entropy (RPDE)
5) Dynamical Complexity (DFA, Spread, D2, PPE)
## 🛠 Tech Stack
- Python
- Streamlit – For building an interactive web UI
- Scikit-learn – For machine learning models
- Pickle – For model serialization
- Pandas & NumPy – For data preprocessing
## ⚙️ Installation & Setup
1️⃣ Clone the Repository
  -  bash

2️⃣ Install Dependencies
  -  bash
         pip install -r requirements.txt

3️⃣ Run the Application

- bash
        streamlit run ui.py
## 📊 Machine Learning Models Used

The models are trained using supervised learning algorithms to classify patients as positive or negative for a particular disease.

- Diabetes Model: Trained on the PIMA Indian Diabetes Dataset
- Heart Disease Model: Based on the Cleveland Heart Disease Dataset
- Parkinson’s Model: Uses Parkinson's Telemonitoring Dataset
#### ** Classification Algorithms Used:  

✔ Logistic Regression  

✔ Random Forest  

✔ Decision Tree  

✔ Support Vector Machine (SVM)  


## 🛡️ Model Performance & Evaluation
-  Achieved 80-90% accuracy across different models.
-  Evaluated using Precision, Recall, F1-score, and ROC-AUC Score.
💡 Future Improvements

🔹  Integrate Deep Learning Models for higher accuracy
🔹  Add a real-time API for mobile app integration
🔹  Improve UI with interactive data visualizations
🔹  Include more diseases for prediction

## 👩‍💻 Contributing  

  We welcome contributions! Feel free to fork the repo, open issues, and submit pull 
  requests.
## 📜 License  

   This project is licensed under the MIT License.
  
