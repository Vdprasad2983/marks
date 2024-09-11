import streamlit as st
import datetime
import mysql.connector as db

# Establishing MySQL connection
try:
    mydb = db.connect(
        host='sql.freedb.tech',
        user='freedb_prasad',
        password='3cPMCyn68$YCBXx',
        database="freedb_streamlitdb")
    mycursor = mydb.cursor()
    st.write("Connection established")
except db.Error as err:
    st.error(f"Error: {err}")
    st.stop()

# Define your college and department lists
college_list = ['Aditya university', 'Aditya engineering college (AEC)', 'Aditya college of engineering and technology (ACET)', 'Aditya college of engineering (ACOE)']
dep_list = ['CSE', 'ECE', 'EEE', 'MECH', 'CIVIL', 'AIML', 'IOT']

# Get input from user
yourname = st.text_input("Enter your name *")
father_name = st.text_input("Enter your father's name")
roll_number = st.text_input("Enter your roll number *", max_chars=10, placeholder="only in caps")
college = st.selectbox("Select your college", options=college_list)
department = st.selectbox("Select your Department", options=dep_list)
section = st.selectbox("Select your section", options=['A', 'B', 'C', 'D'])
cgpa = st.text_input("Enter your present SGPA", max_chars=4)
percentage = st.text_input("Enter your percentage", placeholder="prefer up to 2 decimals")
feedback = st.text_area("Feedback *", placeholder="Please provide your feedback about the website, it would be helpful")
submit_button = st.button("Submit")

# Get current time
current_time = datetime.datetime.now()

# Validate and handle form submission
if submit_button:
    if not yourname or not roll_number or not feedback:
        st.warning("Please enter the mandatory fields")
        st.stop()

    # Validate CGPA and Percentage
    try:
        cgpa_val = float(cgpa) if cgpa else None
        percentage_val = float(percentage) if percentage else None
    except ValueError:
        st.warning("Please enter valid numeric values for CGPA and Percentage")
        st.stop()

    # SQL query for inserting feedback
    sql = "INSERT INTO feedback (yourname, father_name, roll_number, college, department, section, cgpa, percentage, feedback) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (yourname, father_name, roll_number, college, department, section, cgpa_val, percentage_val, feedback)
    
    # Execute query and commit
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Your feedback was submitted successfully")
    except db.Error as err:
        st.error(f"Error: {err}")

    # Close the cursor and connection
    mycursor.close()
    mydb.close()
