import streamlit as st
import re

st.set_page_config(page_title="Password Strenght Checker", page_icon="🔒", layout="wide")

st.title("Password Strength Checker 🔐")
st.markdown("""
## Welcome to the ultimate password strenght checker!👋
use this simple tool to check the strenght of your password and get suggestion on how to make it stronger.
            we will give you helpfull tips to create a **Stronge Password** 🔒""")

password = st.text_input("Enter your password: ", type="password")

feedback = []

score = 0
if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search("[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Password should have at least one lowercase and one uppercase letter.")
    
    if re.search(r'\d', password):
        score += 1
    else :
        feedback.append("❌ Password should have at least one digit.")

    if re.search(r'[!@#$%&*/]', password):
        score += 1
    else :
        feedback.append("❌ Password should have at least one special character.")
    if score == 4:
        feedback.append("✔️Your password is strong!🎊")
    elif score == 3:
        feedback.append("🚨 Your password is good but can be stronger.")
    else:
        feedback.append("❌ Your password is weak. Please try to make it stronger.")
    
    if feedback:
        st.markdown("## Improvement Suggestion ")
        for tip in feedback:
            st.write(tip)

else:
    st.write("Please enter your password to check its strenght.")