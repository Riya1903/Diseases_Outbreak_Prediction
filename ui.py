import os
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu 

st.set_page_config(page_title='Prediction Of Disease Outbreak'
                   ,layout='wide',page_icon="doctor")
diabetes_model=pickle.load(open(r"C:\Users\Intel\OneDrive\Documents\diseases prediction\training_model\diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"C:\Users\Intel\OneDrive\Documents\diseases prediction\training_model\heart_model.sav",'rb'))
parkisons_model=pickle.load(open(r"C:\Users\Intel\OneDrive\Documents\diseases prediction\training_model\parkisons_model.sav",'rb'))
with st.sidebar:
    selected=option_menu('Prediction Of Disease Outbreak System',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkisons Prediction'],
                         menu_icon='hospital-fill',
                         icons=['activity','heart','person'],
                         default_index=0)
if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number Of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        Bloodpressure=st.text_input('Blood Pressure value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age=st.text_input('Age of person')
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
           diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'
        st.success(diab_diagnosis)
if selected=='Heart Disease Prediction':
    st.title('Heart Diseases Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('Chest Pain types')
    with col1:
        trestbps=st.text_input('Resting Blood Pressure')
    with col2:
        chol=st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs=st.text_input('Fasting Blood Suger >120 mg/dl')
    with col1:
        restecg=st.text_input('Resting Electrocardiographic Result')
    with col2:
        thalach=st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang=st.text_input('Excercise Induced Angina')
    with col1:
        oldpeak=st.text_input('ST depression induced by exercise')
    with col2:
        slope=st.text_input('Slope of peak excercise ST segment ')
    with col3:
        ca=st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal=st.text_input('thal:0=normal; 1=fixed defect;2=reversable effect')
    
    heart_diagnosis=''
    if st.button('Heart Disease Test Result'):
        try:
            # Define user input in a proper list format
            user_input = [
                float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), 
                float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), 
                float(ca), float(thal)
            ]
            # Predict with the model
            heart_prediction = heart_model.predict([user_input])

            # Display result based on prediction
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'

            st.success(heart_diagnosis)
        except Exception as e:
            st.error("Error: {e}")

if selected=="Parkisons Prediction":
    st.title('Parkisons Prediction using ML')
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        fo=st.text_input('MDVP:FO(Hz)',)
    with col2: 
        fhi=st.text_input('MDVP:Fhi(Hz)',key="mdvp_fhi")
    with col3:
        flo=st.text_input('MDVP:Fhi(Hz)',key="mdvp_flo")
    with col4:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs))')
    with col1:
        RAP=st.text_input('MDVP:RAP')
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
    with col3:
        DDP=st.text_input('Jitter:DDP')
    with col4:
        Shimmer=st.text_input('MDVP:Shimmer',key="mdvp_shimmer")
    with col5:
        Shimmer_db=st.text_input('MDVP:Shimmer(db)',key="jitter_percent")
    with col1:
        APQ3=st.text_input('Shimmer:APQ3')
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        APQ=st.text_input('MDVP:APQ')
    with col4:
        DDA=st.text_input('Shimmer')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')
    diab_diagnosis=''
    if st.button('Parkinsons Test Result'):
        try:
            user_input = [
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), 
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_db), 
                float(APQ3), float(APQ5), float(APQ)
            ]
            # Ensure the number of features matches the trained model's expected input
            if len(user_input) != 13:
                st.error("Incorrect number of features. Please ensure you input all the required fields correctly.")
            else:
                # Perform prediction
                parki_prediction = parkisons_model.predict([user_input])
                if parki_prediction[0] == 1:
                    st.success("The person has Parkinson's disease")
                else:
                    st.success("The person does not have Parkinson's disease")
        except Exception as e:
            st.error("Error: {e}")