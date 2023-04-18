# -*- coding: utf-8 -*-
"""App_findLargest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IYoAgrVtLu0amiSNHNTmdOhJnvHyB0j_
"""

import streamlit as st

def largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Define the Streamlit app
def app():
    st.title("Find the largest among three numbers")
    st.subheader("Enter any three numbers below")
    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")
    num3 = st.number_input("Enter the third number")

    if st.button("Find largest number"):
        result = largest_number(num1, num2, num3)
        st.write("The largest number is:", result)
     
app()
