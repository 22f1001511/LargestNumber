import streamlit as st

st.title("Find largest of three numbers")

a = st.text_input("Enter first number", "")
b = st.text_input("Enter second number", "")
c = st.text_input("Enter third number", "")

largest = 0
if(st.button("Let's Find")):
    if a == "" or b == "" or c == "":
        st.error("please enter all three numbers")
    else:
        if a > b and a > c:
            largest = a
        if b > a and b > c:
            largest = b
        if c > a and c > b:
            largest = c
        st.text("is the largest of three numbers.".format(largest))
