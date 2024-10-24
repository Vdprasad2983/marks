import streamlit as sl
import pandas as pd
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
def calculate(l):
    count=0
    l1=[]
    for j in l:
        g=[grade_point(i[4])*float(i[5]) for i in data if i[0] ==j]
        c=[float(i[5]) for i in data if i[0]==j]
        if(sum(c)==21.5):
            count+=1
            string="pass"
        else:
            string="fail"
        grade=round((sum(g)/21.5),2)
        with open("data_1.csv","r") as f1:
            x1=csv.reader(f1)
            name_grade=list(x1)
            for k in range(len(name_grade)):
                if(j==name_grade[k][0]):
                    name=name_grade[k][1]
                    previous=name_grade[k][2]
                    change=((float(previous)*(float(present_sem)-1))+(float(grade)))/float(present_sem)
                    p=(float(change)-0.75)*10
                    percentage=round(p,2)
        l1.append([j,name,grade,percentage,previous,round(change,2),string])
    s_l1=sorted(l1,key=lambda x: x[2],reverse=True)

    passper=(count/len(s_l1))*100
    sl.subheader(f"The pass percentage of the respective section is {round(passper,2)}")
    sl.markdown("---")
    for i in range(len(s_l1)):
            if(roll==str(s_l1[i][0])):
                pre=s_l1[i][4]
                change=round(s_l1[i][5],2)
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
    t=pd.DataFrame({"Roll Number":[s_l1[i][0] for i in range(len(s_l1))],
                    "NAME":[s_l1[i][1] for i in range(len(s_l1))],
                    "SGPA":[s_l1[i][2] for i in range(len(s_l1))],
                    "Total CGPA":["%.2f"%s_l1[i][5] for i in range(len(s_l1))],
                    "Percentage":[s_l1[i][3] for i in range(len(s_l1))],
                    "status":[s_l1[i][6] for i in range(len(s_l1))]})
    t = t.set_index([pd.Index([i for i in range(1,len(s_l1)+1)])])
    return t

