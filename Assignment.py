
import streamlit as st 
import requests 
import pickle
from sklearn.preprocessing import StandardScaler
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import openai

# Open the pickle file in read binary mode
with open("/Users/pohsharon/Downloads/ML Assignment/xgb.pkl", "rb") as file:
    # Load the model from the pickle file
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="CardiaRisk!", page_icon=":anatomical_heart:", layout="wide")

# Create sidebar
with st.sidebar:
    menu = option_menu(menu_title="Main Menu", options=["Home", "Predictions", "Statistics"], icons=["house", "bar-chart-line", "graph-up-arrow"])

st.markdown("""
<style>
.css-164nlkn.e1g8pov61{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# If selection is home in sidebar
if menu == "Home":
    # Animation
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Header
    st.title("Welcome to CardiaRisk!:anatomical_heart:")
    st.write("Heart disease, also known as cardiovascular disease (CVD), refers to a group of conditions that affect the heart and blood vessels. It is a leading cause of death worldwide. Heart disease encompasses various disorders such as coronary artery disease, heart failure, arrhythmias, heart valve problems, congenital heart defects, and others.")
    st.markdown("---")

    # Symptoms
    col1, col2 = st.columns(2)
    with col1:
        st.header("What are the symptoms?")
        st.write("""
        Heart disease symptoms depend on the type of heart disease.
        
        - Chest pain, chest tightness, chest pressure and chest discomfort (angina)
        - Shortness of breath
        - Pain in the neck, jaw, throat, upper belly area or back
        - Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in those body areas are narrowed
        """)
    with col2:
        lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_NDRSDjCFia.json")
        st_lottie(lottie_coding, height=300, key="symptoms")

    # Risk
    st.header("What are the risk factors?")
    st.write("""
    Risk factors for heart disease include:

    - **Age**: Growing older increases the risk of damaged and narrowed arteries and a weakened or thickened heart muscle.
    - **Sex**: Men are generally at greater risk of heart disease. The risk for women increases after menopause.
    - **High blood pressure**: Uncontrolled high blood pressure can cause the arteries to become hard and thick. These changes interrupt blood flow to the heart and body.
    - **High cholesterol**: Having high cholesterol increases the risk of atherosclerosis. Atherosclerosis has been linked to heart attacks and strokes.
    - **Diabetes**: Diabetes increases the risk of heart disease. Obesity and high blood pressure increase the risk of diabetes and heart disease.
    - **Unhealthy diet**: Diets high in fat, salt, sugar and cholesterol have been linked to heart disease.
    - **Obesity**: Obesity is associated with high blood cholesterol levels, high triglyceride levels, high blood pressure and diabetes. Losing even a small amount of weight can help reduce heart disease risk.
    - **Physical inactivity**: Lack of exercise is associated with many forms of heart disease and some of its other risk factors, as well.
    - **Stress**: Unrelieved stress may damage arteries and worsen other risk factors for heart disease.
    - **Family history of heart disease**: A family history of heart disease increases your risk of coronary artery disease, especially if a parent developed it at an early age (before age 55 for a male relative, such as your brother or father, and 65 for a female relative, such as your mother or sister).
    """)

    # Prevention
    col1, col2=st.columns(2)
    with col1:
        st.header("How to prevent?")
        st.write("""
    The same lifestyle changes used to manage heart disease may also help prevent it. Try these heart-healthy tips:

    - Don't smoke.
    - Eat a diet that's low in salt and saturated fat.
    - Exercise at least 30 minutes a day on most days of the week.
    - Maintain a healthy weight.
    - Reduce and manage stress.
    - Control high blood pressure, high cholesterol and diabetes.
    - Get good sleep. Adults should aim for 7 to 9 hours daily.
        """)
    with col2:
        lottie_coding=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_m2hrollf.json")
        st_lottie(lottie_coding, height=300, key="prevent")
    st.write("##")

    #Treatments
    st.header("What are the treatments?")
    st.write("""
    The treatment options will vary depending on the type of heart disease a person has, but some common strategies include making lifestyle changes, taking medications, and undergoing surgery.
    """)
    st.subheader("**Medications**")
    st.write("""
    The main options include:

    - Anticoagulants: Also known as blood thinners, these medications can prevent clots. 
    - Antiplatelet therapies: These include aspirin, and they can also prevent clots.
    - Angiotensin-converting enzyme inhibitors: These can help treat heart failure and high blood pressure by causing the blood vessels to expand. 
    - Angiotensin II receptor blockers: These can also control blood pressure. 
    - Angiotensin receptor neprilysin inhibitors: These can help unload the heart and interrupt the chemical pathways that weaken it.
    - Beta-blockers: Metoprolol and other medications in this class can reduce the heart rate and lower blood pressure. They can also treat arrhythmias and angina.
    - Calcium channel blockers: These can lower blood pressure and prevent arrhythmias by reducing the pumping strength of the heart and relaxing the blood vessels. 
    """)

    st.subheader("**Surgery**")
    st.write("""

    Some common types of surgeryTrusted Source include:

    - Coronary artery bypass surgery: This allows blood flow to reach a part of the heart when an artery is blocked. Coronary artery bypass grafting is the most common surgery. A surgeon can use a healthy blood vessel from another part of the body to repair a blocked one.
    - Coronary angiography: This is a procedure that widens narrow or blocked coronary arteries. It is often combined with the insertion of a stent, which is a wire-mesh tube that allows easier blood flow.
    - Valve replacement or repair: A surgeon can replace or repair a valve that is not functioning correctly.
    - Repair surgery: A surgeon can repair congenital heart defects, aneurysms, and other problems.
    - Device implantation: Pacemakers, balloon catheters, and other devices can help regulate the heartbeat and support blood flow.
        """)
    st.write("##")

    st.write("---")
    st.markdown("<h1 style='text-align:center; '>What is Heart Disease?</h1>", unsafe_allow_html=True)
    st.write("##")
    st.video("HeartVid.mp4")

# If selection is predictions in sidebar
elif menu == "Predictions":
    st.markdown("<h1 style='text-align:center; '>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    with st.form("Form 1"):
        col1, col2=st.columns(2)
    # Features
        with col1:
            sex = st.selectbox("Sex", options=["Male", "Female"])
            trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, step=1, value=120, help="Diastolic blood pressure")
            fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=["False", "True"], help="Glucose level after fasting")
            thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, step=1, value=150)
            exang = st.selectbox("Exercise induced agina", options=["No", "Yes"], help="Chest pain or discomfort during physical activity") 
            ca = st.number_input("Number of Major Vessels (0-3) Colored by Fluoroscopy", min_value=0, max_value=3, step=1, value=0)
            thal = st.selectbox("Thalassemia", options=["Normal", "Fixed Defect", "Reversible Defect"])

        with col2:
            age = st.number_input("Age", min_value=1, max_value=100, step=1, value=50)
            cp = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
            chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0, max_value=1000, step=1, value=200)
            restecg = st.selectbox("Resting Electrocardiographic Results", options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
            oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, step=0.1, value=1.0)
            slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=["Upsloping", "Flat", "Downsloping"])
    
            # # Get GPT-3 api key
            # openai.api_key="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"
            # # Generate text
            # response = openai.Completion.create(
            #     engine="text-davinci-002",
            #     prompt="Age: " + str(age) + " Sex: " + sex + " trestbps(mmHg): " + str(trestbps) + " Fasting blood sugar greater than 120mmHg: " + fbs + " Maximum heart rate: " +
            #     str(thalach) + " Discomfort during physical activities: " + exang + " Number of blood vessels colored by fluoroscopy: " + str(ca) + " Thalassemia is " +
            #     thal + " Chest pain type: " + cp + " Serum cholesterol(mg/dL): " + str(chol) + " Resting Electrocardiographic Results: " + restecg +
            #     " ST Depression Induced by Exercise Relative to Rest: " + str(oldpeak) + " Slope of the Peak Exercise ST Segment: " + slope +
            #     " Please give some comments",
            #     max_tokens=1000,
            #     temperature=1.0
            # )

            # res = response.choices[0].text

            # Convert categorical features to numerical
            sex = 1 if sex == "Male" else 0
            cp_dict = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
            cp = cp_dict[cp]
            fbs = 1 if fbs == "True" else 0
            restecg_dict = {"Normal": 0, "ST-T Wave Abnormality": 1, "Left Ventricular Hypertrophy": 2}
            restecg = restecg_dict[restecg]
            exang = 1 if exang == "Yes" else 0
            slope_dict = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
            slope = slope_dict[slope]
            thal_dict = {"Normal": 3, "Fixed Defect": 6, "Reversible Defect": 7}
            thal = thal_dict[thal]

            # Create feature vector
            features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

            # Open the pickle file in read binary mode
            with open("/Users/pohsharon/Downloads/ML Assignment/scaler.pkl", "rb") as file:
                # Load the model from the pickle file
                scaler = pickle.load(file)
                
            # Standardize features
            features = scaler.transform([features])

            # Make prediction
            prediction = model.predict(features)

            #Submit button
            st.write("\n\n")
        s_state=st.form_submit_button(label="Predict", help='Click to predict')
        st.write("\n\n")
        if s_state:
            if prediction[0]==1:
            # Display the warning message
                st.warning("Heart disease is detected! Please consult a doctor immediately!")
            else:
                st.success("No heart disease is detected")
            # st.dropbox()
            # #Make a checkbox
            # def change():
            #     print(st.session_state.checker)
            # state=st.checkbox("Click to see analysis", value=True, on_change=change, key="checker")
            # if state:
            #     st.info(res)
            # else :
            #     pass

# If selection is statistics in sidebar
elif menu == "Statistics":
    st.title("Heart Disease Statistics")

    st.subheader("Age")
    st.write("Age is a significant risk factor for heart disease. As individuals age, their risk increases due to factors like high blood pressure, high cholesterol, diabetes, obesity, and a sedentary lifestyle. Structural changes in the heart, atherosclerosis, and decreased regenerative capacity contribute to the higher risk. However, proactive health monitoring, lifestyle modifications, and risk factor management can help mitigate age-related heart disease risk and promote cardiovascular well-being.")
    age_exp=st.expander("Show more")
    age_exp.image("Age.png")

    st.subheader("Gender")
    st.write("Men generally have a higher risk of developing heart disease compared to premenopausal women. However, after menopause, women's risk increases and becomes similar to that of men. The hormonal changes associated with menopause, along with age-related factors, contribute to this shift. Additionally, women may experience different symptoms of heart disease compared to men, such as atypical chest pain or shortness of breath. It is crucial for both men and women to be aware of their risk factors, maintain a healthy lifestyle, and seek medical attention if they experience any concerning symptoms.")
    gender_exp=st.expander("Show more")
    gender_exp.image("Gender.png")

    st.subheader("Major Vessels Total")
    st.write("The number of major vessels affected by blockages is a crucial factor in determining the severity of heart disease. More blockages in the major vessels indicate a higher risk of complications, such as heart attacks. Fewer affected vessels suggest a lower risk and milder symptoms. Diagnostic tests help assess the extent of blockages, guiding appropriate treatment for better cardiovascular health.")
    vessel_exp=st.expander("Show more")
    vessel_exp.image("MajorVessel.png")
