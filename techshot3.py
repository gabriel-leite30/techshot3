import streamlit as st
import pandas as pd
import pickle


st.title('Risco de AVC')

gender = st.selectbox('Selecione o sexo:', ['Masculino', 'Feminino'])
if gender == 'Masculino': gender = 1 
else: gender = 0

age = st.slider('Selecione a idade:', 0, 100)

hypertension = st.selectbox('É hipertenso? :', ['Sim', 'Não'])
if hypertension == 'Sim': hypertension = 1 
else: hypertension = 0

heart_disease = st.selectbox('Possui doença cardiovascular?', ['Sim', 'Não'])
if heart_disease == 'Sim': heart_disease = 1 
else: heart_disease = 0

ever_married = st.selectbox('Já foi casado?', ['Sim', 'Não'])
if ever_married == 'Sim': ever_married = 1 
else: ever_married = 0

work_type = st.selectbox('Trabalho', ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])

residence_type = st.selectbox('Moradia', ['Urban', 'Rural'])

avg_glucose_level = st.slider('Selecione o nível de glicose médio:', 40, 300)

bmi = st.slider('Insira o BMI:', 3, 100)

smoking_status = st.selectbox('Fuma', ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])





test_data = {
    'gender' : [gender],
    'age' : [age],
    'hypertension' : [hypertension], 
    'heart_disease' : [heart_disease],
    'ever_married' : [ever_married],
    'avg_glucose_level' : [avg_glucose_level],
    'bmi' : [bmi], 
    'Govt_job' : [0], 
    'Never_worked' : [0],
    'Private' : [0], 
    'Self-employed' : [0], 
    'children' : [0], 
    'Rural' : [0], 
    'Urban' : [0], 
    'Unknown' : [0],
    'formerly smoked' : [0], 
    'never smoked' : [0], 
    'smokes' : [0]
}

test_data[work_type] = 1
test_data[residence_type] = 1
test_data[smoking_status] = 1

test_data = pd.DataFrame(test_data)

with open('model.pickle', 'rb') as input_file:
    model = pickle.load(input_file)

prediction = model.predict_proba(test_data)

st.metric(label="Probabilidade de um AVC", value=f'{round(prediction[0][1],4)*100}%')
