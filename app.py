#CRIANDO O APP#

import streamlit as st

st.header('Jogando uma moeda')

st.write('Ainda não é um aplicativo funcional. Em construção.')

#Adicionando o controle deslizante e o botão ao programa#

import streamlit as st

st.header('Jogando uma moeda')

number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')

st.write('Ainda não é um aplicativo funcional. Em construção.')

#adicionar os resultados das tentativas à interface do usuário, calcular a média e exibir como ela muda à medida que as tentativas progridem#

import scipy.stats
import streamlit as st
import time

st.header('Jogando uma moeda')

chart = st.line_chart([0.5])

def toss_coin(n): # função que emula o lançamento de uma moeda

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')