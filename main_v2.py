import streamlit as st
import pandas as pd

def save_uploaded_file(uploadedfile):
    with open(os.path.join("submition",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("results submitted")

def create_cv():
    st.set_page_config(page_title="CV Creator", page_icon=":guardsman:", layout="wide")
    st.image('images/banner.jpeg',use_column_width='auto')
    st.title("CV Creator")

    # Basic Information
    expander = st.expander("Basic Information")
    with expander:
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        address = st.text_input("address")

    # Skills
    expander = st.expander("Skills")
    with expander:
        skills = st.text_area("Enter your skills separated by commas")

    expander = st.expander("Education")    
    with expander:
        #Education
        with st.form("education", clear_on_submit=True):
            degree = st.selectbox("Degree", ['Course','Primary school', 'bachelor degree','master degree', 'PhD'])
            field_of_study = st.text_input("Field of Study")
            school_name = st.text_input("School/University Name")
            graduation_year = st.date_input("Graduation Year")
            # Every form must have a submit button.
            submitted = st.form_submit_button("submit")
            if submitted:
                with open(full_name+'_education.txt', "a+") as f:
                    f.write(f'{degree},{field_of_study},{school_name},{graduation_year}\n')
                st.write("Submit successfully, submit another if you want!")

    expander = st.expander("Experience")    
    with expander:
        #Experience/Occupation
        with st.form("Experience", clear_on_submit=True):
            occupation = st.text_input("Occupation")
            company = st.text_input("Company")
            job_description = st.text_area("Job Description")
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date (Leave blank if currently employed)")
            # Every form must have a submit button.
            submitted = st.form_submit_button("submit")
            if submitted:
                with open(full_name+'_Experience.txt', "a+") as f:
                    f.write(f'{occupation},{company},{job_description},{start_date},{end_date}\n')
                st.write("Submit successfully, submit another if you want!")
    expander = st.expander("langauge")    
    with expander:
        #langauge
        with st.form("Langauge", clear_on_submit=True):
            Langauge = st.text_input("Langauge")
            Level = st.selectbox("Degree", ['Beginner','Elementary', 'Intermediate','Advance', 'Native'])
            # Every form must have a submit button.
            submitted = st.form_submit_button("submit")
            if submitted:
                with open(full_name+'Langauge.txt', "a+") as f:
                    f.write(f'{Langauge},{Level}\n')
                st.write("Submit successfully, submit another if you want!")




    # Profile Picture
    expander = st.expander("Profile Picture")
    with expander:
        profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
    
    expander = st.expander("package")    
    with expander:
        package = st.multiselect("Package", ['CV in english', 'CV in Arabic'])



    if st.button("Submit data"):
        with open(f"{full_name}.txt", "w") as f:
            if expander.expanded:
                f.write("Full Name: " + full_name + "\n")
                f.write("Email: " + email + "\n")
                f.write("Phone Number: " + phone + "\n")
                f.write("address: " + address + "\n")
            if expander.expanded:
                f.write("Skills: " + skills + "\n")            
            if expander.expanded:
                f.write(f"Package:  {package} \n")

            if expander.expanded:
                if profile_picture:
                    file = f"{full_name}.{profile_picture.name.split('.')[-1]}"
                    with open(file,"wb") as p:
                        p.write(profile_picture.getbuffer())
        st.success("Recorded successfully, will be delivered by .....")

if __name__=="__main__":
    create_cv()
