#🔐 projeect 02: password strength Meter Sir Zia projeect 3

#📌 Objective:
#Build a password strength Meter in python that evalates a user's pased on security rles.
#The program will:

#Analyze password based on length, character types, and patterns.
#Assign a strength score (weak, Woderate, strong).
#Provide feedback to improve weak password.
#Use contrl flow, type casting, strings, and functions.

# 🔷 Requirements

#1. Password Strength Criteria

#A strong password should:
#✅ Be at least 8 characters long
#✅ Contain uppercase & lowercase letters
#✅ include at least one digit (0-9)
#✅ Have one special character (!@#$%^&*#)

#2. Scoring System

#weak (score: 1-2) ➡ short, missing key elements
#Moderatate (Score: 3-4) ➡ Good but missing some security features
#Strong (Score: 5 ➡ Meets all criteria)

#3. feedback System

#if the password is weak, suggest improvements.
#if the password is Strong, display a success message.

import re
import stremlit as st 

#page styling
st.set_page_config(page_title="password strength checker By Saima Majid", page_icon="🌘"layot="centerec")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextinput {width: 60% !important; margin: auto; }
    .stBtton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover { background-color: #45a049;}
    <style>
    """, unsafe_allow_html=True)

    #page title and decription
    st.title("🔏 Password Strength Generator")
    st.write("Enter yor password below to check its security level. 🔍")

    #fnction to check password strength
    def check_password_strength(password):
        score = 0
        feedback = []

        if len(password) >= 8:
            score += 1 #increased score by 1
        else:
            feedback.append("❌ password should be **atleast 8 character long**cross")

        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", Password):
            score += 1
        else:
            feedback.append("❌ password should include **both uppercase (A-Z) and lowercase (a-z) letters**.") 

        if re.search(r"/d", password):
            score += 1
            else:
                feedback.append("❌ password should include ** at least one number (0-9) **."") 

            #special characters
            if re.search(r"[!@#$%^&*]", password) :
                score += 1
            else:
                feedback.append("❌ include **at least one special characte (!@#$%^&*)**") 

            #display password strength results
            if score == 4:
                st.success("✅ **strong password** - your password is secre.") 
            elif score == 3 :
                st.info("⚠️ **moderate password** - Consider improving security by adding feature") 
            else:
                st.error("❌ **week password** - follow the suggestion below to strength it, ")    

           #feedback
           if feedback:
               with st.expander("🔍**improve your password** ")
                   for item in feedback:
                       st.write(item) 
            password = st.text_input"(Enter your password:", type="password", help="Ensure your password is strong 🔐")  

            #Button working
            if st.button("check strength"):
                if password:
                    check_password_strength(password)
            else:
                st.working("⚠️ please enter a Password first!")  #show warning if password empty                                
    
    
