import streamlit as st
import filestack
import datetime
from my_styles import *
import os

total = 0
sp = 7*'#'

def get_total(package):
    if package == 'سيرة ذاتية باللغة الانجليزية':
        return 1500, "Enter your details in english"
    elif package == ' سيرة ذاتية باللغة العربية':
        return 1500, "ادخل بياناتك بالغة العربية"
    elif package =='سيرة ذاتية باللغتين':
        return 3000, None
        
def create_cv():
    st.set_page_config(page_title="CV Creator", page_icon=":guardsman:", layout="wide")
    st.image('images/banner.jpeg',use_column_width='auto')
    st.title("CV Creator")

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    #Packages
    expander = st.expander("الخدمة")    
    with expander:
        package = st.selectbox("Package", ['سيرة ذاتية باللغتين' ,'سيرة ذاتية باللغة الانجليزية' , ' سيرة ذاتية باللغة العربية'])
  
        if package:
            total, msg = get_total(package)
            st.write(f"Total = {total}")
            st.write(msg)

    # Basic Information
    expander = st.expander("معلومات أساسية")
    with expander:
        full_name = st.text_input("الاسم بالكامل")
        email = st.text_input("الايميل")
        phone = st.text_input("رقم الهاتف")
        address = st.text_input("العنوان")
        birth_day = st.date_input("أدخل تاريخ ميلادك", min_value=datetime.date(1900,1,1))
        title = st.text_input("المسمى الوظيفي")
        linkedin = st.text_input("ادخل رابط صفحتك على اللينكدان") 
        profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
        
    # Skills
    expander = st.expander("المهارات")
    with expander:
        skills = st.text_area("ادخل مهاراتك مفصولة بفاصل ")

    #Education
    expander = st.expander("التعليم")    
    with expander:
        with st.form("التعليم", clear_on_submit=True):
            degree = st.selectbox("الدرجة العلمية", ['Course','Secondary school', 'Diploma', 'bachelor degree','master degree', 'PhD'])
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
    expander = st.expander("الأوراق العلمية")    
    with expander:
        with st.form("أوراق علمية", clear_on_submit=True):
            title_publicaiton = st.text_input("عنوان الورقة العلمية")
            publisher = st.text_input("دار نشر")
            year = st.text_input("سنة النشر")
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Publicaitons.txt', "a+") as f:
                    f.write(f'{title_publicaiton}--{publisher}--{year}\n')
                st.write("Submission successfull, submit another if you want!")
    
    #Projects
    expander = st.expander("المشاريع")    
    with expander:
        with st.form("المشاريع", clear_on_submit=True):
            title_project = st.text_input("أدخل عنوان مشروعك")
            description_project = st.text_input("تحدث في ما لا يقل عن ثلاث نقاط عن مشروعك")
            date_project = st.date_input("تاريخ البداْ")
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Projects.txt', "a+") as f:
                    f.write(f'{title_project}--{date_project}\n{description_project}\n')
                st.write("Submission successfull, submit another if you want!")

    #Volunteering
    expander = st.expander("عمل تطوعي")    
    with expander:
        with st.form("عمل تطوعي", clear_on_submit=True):
            title_volunteer = st.text_input("المسمي الوظيفي")
            description_volunteer = st.text_input("تحدث في ما لا يقل عن ثلاث نقاط عن مهام وظيفتك")
            start_volunteer = st.date_input("أدخل تاريخ بدء التطوع")
            end_volunteer = st.date_input("أدخل تاريخ انتهاء التطوع")


            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Volunteer.txt', "a+") as f:
                    f.write(f'Volunteering:  {title_volunteer}--{start_volunteer}--{start_volunteer}\n{description_volunteer}\n')
                st.write("Submission successfull, submit another if you want!")

    #Recommendations 
    expander = st.expander("التوصيات")    
    with expander:
        with st.form("التوصيات", clear_on_submit=True):
            name_recommend = st.text_input("الأسم")
            role_recommend = st.text_input("المسمي الوظيفي")
            email_recommend = st.text_input("البريد الالكتروني")
            phone_recommend = st.text_input("رقم الهاتف")
            description_recommend = st.text_input("الوصف")

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
    expander = st.expander("الأوسمة والجوائز")    
    with expander:
        with st.form("honours and awards", clear_on_submit=True):
            title_award = st.text_input("اسم الجائزة")
            Awarding_institution = st.text_input("المؤسسة المانحة")
            award_date = st.date_input("تاريخ الجائزة")
            award_description = st.text_input("وصف")

            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_awards.txt', "a+") as f:
                    f.write(f'{title_award}--{Awarding_institution}--{award_date}\n{award_description}\n')
                st.write("Submission successfull, submit another if you want!")

    #Cirtificates
    expander = st.expander("الشهادات")    
    with expander:
        with st.form("الشهادات", clear_on_submit=True):
            title_Cirtificates = st.text_input("أدخل عنوان الشهادة الخاصة بك")
            description_Cirtificates = st.text_input("صِف شهاداتك")
            year_Cirtificates = st.text_input("تاريخ المنح")

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
                f.write("address: " + address + "\n\n")
            if expander.expanded:
                f.write("Skills: " + skills + "\n\n")            
            if expander.expanded:
                f.write(f"Packages:  {package} \n")
                f.write(f"template:  {template} \n\n")
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
                    f.write(f'\n{sp}{sp}{sp}\n')
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
                f.write(f"{aself}\n")
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
