import streamlit as st
import datetime
import mysql.connector as db
mydb=db.connect(
    host='sql.freedb.tech',
    user='freedb_prasad'
    password='3cPMCyn68$YCBXx',
    database="freedb_streamlitdb",
    port="3306")
mycursor=mydb.cursor()
print("connectoin established")

college_list=['Aditya university','aditya engineering college (AEC)','aditya college of engineering and technology (ACET)','aditya college of engineering (ACOE)']
dep_list=['CSE','ECE','EEE','MECH','CIVIL','AIML','IOT']

yourname=st.text_input("enter your name *")
father_name=st.text_input("enter your father's name")
roll_number=st.text_input("enter your roll number *",max_chars=10,placeholder="only in caps")
college=st.selectbox("Select your college",options=college_list)
department=st.selectbox("Select your Department",options=dep_list)
section=st.selectbox("Select your section",options=['A','B','C','D'])
cgpa=st.text_input("enter your present SGPA",max_chars=4)
percentage=st.text_input("enter your percentage",placeholder="prefer upto 2 decimals")
feedback=st.text_area("Feedback *",placeholder="please provide your feedback about the website it would be helpful")
submit_button=st.button("Submit")

current_time=datetime.datetime.now()

if submit_button:
        if not yourname or not roll_number or not feedback:
            st.warning("please enter the mandatory fields")
            st.stop()
        sql="insert into feedback(yourname , father_name , roll_number, college , department, section ,cgpa,percentage,feedback) values(%s ,%s, %s, %s ,%s, %s, %s, %s, %s)"
        val=(yourname , father_name , roll_number, college , department , section , cgpa , percentage , feedback)
        mycursor.execute(sql,val)
        mydb.commit()
        st.success("your query submitted succesfully")
