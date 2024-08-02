import streamlit as sl
import csv
import pandas as pd
def grade_point(n):
    if n=="A+":
        return 10
    elif n=="A":
        return 9
    elif n=="B":
        return 8
    elif n=="C":
        return 7
    elif n=="D":
        return 6
    elif n=="E":
        return 5
    else:
        return 0
def credit_point(n):
    if n=="-- select grade --":
        return float(0)
    else:
        return float(n)
name=sl.text_input("enter Your name")
prev=sl.text_input("enter your previous grade(round off upto 2 decimals)")
sl.markdown("<h1> SGPA CALCULATOR</h1>",unsafe_allow_html=True)
with sl.form("sgpa calculator"):
    col1,col2,col3=sl.columns(3)
    col4,col5,col6=sl.columns(3)
    col7,col8,col9=sl.columns(3)
    col11,col12,col13=sl.columns(3)
    col14,col15,col16=sl.columns(3)
    col17,col18,col19=sl.columns(3)
    col20,col21,col22=sl.columns(3)
    col23,col24,col25=sl.columns(3)
    col26,col27,col28=sl.columns(3)
    col29,col30,col31=sl.columns(3)
    col1.text_input("subject1 name")
    g1=col2.selectbox("Enter sub1 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c1=col3.selectbox("Enter sub1 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col4.text_input("subject2 name")
    g2=col5.selectbox("Enter sub2 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c2=col6.selectbox("Enter sub2 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col7.text_input("subject3 name")
    g3=col8.selectbox("Enter sub3 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c3=col9.selectbox("Enter sub3 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col11.text_input("subject4 name")
    g4=col12.selectbox("Enter sub4 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c4=col13.selectbox("Enter sub4 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col14.text_input("subject5 name")
    g5=col15.selectbox("Enter sub5 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c5=col16.selectbox("Enter sub5 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col17.text_input("subject6 name")
    g6=col18.selectbox("Enter sub6 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c6=col19.selectbox("Enter sub6 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col20.text_input("subject7 name")
    g7=col21.selectbox("Enter sub7 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c7=col22.selectbox("Enter sub7 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col23.text_input("subject8 name")
    g8=col24.selectbox("Enter sub8 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c8=col25.selectbox("Enter sub8 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col26.text_input("subject9 name")
    g9=col27.selectbox("Enter sub9 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c9=col28.selectbox("Enter sub9 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    col29.text_input("subject10 name")
    g10=col30.selectbox("Enter sub10 grade",options=("-- select grade --","A+","A","B","C","D","E","F","COMPLETED"))
    c10=col31.selectbox("Enter sub10 credit",options=("-- select grade --","3.0","2.0","1.5","4.0","8.0","0.0"))
    def calculate():
        grades=[grade_point(g1),grade_point(g2),grade_point(g3),grade_point(g4),grade_point(g5),
                grade_point(g6),grade_point(g7),grade_point(g8),grade_point(g9),grade_point(g10)]
        credit=[credit_point(c1),credit_point(c2),credit_point(c3),credit_point(c4),credit_point(c5),
                credit_point(c6),credit_point(c7),credit_point(c8),credit_point(c9),credit_point(c10)]
        grade=[(grades[i]*credit[i]) for i in range(len(grades))]
        final_grade=(sum(grade)/21.5)
        sl.text(final_grade)
        sl.metric(label="change in cgpa",value=final_grade,delta=(final_grade-float(prev)))
    sl.write("please check the result on top of the page after clicking on submit button")
    sl.write("Incase of result not shown please click on the submit button again")
    sl.form_submit_button("Submit",on_click=calculate)