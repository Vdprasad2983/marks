import streamlit as st
import datetime
import sqlite3
conn=sqlite3.connect('form.db',check_same_thread=False)
cur=conn.cursor()
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

date=datetime.datetime.now()
if submit_button:
        if not yourname or not roll_number or not feedback:
            st.warning("please enter the mandatory fields")
            st.stop()
        cur.execute(
            """
CREATE TABLE IF NOT EXISTS feedback(NAME TEXT(50),FATHER_NAME TEXT(50),ROLL_NUMBER TEXT(50),COLLEGE TEXT(50),DEPARTMENT TEXT(50),SECTION TEXT(50),CGPA TEXT(50),PERCENTAGE TEXT(50),FEEDBACK TEXT(150),DATE TEXT(50))
"""
        )
        cur.execute("INSERT INTO feedback VALUES (?,?,?,?,?,?,?,?,?,?)",(yourname,father_name,roll_number,college,department,section,cgpa,percentage,feedback,date))
        conn.commit()
        st.success("data added into the database successfully !!!")
view_data_button = st.button("View Feedback Data")

if view_data_button:
    # Fetch all data from the feedback table
    cur.execute("SELECT * FROM feedback")
    rows = cur.fetchall()

    if rows:
        st.write("Feedback Data:")
        for row in rows:
            st.write(f"Name: {row[0]}, Roll Number: {row[2]}, College: {row[3]}, Department: {row[4]}, Feedback: {row[8]}, Date: {row[9]}")
    else:
        st.write("No data found in the database.")

# Close the connection at the end of the script
conn.close()
