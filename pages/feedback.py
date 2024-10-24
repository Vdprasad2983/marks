import streamlit as st
import datetime
import psycopg2
import os
from pytz import timezone

# PostgreSQL connection parameters (replace with your Render PostgreSQL details)
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port=DB_PORT
)
cur = conn.cursor()

# College and department lists
college_list = ['Aditya university', 'aditya engineering college (AEC)', 
                'aditya college of engineering and technology (ACET)', 
                'aditya college of engineering (ACOE)']
dep_list = ['CSE', 'ECE', 'EEE', 'MECH', 'CIVIL', 'AIML', 'IOT']

# Streamlit input fields
yourname = st.text_input("Enter your name *",max_chars=100)
father_name = st.text_input("Enter your father's name",max_chars=100)
roll_number = st.text_input("Enter your roll number *", max_chars=10, placeholder="Only in caps")
college = st.selectbox("Select your college", options=college_list)
department = st.selectbox("Select your Department", options=dep_list)
section = st.selectbox("Select your section", options=['A', 'B', 'C', 'D'])
cgpa = st.text_input("Enter your present SGPA", max_chars=4)
percentage = st.text_input("Enter your percentage", placeholder="Prefer up to 2 decimals")
feedback = st.text_area("Feedback *", placeholder="Please provide your feedback about the website")

submit_button = st.button("Submit")

# Current date
kolkata=timezone("Asia/Kolkata")
date = datetime.datetime.now(tz=kolkata)

if submit_button:
    if not yourname or not roll_number or not feedback:
        st.warning("Please enter the mandatory fields")
        st.stop()

    # Create table if it does not exist
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback(
            NAME VARCHAR(100), FATHER_NAME VARCHAR(100), ROLL_NUMBER VARCHAR(50),
            COLLEGE VARCHAR(150), DEPARTMENT VARCHAR(50), SECTION VARCHAR(50), 
            CGPA VARCHAR(50), PERCENTAGE VARCHAR(50), FEEDBACK TEXT, DATE TIMESTAMPTZ
        )
        """
    )

    # Insert data into the table
    cur.execute("INSERT INTO feedback (NAME, FATHER_NAME, ROLL_NUMBER, COLLEGE, DEPARTMENT, SECTION, CGPA, PERCENTAGE, FEEDBACK, DATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (yourname, father_name, roll_number, college, department, section, cgpa, percentage, feedback, date))
    conn.commit()
    st.success("Data added into the database successfully !!!")
    conn.close()
