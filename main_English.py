import streamlit as st
import filestack
import datetime
from my_styles import *
import os

total = 0
sp = 7*'#'


        
def create_cv():
    st.set_page_config(page_title="CV Creator", page_icon=":guardsman:", layout="wide")
    st.image('images/banner.jpeg',use_column_width='auto')
    st.title("CV Creator")

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Basic Information
    expander = st.expander("Basic information")
    with expander:
        full_name = st.text_input("Enter your full name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        address = st.text_input("Address")
        birth_day = st.date_input("Birth day", min_value=datetime.date(1900,1,1))
        title = st.text_input("المسمى الوظيفي")
        linkedin = st.text_input("Enter linkedin account") 
        profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
        
    # Skills
    expander = st.expander("Skills")
    with expander:
        skills = st.text_area("Skills")

    #Education
    expander = st.expander("Education")    
    with expander:
        with st.form("Education", clear_on_submit=True):
            degree = st.selectbox("", ['Course','Secondary school', 'Diploma', 'bachelor degree','master degree', 'PhD'])
            field_of_study = st.text_input("مجال الدراسة")
            school_name = st.text_input("أسم الجامعة \ المدرسة")
            dis_edu = st.text_input("بحث التخرج")
            score = st.text_input("المعدل التراكمي")
            graduation_year = st.date_input("سنة التخريج")

            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_education.txt', "a+") as f:
                    f.write(f'{degree}, {field_of_study}, {school_name}, {graduation_year}, {score}\n{dis_edu}\n')
                st.write("Submission successfull, submit another if you want!")
 
    #Experience/Occupation
    expander = st.expander("الخبرة")    
    with expander:
        with st.form("الخبرة", clear_on_submit=True):
            occupation = st.text_input("المسمي الوظيفي")
            company = st.text_input("الشركة / المؤسسة")
            where = st.text_input("منطقة العمل")
            job_description = st.text_area("تحدث في ما لا يقل عن ثلاث نقاط عن مهام وظيفتك")
            start_date = st.date_input("تاريخ البداْ", min_value=datetime.date(1900,1,1))
            work_here = st.checkbox("أعمل هنا")
            end_date = st.date_input("تاريخ الانتهاْ (دعه فارغا اذا كنت تعمل هتا)")
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Experience.txt', "a+") as f:
                    f.write(f'{occupation},{company},{job_description},{start_date},{work_here},{end_date}\n')
                st.write("Submission successfull, submit another if you want!")
    
    #Publications
    expander = st.expander("Publications")    
    with expander:
        with st.form("Publications", clear_on_submit=True):
            title_publicaiton = st.text_input("Tilte of publication")
            publisher = st.text_input("publisher")
            year = st.text_input("Year of publication")
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Publicaitons.txt', "a+") as f:
                    f.write(f'{title_publicaiton}--{publisher}--{year}\n')
                st.write("Submission successfull, submit another if you want!")
    
    #Projects
    expander = st.expander("Projects")    
    with expander:
        with st.form("Projects", clear_on_submit=True):
            title_project = st.text_input("Enter the title of your project")
            description_project = st.text_input("Describ your project")
            date_project = st.date_input("Enter the date of your project")
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Projects.txt', "a+") as f:
                    f.write(f'{title_project}--{date_project}\n{description_project}\n')
                st.write("Submission successfull, submit another if you want!")

    #Volunteering
    expander = st.expander("Volunteering")    
    with expander:
        with st.form("Volunteering", clear_on_submit=True):
            title_volunteer = st.text_input("Enter title of your work")
            description_volunteer = st.text_input("Describ your work")
            date_volunteer = st.text_input("Enter the data of Volunteering")


            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Volunteer.txt', "a+") as f:
                    f.write(f'Volunteering:  {title_volunteer}--{date_volunteer}\n{description_volunteer}\n')
                st.write("Submission successfull, submit another if you want!")

    #Recommendations 
    expander = st.expander("Recommendations ")    
    with expander:
        with st.form("Recommendations ", clear_on_submit=True):
            name_recommend = st.text_input("Name")
            role_recommend = st.text_input("Role")
            email_recommend = st.text_input("Email")
            phone_recommend = st.text_input("Phone Number")
            description_recommend = st.text_input("Description")

            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Recommendations.txt', "a+") as f:
                    f.write(f'Recommendation:  {name_recommend}--{role_recommend}--{email_recommend}--{phone_recommend}\n{description_recommend}')
                st.write("Submission successfull, submit another if you want!")


    # #Networks and memberships 
    # expander = st.expander("Networks and memberships ")    
    # with expander:
    #     with st.form("memberships ", clear_on_submit=True):
    #         title_membership = st.text_input("Enter title of your memberships")
    #         description_membership = st.text_input("Describ your memberships")
    #         from_membership = st.date_input("From")
    #         to_membership = st.date_input("To")
    #         Ongoing_membership = st.radio("On going", ["yes", "no"])
    #         # Every form must have a submit button.
    #         submitted = st.form_submit_button("حفظ")
    #         if submitted:
    #             with open(full_name+'_Networks.txt', "a+") as f:
    #                 f.write(f'{title_membership}\n{description_membership}\n{from_membership}--{to_membership}--{Ongoing_membership}')
    #             st.write("Submission successfull, submit another if you want!")

    #honours and awards
    expander = st.expander("honours and awards")    
    with expander:
        with st.form("honours and awards", clear_on_submit=True):
            title_award = st.text_input("Title")
            Awarding_institution = st.text_input("Awarding institution")
            award_date = st.date_input("Date of award")
            award_description = st.text_input("Description")

            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_awards.txt', "a+") as f:
                    f.write(f'{title_award}--{Awarding_institution}--{award_date}\n{award_description}\n')
                st.write("Submission successfull, submit another if you want!")

    #Cirtificates
    expander = st.expander("Cirtificates")    
    with expander:
        with st.form("Cirtificates ", clear_on_submit=True):
            title_Cirtificates = st.text_input("Enter title of your Cirtificate")
            description_Cirtificates = st.text_input("Describ your Cirtificates")
            year_Cirtificates = st.text_input("Date of issue")

            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Cirtificates.txt', "a+") as f:
                    f.write(f'Cirtificates:  {title_Cirtificates}--{year_Cirtificates}\n{description_Cirtificates}\n')
                st.write("Submission successfull, submit another if you want!")

    #langauge 
    expander = st.expander("اللغة")   
    with expander:
       
        with st.form("اللغة", clear_on_submit=True):
            Langauge = st.text_input("اللغة")
            Level = st.selectbox("المستوى", ['Beginner','Elementary', 'Intermediate','Advance', 'Native'])
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Langauge.txt', "a+") as f:
                    f.write(f'{Langauge},{Level}\n')
                st.write("Submission successfull, submit another if you want!")
    
    #self   
    expander = st.expander("تحدث عن نفسك") 
    with expander:
        
        aself = st.text_input("تحدث عن نفسك واهتماماتك")




    # templates
    expander = st.expander("النماذج")    
    with expander:
        template = st.selectbox("اختر النموذج", ['1','2', '3','4', '5', '6'])        
        col1, col2 = st.columns(2)
        col1.image('images/1.jpeg',caption=1, use_column_width=True)
        col2.image('images/2.jpeg',caption=2, use_column_width=True)
        col1.image('images/3.jpeg',caption=3, use_column_width=True)
        col2.image('images/4.jpeg',caption=4, use_column_width=True)
        col1.image('images/5.jpeg',caption="5 word format", use_column_width=True)
        col2.image('images/6.jpeg',caption="6 word format", use_column_width=True)

    #Others
    expander = st.expander("أخري")    
    with expander:
        #self
        other= st.text_input("ادخل أي إضافات أخرى ")


    if st.button("ارسل البيانات"):
        with open(f"{full_name}.txt", "w") as f:
            if expander.expanded:
                f.write("Full Name: " + full_name + "\n")
                f.write("Title: " + title + "\n")
                f.write("Email: " + email + "\n")
                f.write("Phone Number: " + phone + "\n")
                f.write("linkedin: " + linkedin + "\n")
                f.write("address: " + address + "\n")
            if expander.expanded:
                f.write("Skills: " + skills + "\n")            
            if expander.expanded:
                f.write(f"Packages:  {package} \n")
                f.write(f"template:  {template} \n")
            #submit education
            if expander.expanded:
                try:
                    f.write(f'{sp}Education section{sp}\n')
                    f.write(open(full_name+'_education.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')

                except FileNotFoundError:
                    f.write(f'{sp}\nNo Education\n{sp}\n\n')

            if expander.expanded:
                try:
                    f.write(f'{sp}Langauge section{sp}\n')
                    f.write(open(full_name+'_Langauge.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')
                except FileNotFoundError:
                    f.write(f'{sp}\nNo Langauge\n{sp}\n\n')

            if expander.expanded:
                try:
                    f.write(f'{sp}Experience section{sp}\n')
                    f.write(open(full_name+'_Experience.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')
                except FileNotFoundError:
                    f.write(f'{sp}\nNo Experience \n{sp}\n\n')


            if expander.expanded:
                try:
                    f.write(f'{sp}Project section{sp}\n')
                    f.write(open(full_name+'_Projects.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')
                except FileNotFoundError:
                    f.write(f'{sp}\nNo Project \n{sp}\n\n')

            if expander.expanded:
                try:
                    f.write(f'{sp}Volunteering section{sp}\n')
                    f.write(open(full_name+'_Volunteer.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')
                except FileNotFoundError:
                    f.write(f'{sp}\nNo Volunteering \n{sp}\n\n')

            if expander.expanded:
                try:
                    f.write(f'{sp}Publicaitons section{sp}\n')
                    f.write(open(full_name+'_Publicaitons.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')
                except FileNotFoundError:
                    f.write(f'{sp}\nNo Publicaitons \n{sp}\n\n')

            if expander.expanded:
                try:
                    f.write(f'{sp}Recommendations section{sp}\n')
                    f.write(open(full_name+'_Recommendations.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')
                except FileNotFoundError:
                    f.write(f'{sp}\nNo Recommendations \n{sp}\n\n')

            if expander.expanded:
                try:
                    f.write(f'{sp}Cirtificates section{sp}\n')
                    f.write(open(full_name+'_Cirtificates.txt').read())
                    f.write(f'{sp}{sp}{sp}\n')
                except FileNotFoundError:
                    f.write(f'{sp}\nNo Cirtificates \n{sp}\n\n')

            try:
                f.write(f'{sp}Other section{sp}\n')
                f.write(other)
                f.write(f'{sp}{sp}{sp}\n')
            except FileNotFoundError:
                f.write(f'{sp}\nNo section \n{sp}\n\n')            

            try:
                f.write(f'{sp}Self section{sp}\n')
                f.write(aself)
                f.write(f'{sp}{sp}{sp}\n')
            except FileNotFoundError:
                f.write(f'{sp}\nNo Self \n{sp}\n\n')

            
            if expander.expanded:
                if profile_picture:
                    file = f"{full_name}.{profile_picture.name.split('.')[-1]}"
                    with open(file,"wb") as p:
                        p.write(profile_picture.getbuffer())


 
        APIKEY = st.secrets["FILESTACK"]
        client = filestack.Client(APIKEY)

        store_params = {
            'location': 's3', 
            'path': 'folder/subfolder/',
            'upload_tags': {
                  "foo":"bar"
            }
        }
        
        # Upload files
        with st.spinner('Processing..'):
            # Upload the file to filestack
            filelink = client.upload(filepath=f'{full_name}.txt', store_params=store_params)
            try:
                filelink = client.upload(filepath=f'{file}', store_params=store_params)
            except:
                print('no picture')
        # total = 0
        st.success(f"Your total is **{total}** SDG")
        st.success("تم استلام الطلب ، تواصل معنا على الواتساب للتأكيد 0125836305")



if __name__=="__main__":
    create_cv()
    st.markdown(footer,unsafe_allow_html=True)
