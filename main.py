import streamlit as st
from decimal import Decimal

st.header("Хомякова Лилия Сергеевна, 4 курс, 4 группа, 2023")


def operation(n1, n2, op):
    if op == '+':
        return n1 + n2
    else:
        return n1 - n2


value1, value2 = "", ""
if 'val1' in st.session_state:
    value1 = st.session_state['val1']
if 'val2' in st.session_state:
    value2 = st.session_state['val2']
with st.form("My calculator"):
    num1 = st.text_area(label='Number 1', placeholder='First number', value=value1)
    option = st.selectbox(label='Operation', options=["+", "-"])
    num2 = st.text_area(label='Number 2', placeholder='Second number', value=value2)
    submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            num1 = Decimal(num1.replace(',', '.').replace(' ', ''))
            num2 = Decimal(num2.replace(',', '.').replace(' ', ''))
            st.write(f'Answer: {operation(num1, num2, option):.20f}')
        except:
            st.write('Invalid values')