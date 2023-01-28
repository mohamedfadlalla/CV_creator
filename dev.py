import streamlit as st
import filestack
import datetime
from my_styles import *
import os
 
    
sp = 7*'#'
 
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def create_cv():
    st.title("CV Creator")


    # Basic Information
    expander = st.expander("Basic information")
    with expander:
        full_name = st.text_input("Enter your full name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        address = st.text_input("Address")
        birth_day = st.date_input("Birth day", min_value=datetime.date(1900,1,1))
        
    # Skills
    expander = st.expander("Skills")
    with expander:
        skills = st.text_area("Skills")
    



      
    #Education       
    expander = st.expander("Education")     
    with expander:      
        with st.form("Education", clear_on_submit=True):
            degree = st.selectbox("", ['Course','Secondary school', 'Diploma', 'bachelor degree','master degree', 'PhD'])
            field_of_study = st.text_input("Field of study")
            school_name = st.text_input("School Name")
            dis_edu = st.text_input("Discrib your Education")
            score = st.text_input("Enter score")
            started = st.date_input("enter year of start")
            graduation_year = st.date_input("year of graduation")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Save")
            if submitted:
                with open(full_name+'_education.txt', "a+") as f:
                    f.write(f'{degree}, {field_of_study}, {school_name}, {graduation_year}, {score}\n{dis_edu}\n')
                st.write("Submission successfull, submit another if you want!")
 

    if st.button("Submit"):
        with open(f"{full_name}.txt", "w") as f:
            if expander.expanded:
                f.write("Full Name: " + full_name + "\n")
                f.write("Email: " + email + "\n")
                f.write("Phone Number: " + phone + "\n")
                f.write("address: " + address + "\n")
            
            if expander.expanded:
                f.write("Skills: " + skills + "\n")            

            if expander.expanded:
                try:
                    f.write(f'{sp}Education section{sp}\n')
                    f.write(open(full_name+'_education.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')

                except FileNotFoundError:
                    f.write(f'{sp}\nNo Education\n{sp}\n\n')


if __name__=="__main__":
    create_cv()
    st.markdown(footer,unsafe_allow_html=True)
