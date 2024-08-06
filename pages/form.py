import gspread
import streamlit as st
import pandas as pd
import datetime
from oauth2client.service_account import ServiceAccountCredentials
scope=['https://www.googleapis.com/auth/spreadsheets',
       "https://www.googleapis.com/auth/drive"]
credentials=ServiceAccountCredentials.from_json_keyfile_name('entry-form-431402-3b3ffcc87e47.json',scope)
client=gspread.authorize(credentials)
#sheet=client.create("datasheet")
#sheet.share("veduruparthydurgaprasad@gmail.com",perm_type='user',role='writer')
sheet=client.open("datasheet").sheet1
existing_data=pd.DataFrame(sheet.get_all_records())
college_list=['Aditya university','aditya engineering college (AEC)','aditya college of engineering and technology (ACET)','aditya college of engineering (ACOE)']
dep_list=['CSE','ECE','EEE','MECH','CIVIL','AIML','IOT']
st.markdown("""
<style>
.css-erpbzb.edgvbvh3
{
    visibility: hidden;
}
.css-cio0dv.egzxvld1
{
    visibility: hidden;
}
</style>
""",unsafe_allow_html=True)
with st.form(key="new data",clear_on_submit=True):
    name=st.text_input("enter your name *")
    father=st.text_input("enter your father's name")
    roll=st.text_input("enter your roll number *",max_chars=10,placeholder="only in caps")
    college=st.selectbox("Select your college",options=college_list)
    department=st.selectbox("Select your Department",options=dep_list)
    section=st.selectbox("Select your section",options=['A','B','C','D'])
    cgpa=st.text_input("enter your present SGPA *",max_chars=4)
    percentage=st.text_input("enter your percentage *",placeholder="prefer upto 2 decimals")
    feedback=st.text_area("Feedback",placeholder="please provide your feedback about the website it would be helpful")
    submit_button=st.form_submit_button("Submit")

    current_time=datetime.datetime.now()

    if submit_button:
        if not name or not roll or not cgpa or not percentage:
            st.warning("please enter the mandatory fields")
            st.stop()
        #elif existing_data["roll number"].str.contains(roll).any():
            #st.warning("the person with same roll number is existed")
            #st.stop()
        else:
            add_data=pd.DataFrame(
                [
                   {
                       "name":name,
                       "father name": father,
                       "roll number": roll,
                       "college":college,
                       "department":department,
                       "section":section,
                       "cgpa":cgpa,
                       "percentage":percentage,
                       "feedback":feedback,
                       "date":str(current_time)[:10],
                       "time":str(current_time)[11:19]
                   } 
                ]
            )
            #update=pd.concat([existing_data,add_data],ignore_index=True)
            #sheet.add_cols(add_data)
            sheet.update([add_data.columns.values.tolist()] + existing_data.values.tolist() + add_data.values.tolist())
            st.success("data submitted successfully")