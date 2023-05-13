import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

#Page config
st.set_page_config(page_title="Heart Disease", page_icon=":anatomical_heart:", layout="wide")

#Create sidebar
with st.sidebar:
    menu=option_menu(menu_title="Main Menu", options=["Home", "Predictions", "Statistics"], icons=["house", "bar-chart-line", "graph-up-arrow"])

#Create horizontal menu
selected=option_menu(menu_title=None, options=["Home", "Predictions", "Statistics"], icons=["house", "bar-chart-line", "graph-up-arrow"], orientation="horizontal")


st.markdown("""
<style>
.css-10pw50.egzxvld1{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


#If selection is home in sidebar
if menu=="Home" or selected=="Home":
    # menu=="Home"
    # selected="Home"
    #Animation
    def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code!=200:
            return None
        return r.json()

    #Header
    st.title("Heart Disease:anatomical_heart:")
    st.write("Heart disease, also known as cardiovascular disease (CVD), refers to a group of conditions that affect the heart and blood vessels. It is a leading cause of death worldwide. Heart disease encompasses various disorders such as coronary artery disease, heart failure, arrhythmias, heart valve problems, congenital heart defects, and others.")
    st.markdown("---")

    #Symptoms
    col1, col2=st.columns(2)
    with col1:
        st.header("What are the symptoms?")
        # st.write("##")
        st.write("""
        Heart disease symptoms depend on the type of heart disease.
        
        - Chest pain, chest tightness, chest pressure and chest discomfort (angina)
        - Shortness of breath
        - Pain in the neck, jaw, throat, upper belly area or back
        - Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in those body areas are narrowed
        """)
    with col2:
        lottie_coding=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_NDRSDjCFia.json")
        st_lottie(lottie_coding, height=300, key="symptoms")

    #Risk
    # col1, col2=st.columns(2)
    # with col1:
    st.header("What are the risk factors?")
    st.write("""
    Risk factors for heart disease include:

    - **Age**: Growing older increases the risk of damaged and narrowed arteries and a weakened or thickened heart muscle.
    - **Sex**: Men are generally at greater risk of heart disease. The risk for women increases after menopause.
    - **High blood pressure**: Uncontrolled high blood pressure can cause the arteries to become hard and thick. These changes interrupt blood flow to the heart and body.
    - **High cholesterol**: Having high cholesterol increases the risk of atherosclerosis. Atherosclerosis has been linked to heart attacks and strokes.
    - **Diabetes**: Diabetes increases the risk of heart disease. Obesity and high blood pressure increase the risk of diabetes and heart disease.
    - **Unhealthy diet**: Diets high in fat, salt, sugar and cholesterol have been linked to heart disease.
    - **Obesity**: Excess weight typically worsens other heart disease risk factors.
    - **Lack of exercises**: Being inactive (sedentary lifestyle) is associated with many forms of heart disease and some of its risk factors, too.
    - **Stress**: Unrelieved stress may damage the arteries and worsen other risk factors for heart disease.
        """)
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
    
    #Preventions
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
    st.write("---")

    #Insert video
    # col1, col2=st.columns(2)
    # with col1:
    st.markdown("<h1 style='text-align:center; '>What is Heart Disease?</h1>", unsafe_allow_html=True)
    st.write("##")
    st.video("HeartVid.mp4")

#If seclection is predictions insidebar
#Used to predict presence of heart disease based on input features
if menu=="Predictions" or selected=="Predictions":
    # menu="Predictions"
    # selected="Predictions"
    st.markdown("<h1 style='text-align:center; '>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    # with st.form("Form 1", clear_on_submit=True):
    with st.form("Form 1"):
    # with st.form("Form 1"):
        #Put into two columns left and right
        col1, col2=st.columns(2)
        #Column 1
        with col1:
            gender=col1.selectbox("Gender", options=("---", "Male","Female"))
            st.write("##")
            trestbps = col1.slider("Resting Blood Pressure (mm Hg)", min_value=100, max_value=200)
            st.write("##")
            fbs=col1.selectbox("Fasting Blood Sugar", options=("---", "Greater than 120 mg/dl", "Lower than 120 mg/dl"))
            st.write("##")
            thalach=col1.slider("Maximum Heart Rate Achieved", min_value=50, max_value=250)
            st.write("##")
            exang=col1.selectbox("Exercise Induced Angina", options=("---", "Yes", "No"))
            st.write("##")
            ca=col1.slider("Number of Major Vessels Colored by Fluoroscopy",  min_value=0, max_value=3)
            st.write("##")
            thal=col1.selectbox("Exercise Induced Angina", options=("---", "Normal", "Fixed Defect", "Reversible Defect"))

        #Column 2
        with col2: 
            age=col2.slider("Age", min_value=0, max_value=100)   
            st.write("##") 
            chest_pain=col2.selectbox("Type Of Chest Pain", options=("---", "Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"))
            st.write("##")
            chol = col2.slider("Serum Cholestoral in mg/dl", min_value=100, max_value=600)
            st.write("##")
            restecg=col2.selectbox("Resting Electrocardiographic Results", options=("---", "Normal", "Having ST-T wave abnormality","showing probable or definite left ventricular hypertrophy"))
            st.write("##")
            oldpeak=col2.slider("ST depression Induced by Exercise Relative to Rest", min_value=0, max_value=7)
            st.write("##")
            slope=col2.selectbox("Slope of the peak exercise ST segment", options=("---", "Unsloping", "Flat","Downsloping"))

        #Submit button
        s_state=st.form_submit_button("Predict")
        #If one of the field is not filled will out warning
        if s_state:
            if gender=="---" or fbs=="---" or  exang=="---" or thal=="---" or  chest_pain=="---" or restecg=="---" or slope=="---":
                st.warning("Please fill in all fields")
            else:
                st.success("Submitted successfully")
                switch_page("results")
                


