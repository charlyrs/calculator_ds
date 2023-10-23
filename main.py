import streamlit as st
import math
import decimal
from decimal import Decimal

st.header("Хомякова Лилия Сергеевна, 4 курс, 4 группа, 2023")


def operation(n1: Decimal, n2: Decimal, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1/n2
    return 0


value1, value2 = "", ""
if 'val1' in st.session_state:
    value1 = st.session_state['val1']
if 'val2' in st.session_state:
    value2 = st.session_state['val2']
with st.form("My calculator"):
    num1 = st.text_area(label='Number 1', placeholder='First number', value=value1)
    option = st.selectbox(label='Operation', options=["+", "-", "*", "/"])
    num2 = st.text_area(label='Number 2', placeholder='Second number', value=value2)
    submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            num1 = Decimal(num1.replace(',', '.').replace(' ', ''))
            num2 = Decimal(num2.replace(',', '.').replace(' ', ''))
            if num2 == 0 and option == "/":
                st.write("Cannot devide by zero")
            else:
                six_digits = Decimal('0.000001')
                ans = operation(num1, num2, option).quantize(six_digits,rounding=decimal.ROUND_HALF_UP)
                ans = '{:,}'.format(ans).replace(',', ' ')
                ans = ans.rstrip("0")
                if ans[-1] == '.':
                    ans = ans[:-1]
                st.write(f'Answer: {ans}'.replace(',', '.'))
        except:
            st.write('Invalid values')