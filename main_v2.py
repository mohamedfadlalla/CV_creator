import streamlit as st
import filestack
import os

total = 0
sp = 7*'#'




def get_total(package):
    if len(package) == 1:
        return 800
    elif len(package) == 2:
        return 1500

def create_cv():
    st.set_page_config(page_title="CV Creator", page_icon=":guardsman:", layout="wide")
    st.image('images/banner.jpeg',use_column_width='auto')
    st.title("CV Creator")


    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    expander = st.expander("الخدمة")    
    with expander:
        package = st.multiselect("Package", ['CV in english', 'CV in Arabic'])
  
        if package:
            total = get_total(package)


    # Basic Information
    expander = st.expander("معلومات اساسية")
    with expander:
        full_name = st.text_input("الاسم بالكامل")
        email = st.text_input("الايميل")
        phone = st.text_input("رقم الهاتف المحمول")
        address = st.text_input("العنوان")

    # Skills
    expander = st.expander("المهارات")
    with expander:
        skills = st.text_area("ادخل ماهاراتك مفصولة بفاصل ")

    expander = st.expander("التعليم")    
    with expander:
        #Education
        with st.form("التعليم", clear_on_submit=True):
            degree = st.selectbox("Degree", ['Course','Primary school', 'bachelor degree','master degree', 'PhD'])
            field_of_study = st.text_input("مجال الدراسة")
            school_name = st.text_input("أسم الجامعة \ المدرسة")
            graduation_year = st.date_input("سنة التخريج")
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_education.txt', "a+") as f:
                    f.write(f'{degree},{field_of_study},{school_name},{graduation_year}\n')
                st.write("Submit successfully, submit another if you want!")
 
    expander = st.expander("الخبرة")    
    with expander:
        #Experience/Occupation
        with st.form("الخبرة", clear_on_submit=True):
            occupation = st.text_input("المسمي الوظيفي")
            company = st.text_input("الشركة / المواسسة")
            job_description = st.text_area("تكلم في ما لا يقل عن ثلاث نقاط عن مهام وظيفتك")
            start_date = st.date_input("تاريخ البداْ")
            work_here = st.checkbox("أعمل هنا")
            end_date = st.date_input("تاريخ الانتهاْ (دعه فارغا اذا كنت تعمل هتا)")
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Experience.txt', "a+") as f:
                    f.write(f'{occupation},{company},{job_description},{start_date},{work_here},{end_date}\n')
                st.write("Submit successfully, submit another if you want!")
    expander = st.expander("اللغة")    
    with expander:
        #langauge
        with st.form("اللغة", clear_on_submit=True):
            Langauge = st.text_input("اللغة")
            Level = st.selectbox("Degree", ['Beginner','Elementary', 'Intermediate','Advance', 'Native'])
            # Every form must have a submit button.
            submitted = st.form_submit_button("حفظ")
            if submitted:
                with open(full_name+'_Langauge.txt', "a+") as f:
                    f.write(f'{Langauge},{Level}\n')
                st.write("Submit successfully, submit another if you want!")
    
    expander = st.expander("عنك")    
    with expander:
        #self
        aself = st.text_input("تكلم عن نفسك واهتماماتك")
    


    # templates
    expander = st.expander("Linkedin")    
    with expander: 
        linkedin = st.text_input("ادخل رابط صفحتك علي اللينكدان")   



    # templates
    expander = st.expander("النماذج")    
    with expander:
        template = st.selectbox("اختر النموذج", ['1','2', '3','4', '5', '6'])        
        col1, col2 = st.columns(2)
        col1.image('images/1.jpeg',caption=1, use_column_width=True)
        col2.image('images/2.jpeg',caption=2, use_column_width=True)
        col1.image('images/3.jpeg',caption=3, use_column_width=True)
        col2.image('images/4.jpeg',caption=4, use_column_width=True)
        col1.image('images/5.jpeg',caption="5 word formate", use_column_width=True)
        col2.image('images/6.jpeg',caption="6 word formate", use_column_width=True)

    #Others
    expander = st.expander("أخري")    
    with expander:
        #self
        Other= st.text_input("ادخل اي اضافات اخري ")

    # Profile Picture
    expander = st.expander("ارفع صورتك الشخصية")
    with expander:
        profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
    


    if st.button("ارسل البيانات"):
        with open(f"{full_name}.txt", "w") as f:
            if expander.expanded:
                f.write("Full Name: " + full_name + "\n")
                f.write("Email: " + email + "\n")
                f.write("Phone Number: " + phone + "\n")
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
        total = 0
        st.success(f"Your total is **{total}** SDG")
        st.success("تم استلام الطلب ، اتصل بنا على الواتساب للتأكيد 0125836305")



if __name__=="__main__":
    create_cv()
    footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

.footer {
# position: bottom;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: grey;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/mohamed-fadlalla-ds/" target="_blank">M.Fadlalla </a></p>
</div>
"""

    # footer = "<footer><p>Mohamed</p></footer>"
    st.markdown(footer,unsafe_allow_html=True)
