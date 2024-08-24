import streamlit as st
import pickle
import numpy as np

#st.Page(title='heart disease',)
st.title('heart checker :sparkling_heart:')
st.write('give details bellow')

col1,col2,col3= st.columns([3,3,3],vertical_alignment='center')

with col1:
    age = st.number_input(label='age',min_value=0,max_value=100,step=1)
    trestbps= st.number_input('resting blood pressure',min_value=0,step=1)
    restecg= st.selectbox('resting electrocardiographic results',[0,1,2])
    oldpeak= st.number_input('ST depression induced by exercise relative to rest',step=0.1)
    thal= st.selectbox('thal',["low",'normal', "fixed defect", "reversable defect"])

with col2:
    sex= st.selectbox('sex',['male','female'])
    chol= st.number_input('serum cholestoral in mg/dl', step=1)
    thalach=st.number_input('maximum heart rate achieved',step=1)
    slope=st.selectbox('slope of the peak exercise ST segment',[0,1,2])

with col3:
    cp= st.selectbox('chest pain',['null','negligible','mild','extreme'])
    fbs= st.selectbox('fasting blood sugar > 120 mg/dl',['yes','no'])
    exang=st.selectbox('exercise induced angina',['yes','no'])
    ca= st.selectbox('number of major vessels',[0,1,2,3,4])

model= pickle.load(open(r'corrected_heart_disease.pkl','rb'))

#13 functions:
def age_get(value):
    age_v= (value-29)/48
    if age_v<0:
        return 0
    else:
        return age_v
    
def sex_get(value):
    if value == 'male':
        return 1
    else:
        return 0

def cp_get(value):
    if value == 'null':
        return 0
    elif value== 'negligible':
        return 1/3
    elif value== 'mild':
        return 2/3
    elif value== 'extreme':
        return 3/3
    
def trestbps_get(value):
    return (value-94)/106

def chol_get(value):
    return (value-126)/438

def fbs_get(value):
    if value=='yes':
        return 1
    else:
        return 0

def restecg_get(value):
    return value/2

def thalach_get(value):
    return (value-71)/131

def exang_get(value):
    if value== 'yes':
        return 1
    else:
        return 0

def oldpeak_get(value):
    return value/6.2

def slope_get(value):
    return value/2

def ca_get(value):
    return value/4

def thal_get(value):
    if value == "low":
        return 0
    elif value == 'normal':
        return 1/3
    elif value== "fixed defect":
        return 2/3
    elif value== "reversable defect":
        return 3/3
    

feed=[]

button=st.button('submit')

def collect_data():
    feed.append(age_get(age))
    feed.append(sex_get(sex))
    feed.append(cp_get(cp))
    feed.append(trestbps_get(trestbps))
    feed.append(chol_get(chol))
    feed.append(fbs_get(fbs))
    feed.append(restecg_get(restecg))
    feed.append(thalach_get(thalach))
    feed.append(exang_get(exang))
    feed.append(oldpeak_get(oldpeak))
    feed.append(slope_get(slope))
    feed.append(ca_get(ca))
    feed.append(thal_get(thal))

if button:
    collect_data()
    data= np.array(feed)
    out=model.predict(data.reshape(1,-1))

    if out==0:
        st.write("You don't have heart disease")
        st.balloons()
    else:
        st.write("You got heart disease. Go to Clinic or i have a friend who sales coffin")