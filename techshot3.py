import streamlit as st
import pandas as pd
import pickle
import requests
import subprocess
import sys
package = 'scikit-learn'
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
from sklearn.linear_model import LinearRegression

st.title('Previsão de vendas')

item_id = st.selectbox('Selecione o id do produto:', list(range(1, 21798)))

item_category_id = st.selectbox('Selecione o id da categoria do produto:', list(range(1, 85)))

shop_id = st.selectbox('Selecione o id da loja:', list(range(1,61)))

month = st.selectbox('Selecione o mês da previsão:', list(range(1, 13)))

year = st.selectbox('Selecione o ano da previsão:', list(range(2015, 2017)))

monday = st.selectbox('Insira a quantidade de segundas-feiras no mês:', list(range(3, 6)))
tuesday = st.selectbox('Insira a quantidade de terças-feiras no mês:', list(range(3, 6)))
wednesday = st.selectbox('Insira a quantidade de quartas-feiras no mês:', list(range(3, 6)))
thursday = st.selectbox('Insira a quantidade de quintas-feiras no mês:', list(range(3, 6)))
friday = st.selectbox('Insira a quantidade de sextas-feiras no mês:', list(range(3, 6)))
saturday = st.selectbox('Insira a quantidade de sábados no mês:', list(range(3, 6)))
sunday = st.selectbox('Insira a quantidade de domingos no mês:', list(range(3, 6)))

test_data = {
    'item_id' : [item_id],
    'shop_id' : [shop_id],
    'item_category_id' : [item_category_id],
    'month' : [month],
    'year' : [year],
    'Monday' : [monday],
    'Tuesday' : [tuesday],
    'Wednesday' : [wednesday],
    'Thursday' : [thursday],
    'Friday' : [friday],
    'Saturday' : [saturday],
    'Sunday' : [sunday]
}

test_data = pd.DataFrame(test_data)

'''with open('model.pickle', 'wb') as out_file:
    content = requests.get('https://github.com/gabriel-leite30/techshot3/raw/main/model.pickle', stream=True).content
    out_file.write(content)'''

with open('model.pickle', 'rb') as input_file:
    model = pickle.load(input_file)


prediction = model.predict(test_data)

st.write(f'A previsão de vendas do produto é de: {prediction[0]}')