with open("ecemarks_1.csv","r") as f:
    x=csv.reader(f)
    data=list(x)
    l=['21P31A0401', '21P31A0402', '21P31A0403', '21P31A0404', '21P31A0405', '21P31A0406', '21P31A0407', '21P31A0408', 
       '21P31A0409', '21P31A0410', '21P31A0411', '21P31A0412', '21P31A0413', '21P31A0414', '21P31A0415', '21P31A0416', 
       '21P31A0417', '21P31A0418', '21P31A0419', '21P31A0420', '21P31A0421', '21P31A0422', '21P31A0423', '21P31A0424', 
       '21P31A0425', '21P31A0426', '21P31A0427', '21P31A0428', '21P31A0429', '21P31A0430', '21P31A0431', '21P31A0432', 
       '21P31A0433', '21P31A0434', '21P31A0435', '21P31A0436', '21P31A0437', '21P31A0438', '21P31A0439', '21P31A0440', 
       '21P31A0441', '21P31A0442', '21P31A0443', '21P31A0444', '21P31A0445', '21P31A0446', '21P31A0447', '21P31A0448', 
       '21P31A0449', '21P31A0450', '21P31A0451', '21P31A0452', '21P31A0453', '21P31A0454', '21P31A0455', '21P31A0456', 
       '21P31A0457', '21P31A0458', '21P31A0459', '21P31A0460', '21P31A0461', '21P31A0462', '21P31A0463', '21P31A0464', 
       '21P31A0465', '21P31A0466', '22P35A0401', '22P35A0402', '22P35A0403', '22P35A0404', '22P35A0405', '22P35A0406',
       '21P31A0467', '21P31A0468', '21P31A0469', '21P31A0470', '21P31A0471', '21P31A0472', '21P31A0473', '21P31A0474', 
       '21P31A0475', '21P31A0476', '21P31A0477', '21P31A0478', '21P31A0479', '21P31A0480', '21P31A0481', '21P31A0482', 
       '21P31A0483', '21P31A0484', '21P31A0485', '21P31A0486', '21P31A0487', '21P31A0488', '21P31A0489', '21P31A0490', 
       '21P31A0491', '21P31A0492', '21P31A0493', '21P31A0494', '21P31A0495', '21P31A0496', '21P31A0497', '21P31A0498', 
       '21P31A0499', '21P31A04A0', '21P31A04A1', '21P31A04A2', '21P31A04A3', '21P31A04A4', '21P31A04A5', '21P31A04A6', 
       '21P31A04A7', '21P31A04A8', '21P31A04A9', '21P31A04B0', '21P31A04B1', '21P31A04B2', '21P31A04B3', '21P31A04B4', 
       '21P31A04B5', '21P31A04B6', '21P31A04B7', '21P31A04B8', '21P31A04B9', '21P31A04C0', '21P31A04C1', '21P31A04C2', 
       '21P31A04C3', '21P31A04C4', '21P31A04C5', '21P31A04C6', '21P31A04C7', '21P31A04C8', '21P31A04C9', '21P31A04D0', 
       '21P31A04D1', '21P31A04D2', '22P35A0407', '22P35A0408', '22P35A0409', '22P35A0410', '22P35A0411', '22P35A0412', 
       '21P31A04D3', '21P31A04D4', '21P31A04D5', '21P31A04D6', '21P31A04D7', '21P31A04D8', '21P31A04D9', '21P31A04E0', 
       '21P31A04E1', '21P31A04E2', '21P31A04E3', '21P31A04E4', '21P31A04E5', '21P31A04E6', '21P31A04E7', '21P31A04E8', 
       '21P31A04E9', '21P31A04F0', '21P31A04F1', '21P31A04F2', '21P31A04F3', '21P31A04F4', '21P31A04F5', '21P31A04F6', 
       '21P31A04F7', '21P31A04F8', '21P31A04F9', '21P31A04G0', '21P31A04G1', '21P31A04G2', '21P31A04G3', '21P31A04G4', 
       '21P31A04G5', '21P31A04G6', '21P31A04G7', '21P31A04G8', '21P31A04G9', '21P31A04H0', '21P31A04H1', '21P31A04H2', 
       '21P31A04H3', '21P31A04H4', '21P31A04H5', '21P31A04H6', '21P31A04H7', '21P31A04H8', '21P31A04H9', '21P31A04I0', 
       '21P31A04I1', '21P31A04I2', '21P31A04I3', '21P31A04I4', '21P31A04I5', '21P31A04I6', '21P31A04I7', '21P31A04I8', 
       '21P31A04I9', '21P31A04J0', '21P31A04J1', '21P31A04J2', '21P31A04J3', '21P31A04J4', '21P31A04J5', '21P31A04J6', 
       '21P31A04J7', '21P31A04J8', '22P35A0413', '22P35A0414', '22P35A0415', '22P35A0416', '22P35A0417', '22P35A0418',
       '21P31A04J9', '21P31A04K0', '21P31A04K1', '21P31A04K2', '21P31A04K3', '21P31A04K4', '21P31A04K5', '21P31A04K6', 
       '21P31A04K7', '21P31A04K8', '21P31A04K9', '21P31A04L0', '21P31A04L1', '21P31A04L2', '21P31A04L3', '21P31A04L4', 
       '21P31A04L5', '21P31A04L6', '21P31A04L7', '21P31A04L8', '21P31A04L9', '21P31A04M0', '21P31A04M1', '21P31A04M2', 
       '21P31A04M3', '21P31A04M4', '21P31A04M5', '21P31A04M6', '21P31A04M7', '21P31A04M8', '21P31A04M9', '21P31A04N0', 
       '21P31A04N1', '21P31A04N2', '21P31A04N3', '21P31A04N4', '21P31A04N5', '21P31A04N6', '21P31A04N7', '21P31A04N8', 
       '21P31A04N9', '21P31A04O0', '21P31A04O1', '21P31A04O2', '21P31A04O3', '21P31A04O4', '21P31A04O5', '21P31A04O6', 
       '21P31A04O7', '21P31A04O8', '21P31A04O9', '21P31A04P0', '21P31A04P1', '21P31A04P2', '21P31A04P3', '21P31A04P4', 
       '21P31A04P5', '21P31A04P6', '21P31A04P7', '21P31A04P8', '21P31A04P9', '21P31A04Q0', '21P31A04Q1', '21P31A04Q2', 
       '21P31A04Q3', '21P31A04Q4', '22P35A0419', '22P35A0420', '22P35A0421', '22P35A0422', '22P35A0423', '22P35A0424']
    
    a=l[:72]
    b=l[72:144]
    c=l[144:216]
    d=l[216:288]
    sl.set_page_config(page_title="ACET",page_icon="acetlogo.jpeg")
    sl.image("university.png",width=500)
    sl.title("Marks of ACET ECE in the III-II sem")
    select=option_menu(menu_title=None,options=["All sections","A sec","B sec","C sec","D sec","Custom"],
                        default_index=0,orientation="horizontal")
    sl.subheader("you can explore other options by clicking on menu bar")
    sl.subheader("For better experience turn on desktop mode")
    col1,col2,col3=sl.columns(3)
    r=col1.text_input("enter your roll number",max_chars=10)
    roll=r.upper()
    #pre=col2.text_input("enter you total cgpa upto this result",value=0.0,max_chars=5)
    #present_sem=col3.selectbox("enter you present number of sem",options=('1','2','3','4','5','6','7','8'))
    present_sem='6'
    if(roll==""):
        sl.error("please! enter the roll number")
    #select=sl.selectbox("choose your option for sections",options=("All sections","A sec","B sec","C sec","D sec"))
    def color_df(val):
        if val=='pass':
            color='green'
        else:
            color='red'
        return f'background-color:{color}'
    if select=="A sec":
        t=calculate(a)
        sl.table(t.style.applymap(color_df,subset=['status']))
    if select=="B sec":
        t=calculate(b)
        sl.table(t.style.applymap(color_df,subset=['status']))
    if select=="C sec":
        t=calculate(c)
        sl.table(t.style.applymap(color_df,subset=['status']))
    if select=="D sec":
        t=calculate(d)
        sl.table(t.style.applymap(color_df,subset=['status']))
    if select=="All sections":
        t=calculate(l)
        sl.dataframe(t.style.applymap(color_df,subset=['status']))
    if select=="Custom":
        cus=list(sl.multiselect("select the numbers you want",options=l))
        try:
            t=calculate(cus)
            sl.table(t)
        except ZeroDivisionError:
            sl.warning("please choose atleast one number")
    '''mapdata=pd.DataFrame({
        'latitude':[17.0888774],
        'longitude':[82.0680957]
    })
    sl.map(mapdata)'''
