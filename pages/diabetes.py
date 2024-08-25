import streamlit as st
import sklearn
import pickle
import numpy as np
import json


st.title('Diabetes :ice_cube:')

with open('help.json', 'r') as file:
   info = json.load(file)
  
hypertension_info= info['Diabetes']["Hypertension"]
bmi_info= info['Diabetes']["Body Mass Index"]
hbac1_info= info['Diabetes']["Hemoglobin A1c"]
glucose_info= info['Diabetes']["Blood glucose"]


model= pickle.load(open(r'corrected_diabetes.pkl','rb'))

col1,col2,col3= st.columns([3,3,3],vertical_alignment='center',)

with col1:
    gender= st.selectbox('gender',['Male','Female','Other'])
    Heart_disease= st.selectbox('Heart disease',['Yes', 'No'])
    Hemoglobin_A1c_level= st.number_input("Hemoglobin A1c level",min_value=0.0,step=0.1,help=str(hbac1_info))

    

with col2:
    age= st.number_input('age',min_value=0,step=1)
    Smoking_history= st.selectbox('Smoking history',["never","No Info","current","former","ever","not current"])
    Blood_glucose= st.number_input('Blood glucose',min_value=0,step=1,help=str(glucose_info))
    

with col3:
    hypertension= st.selectbox('hypertension',['No','Yes'],help=str(hypertension_info))
    BMI= st.number_input("BMI",min_value=0.00,step=0.01,help=str(bmi_info))


button= st.button('submit')

feed=[]

def gender_changer(x):
  if x=='Male':
    return 1
  elif x=='Female':
    return 2
  else:
    return 0
  
def smoke_change(value):
  if value == 'never':
    return 0
  elif value == 'No Info':
      return 1
  elif value == 'current':
      return 2
  elif value == 'former':
      return 3
  elif value == 'ever':
      return 4
  elif value == 'not current':
    return 5

def bmi_get(value):
   return (value-10.01)/85.68

def hb1ac_get(value):
   return (value-3.5)/5.5

def glucose_get(value):
   return (value-80)/220

def hypten_get(value):
   if value == 'No':
      return 0
   else:
      return 1
   
def hert_dis(value):
   if value== 'No':
      return 0
   else:
      return 1

def collect_data():
    feed.append((age/80))
    feed.append(bmi_get(BMI))
    feed.append(hb1ac_get(Hemoglobin_A1c_level))
    feed.append(glucose_get(Blood_glucose))
    feed.append(gender_changer(gender))
    feed.append(hypten_get(hypertension))
    feed.append(hert_dis(Heart_disease))
    feed.append(smoke_change(Smoking_history))
    


if button:
  collect_data()
  data= np.array(feed)
  out=model.predict(data.reshape(1,-1))
  
  if out==0:
    st.write("You don't have diabetes")
    st.balloons()
  else:
    st.write("You got diabates. Go to Clinic")


