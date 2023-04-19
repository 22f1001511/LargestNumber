import streamlit as st

st.title("Find largest of three numbers")

a = st.text_input("Enter first number", "Type Here ...")
b = st.text_input("Enter second number", "Type Here ...")
c = st.text_input("Enter third number", "Type Here ...")

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

st.text(largest, "is the largest of three numbers.")
