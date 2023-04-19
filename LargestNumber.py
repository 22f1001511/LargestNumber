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
        val1 = int(a)
        val2 = int(b)
        val3 = int(c)
        if val1 > val2 and val1 > val3:
            largest = val1
        elif val2 > val1 and val2 > val3:
            largest = val2
        else
            largest = val3
        st.text("{}is the largest of three numbers.".format(largest))
