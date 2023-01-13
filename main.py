import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

def create_cv():
    st.set_page_config(page_title="CV Creator", page_icon=":guardsman:", layout="wide")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    st.title("CV Creator")

    # Basic Information
    st.header("Basic Information")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    location = st.text_input("Location")

    # Skills
    st.header("Skills")
    skills = st.text_area("Enter your skills separated by commas")

    # Education
    st.header("Education")
    degree = st.text_input("Degree")
    field_of_study = st.text_input("Field of Study")
    school_name = st.text_input("School Name")
    graduation_year = st.text_input("Graduation Year")

    # Profile Picture
    st.header("Profile Picture")
    profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])

    if st.button("Create CV"):
        with open("cv.txt", "w") as f:
            f.write("Full Name: " + full_name + "\n")
            f.write("Email: " + email + "\n")
            f.write("Phone Number: " + phone + "\n")
            f.write("Location: " + location + "\n")
            f.write("Skills: " + skills + "\n")
            f.write("Education: " + degree + " in " + field_of_study + " from " + school_name + " (" + graduation_year + ")" + "\n")
            if profile_picture:
                f.write("Profile Picture: " + profile_picture.name + "\n")
        st.success("CV created!")

if __name__=="__main__":
    create_cv()
