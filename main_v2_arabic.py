import streamlit as st
import os
import dropbox



def create_cv():
    st.set_page_config(page_title="CV Creator", page_icon=":guardsman:", layout="wide")
    st.image('images/banner.jpeg',use_column_width='auto')
    st.title("CV Creator")

    # Basic Information
    expander = st.expander("�������� �������")
    with expander:
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        address = st.text_input("address")

    # Skills
    expander = st.expander("مهاراتك ")
    with expander:
        skills = st.text_area("أدخل مهاراتك مفصولة بفواصل")

    expander = st.expander("Education")    
    with expander:
        #Education
        with st.form("تعليم", clear_on_submit=True):
            degree = st.selectbox("الدرجة العلمية", ['Course','Primary school', 'bachelor degree','master degree', 'PhD'])
            field_of_study = st.text_input("مجال الدراسة")
            school_name = st.text_input("اسم المدرسة / الجامعة")
            graduation_year = st.date_input("سنة التخرج")
            # Every form must have a إرسال button.
            submitted= st.form_submit_button("Submit")
            if submitted:
                with open(full_name+'_education.txt', "a+") as f:
                    f.write(f'{degree},{field_of_study},{school_name},{graduation_year}\n')
                st.write("إرسال successfully, إرسال another if you want!")

    expander = st.expander("Experience")    
    with expander:
        #Experience/Occupation
        with st.form("خبرة", clear_on_submit=True):
            occupation = st.text_input("المسمى الوظيفي")
            company = st.text_input("شركة")
            job_description = st.text_area("")
            start_date = st.date_input("تاريخ البدء")
            end_date = st.date_input("تاريخ الانتهاء")
            # Every form must have a إرسال button.
            submitted = st.form_submit_button("submit")
            
            if submitted:
                with open(full_name+'_Experience.txt', "a+") as f:
                    f.write(f'{occupation},{company},{job_description},{start_date},{end_date}\n')
                st.write("إرسال successfully, إرسال another if you want!")
    
    expander = st.expander("langauge")    
    with expander:
        #langauge
        with st.form("Langauge", clear_on_submit=True):
            Langauge = st.text_input("Langauge")
            Level = st.selectbox("Degree", ['Beginner','Elementary', 'Intermediate','Advance', 'Native'])
            # Every form must have a إرسال button.
            submited = st.form_submit_button("إرسال")
            if submited:
                with open(full_name+'Langauge.txt', "a+") as f:
                    f.write(f'{Langauge},{Level}\n')
                st.write("")

    # templates
    expander = st.expander("template")    
    with expander:
        template = st.selectbox("Choose a template", ['1','2', '3','4'])  
        col1, col2 = st.columns(2)
        col1.image('images/1.jpeg',caption=1, use_column_width=True)
        col2.image('images/2.jpeg',caption=2, use_column_width=True)
        col1.image('images/3.jpeg',caption=3, use_column_width=True)
        col2.image('images/4.jpeg',caption=4, use_column_width=True)

    # Profile Picture
    expander = st.expander("Profile Picture")
    with expander:
        profile_picture = st.file_uploader("Picture", type=["jpg", "jpeg", "png"])
    
    expander = st.expander("package")    
    with expander:
        package = st.multiselect("", ["CV in Arabic", "CV in English"])
        # if package:
        #     st.write('your total is 1500SDG')
        #     st.write('send it to this notification to 123345626')
        #     st.



    if st.button("إرسال data"):
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
                f.write(f"template:  {template} \n")


            if expander.expanded:
                if profile_picture:
                    file = f"{full_name}.{profile_picture.name.split('.')[-1]}"
                    with open(file,"wb") as p:
                        p.write(profile_picture.getbuffer())

        dbx = dropbox.Dropbox(st.secrets["DROPBOX"])
        # list files needed to be uploaded
        files = os.listdir()
        files = [file for file in files if file.startswith(full_name)]
        
        # Upload files
        with st.spinner('Processing..'):
            for file in files:
                with open(file, "rb") as f:
                    # Upload the file to Dropbox
                    dbx.files_upload(f.read(), f"/{file}", 
                        mode=dropbox.files.WriteMode.overwrite)
        st.success("Your total is **1500** SDG")
        st.success("Order received contact us for confirmation at 0125836305")
        


if __name__=="__main__":
    create_cv()



#write 3 to 5 polits points of desicriptoin
