import streamlit as sl
import pandas as pd
import datetime
import math
import csv
from streamlit_option_menu import option_menu
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


with open("ecemarks_2.csv","r") as f:
    x=csv.reader(f)
    data=list(x)
    l=['21MH1A0401', '21MH1A0402', '21MH1A0404', '21MH1A0405', '21MH1A0406', '21MH1A0407', '21MH1A0408', 
       '21MH1A0409', '21MH1A0410', '21MH1A0411', '21MH1A0412', '21MH1A0413', '21MH1A0414', '21MH1A0415', 
       '21MH1A0416', '21MH1A0417', '21MH1A0418', '21MH1A0420', '21MH1A0421', '21MH1A0422', '21MH1A0423', 
       '21MH1A0424', '21MH1A0425', '21MH1A0426', '21MH1A0427', '21MH1A0428', '21MH1A0429', '21MH1A0430', 
       '21MH1A0431', '21MH1A0432', '21MH1A0433', '21MH1A0434', '21MH1A0435', '21MH1A0436', '21MH1A0437', 
       '21MH1A0438', '21MH1A0439', '21MH1A0440', '21MH1A0441', '21MH1A0442', '21MH1A0443', '21MH1A0445', 
       '21MH1A0446', '21MH1A0447', '21MH1A0448', '21MH1A0449', '21MH1A0450', '21MH1A0451', '21MH1A0452', 
       '21MH1A0453', '21MH1A0454', '21MH1A0455', '21MH1A0456', '21MH1A0457', '21MH1A0458', '21MH1A0459', 
       '21MH1A0460', '21MH1A0461', '21mh1a0462', '21MH1A0463', '21MH1A0465', '21MH1A0466', '21MH1A0467', 
       '21MH1A0468', '21MH1A0469', '21MH1A0470', '21MH1A0471', '21MH1A0472', '21MH1A0473', '21MH1A0474', 
       '21MH1A0477', '21MH1A0478', '21MH1A0479', '21MH1A0480', '21MH1A0481', '21MH1A0482', '21MH1A0483', 
       '21MH1A0484', '21MH1A0485', '21MH1A0486', '21MH1A0487', '21MH1A0488', '21MH1A0489', '21MH1A0490', 
       '21MH1A0491', '21MH1A0492', '21MH1A0493', '21MH1A0494', '21MH1A0495', '21MH1A0496', '21MH1A0497', 
       '21MH1A0498', '21MH1A0499', '21MH1A04A0', '21MH1A04A1', '21MH1A04A2', '21MH1A04A3', '21MH1A04A4', 
       '21MH1A04A5', '21MH1A04A6', '21mh1a04a7', '21MH1A04A8', '21MH1A04A9', '21MH1A04B0', '21MH1A04B1', 
       '21MH1A04B2', '21MH1A04B3', '21MH1A04B4', '21MH1A04B6', '21MH1A04B7', '21MH1A04B8', '21MH1A04B9', 
       '21MH1A04C0', '21MH1A04C1', '21MH1A04C2', '21MH1A04C3', '21MH1A04C4', '21MH1A04C5', '21MH1A04C7', 
       '21MH1A04C8', '21MH1A04D0', '21MH1A04D1', '21MH1A04D3', '21MH1A04D4', '21MH1A04D5', '21MH1A04D6', 
       '21MH1A04D7', '21MH1A04D8', '21MH1A04D9', '21MH1A04E0', '21MH1A04E1', '21MH1A04E2', '21MH1A04E4', 
       '21MH1A04E5', '21MH1A04E6', '21MH1A04E7', '21MH1A04E8', '21MH1A04F0', '21MH1A04F1', '21MH1A04F2', 
       '21MH1A04F3', '21MH1A04F4', '21MH1A04F5', '21MH1A04F6', '21MH1A04F7', '21MH1A04F8', '21MH1A04F9', 
       '21MH1A04G0', '21MH1A04G1', '21MH1A04G2', '21MH1A04G3', '21MH1A04G5', '21MH1A04G6', '21MH1A04G7', 
       '21MH1A04G8', '21MH1A04G9', '21MH1A04H0', '21MH1A04H1', '21MH1A04H2', '21MH1A04H3', '21MH1A04H4', 
       '21MH1A04H5', '21MH1A04H6', '21MH1A04H7', '21MH1A04H8', '21MH1A04H9', '21MH1A04I0', '21MH1A04I1', 
       '21MH1A04I2', '21MH1A04I4', '21MH1A04I5', '21MH1A04I6', '21MH1A04I7', '21MH1A04I8', '21MH1A04I9', 
       '21MH1A04J0', '21MH1A04J1', '21MH1A04J2', '21MH1A04J3', '21MH1A04J4', '21MH1A04J5', '21MH1A04J6', 
       '21MH1A04J7', '21MH1A04J8', '21MH1A04J9', '21MH1A04K0', '21MH1A04K1', '21MH1A04K2', '21MH1A04K3', 
       '21MH1A04K4', '21MH1A04K5', '21MH1A04K6', '21MH1A04K7', '21MH1A04K8', '21MH1A04K9', '21MH1A04L0', 
       '21MH1A04L1', '21MH1A04L2', '21MH1A04L3', '21MH1A04L4', '21MH1A04L5', '21MH1A04L6', '21MH1A04L8', 
       '21MH1A04L9', '21MH1A04M1', '21MH1A04M2', '21MH1A04M3', '21MH1A04M4', '21MH1A04M5', '21MH1A04M6', 
       '21MH1A04M7', '21MH1A04M8', '21MH1A04M9', '21MH1A04N0', '21MH1A04N1', '21MH1A04N2', '21MH1A04N3', 
       '21MH1A04N4', '21MH1A04N5', '21MH1A04N6', '21MH1A04N7', '21MH1A04N8', '21MH1A04N9', '21MH1A04O0', 
       '21MH1A04O1', '21MH1A04O2', '21MH1A04O3', '21MH1A04O4', '21MH1A04O5', '21MH1A04O6', '21MH1A04O7', 
       '21MH1A04O8', '21MH1A04O9', '21MH1A04P0', '21MH1A04P1', '21MH1A04P2', '21MH1A04P3', '21MH1A04P4', 
       '21MH1A04P5', '21MH1A04P7', '21MH1A04P8', '21MH1A04P9', '21MH1A04Q0', '21MH1A04Q1', '21MH1A04Q2', 
       '21MH1A04Q3', '21MH5A0450', '223C5A0401', '22MH5A0401', '22MH5A0402', '22MH5A0403', '22MH5A0404', 
       '22MH5A0405', '22MH5A0406', '22MH5A0407', '22MH5A0408', '22MH5A0409', '22MH5A0410', '22MH5A0411', 
       '22MH5A0412', '22MH5A0413', '22MH5A0414', '22MH5A0415', '22MH5A0416', '22MH5A0417', '22MH5A0418', 
       '22MH5A0419', '22MH5A0420', '22MH5A0421', '22MH5A0422', '22MH5A0423', '22MH5A0424', '22MH5A0425']
    
    #a=l[:72]
    #b=l[72:144]
    #c=l[144:216]
    #d=l[216:288]
    sl.title("Marks of ACOE ECE in the III-II sem")
    selected=option_menu(menu_title=None,options=["profile","console data"],
                         icons=["cast","book"],default_index=0,orientation="horizontal")
    col1,col2,col3=sl.columns(3)
    r=col1.text_input("enter your roll number*",max_chars=10)
    roll=r.upper()
    pre=col2.text_input("enter you total cgpa upto this result",value=0.0,max_chars=5)
    present_sem=col3.selectbox("enter you present number of sem",options=('1','2','3','4','5','6','7','8'))
    
    #present_sem='5'
    if(roll==""):
        sl.error("please! enter the roll number")
    if roll not in l and roll !="":
        sl.warning("the number you have entered is not in the list please check again!")
    
    l1=[]
    count=0
    for j in l:
        g=[grade_point(i[4])*float(i[5]) for i in data if i[0] ==j]
        c=[float(i[5]) for i in data if i[0]==j]
        if(sum(c)==21.5):
            count+=1
            string="pass"
        else:
            string="fail"
        grade=("%.2f"%(sum(g)/21.5))
        p=(float(grade)-0.75)*10
        percentage=("%.2f"%p)
        with open("data_2.csv","r") as f1:
            x1=csv.reader(f1)
            extra=list(x1)
            for k in range(len(extra)):
                if(j==extra[k][1]):
                    name=extra[k][2]
                    father=extra[k][4]
                    dob=extra[k][7]
                    abc=extra[k][6]
                    
        l1.append([j,name,grade,percentage,father,abc,string,dob])
    s_l1=sorted(l1,key=lambda x: x[2],reverse=True)
    if selected=="console data":
        for i in range(len(s_l1)):
            if(roll==str(s_l1[i][0])):
            
                change=((float(pre)*(float(present_sem)-1))+(float(s_l1[i][2])))/float(present_sem)
                    #with open("data.csv","a+",newline="")as f1:
                        #x1=csv.writer(f1)
                        #current_time = datetime.datetime.now()
                        #[roll no,previous cgpa,present cgpa,precentage]
                        #x1.writerow([roll,present_sem,pre,s_l1[i][1],s_l1[i][2],"%.2f"%change,str(current_time)[:10],str(current_time)[11:19]])
                if(s_l1[i][6]=="pass"):
                    sl.write(f"Congratulations {s_l1[i][1]} you have passed in all of your exams")
                    sl.write(f"YOU HAVE SECURED {s_l1.index(s_l1[i])+1}th position")
                    sl.success(f"{s_l1[i][0]} --> CGPA={s_l1[i][2]}, percentage={s_l1[i][3]}")
                else:
                    sl.write(f"sorry {s_l1[i][1]} you have failed, luck doesn't favour you this time")
                    sl.write(f"YOU HAVE SECURED {s_l1.index(s_l1[i])+1}th position in the department")
                    #sl.write("Humein successful selections ke sath successful preprations ko bi celebrate karna chahiye!       ~jeethu bhaiya")
                    sl.error(f"{s_l1[i][0]} --> CGPA={s_l1[i][2]}, percentage={s_l1[i][3]}")
                #change=((float(s_l1[i][4])*(float(present_sem)-1))+(float(s_l1[i][2])))/float(present_sem)
                sl.metric(label="Your total CGPA",value="%.2f"%change,delta="%.2f"%(float(s_l1[i][2])-change))
        t=pd.DataFrame({"Roll Number":[s_l1[i][0] for i in range(len(s_l1))],"NAME":[s_l1[i][1] for i in range(len(s_l1))],
                        "SGPA":[s_l1[i][2] for i in range(len(s_l1))],"Percentage":[s_l1[i][3] for i in range(len(s_l1))],
                        "status":[s_l1[i][6] for i in range(len(s_l1))]})
        t = t.set_index([pd.Index([i for i in range(1,len(s_l1)+1)])])
        sl.table(t)
    if(selected=="profile"):
        #l1.append([roll,name,grade,percentage,father,abc,string,dob])
        for i in s_l1:
            if i[0]==roll:
                sl.write(f"Roll number :\t {i[0]}")
                sl.write(f"name :\t {i[1]}")
                sl.write(f"father name :\t {i[4]}")
                sl.write(f"Date of Birth : {i[7]}")
                sl.write(f"ABC id : {i[5]}")
                sl.write(f"grade obtianed in 6th sem :\t {i[2]}")
                sl.write(f"percentage obtianed in 6th sem :\t {i[3]}")
                if(i[6]=="pass"):
                    sl.success("passed in all subjects and not having any backlogs")
                else:
                    sl.error("failed in one or more subject(s)")
                
