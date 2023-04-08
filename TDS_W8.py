import streamlit as st

st.header("Largest Number")
st.write("""This app finds out largest number among three inputs from the user.""")
num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")
num3 = st.number_input("Third Number")

arr = [num1,num2,num3]
arr.sort()
st.write("""Largest number is """,arr[-1])
