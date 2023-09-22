import pandas as pd
import datetime
import time as t
#import sys
import pyautogui as py
py.FAILSAFE=False



today=datetime.date.today();



login=pd.read_csv('prescription.csv')
l2=pd.read_csv('Patients_main.csv')
acsv=pd.read_csv("admin.csv")
app=pd.read_csv("Appointment.csv")
app_list=pd.read_csv("timings.csv")
app_list2=pd.read_csv("timings.csv",header=None)





'''
def slow_print(s, delay=0.1):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        t.sleep(delay)
    print('')
'''


log1=''
log2=''


#Defining a Function called system_doctor
#We have defined this Function so it is easier
#for us to find the error in the code
#We will use this Function later in the code
def system_doctor():
     global app
     global log2
     global log1
     while True:
          print('''             ***************************************
                    Clinic Management System
             ***************************************
             *************M̳A̳I̳N̳ M̳E̳N̳U̳*****************
               1. Old Records
               2. New Patient(New Record)
               3. Old Patients(New Visit)
               4. Exit System
             ***************************************''')
          #Giving the user a number of options to choose from
          choice=input("Enter the function's number-->")
          print(l2)
          if choice=='1':
               print('\t-------------------Login-------------------')
               log1=input('Enter your First Name-->')
               log2=input('Enter your Last Name-->')
               #df = login.loc[login.Password == passkey.lower()]
               df=l2.loc[(l2.Name==log1)&(l2.Lname==log2)]
               if df.empty:
                    print("Failed")
               else:
                    customer_records()
          elif choice=='2':
               new_patient()
          elif choice=='3':
               print("y")
          elif choice=='4':
               exit_sys()
          elif choice!=1 or choice!=2 or choice!=3:
               print("Incorrect Input")
               print("Try Again.")
          else:
               print("Incorrect Input")
               print("Try Again.")
     return log2




def new_patient():
    print('-------------------New Patient-------------------')
    print("Enter your First Name")
    userfname=input(">>>")
    userlname=input('Enter your Last Name-->')
    gender1=input("Enter your Gender(M/F)-->")
    userdob=input("Enter your Date of Birth(DD/MM/YYYY)-->")
    userall=input("Enter Your Allergies(Seperated with commas)-->")
    doctype=input("Enter The Doctor's type-->")
    medname=input("Enter Medicine Name-->")
    userfname2=userfname.lower()
    userlname2=userlname.lower()
    gender=gender1.upper()
    userall2=userall.upper()
    t.sleep(3)
    pid=len(l2.index)+1
    medtime=input("Medicine Is Given Till Which Date(DD/MM/YYYY)-->")
    medtime1=datetime.datetime.strptime(medtime,"%d/%m/%Y").date()
    med=medtime1-today;
    docname=login.loc[(login.Doctor_type==doc)]['Doctor_Name']
    ls1 = [pid,userfname2,userlname2,gender,userdob,userall2]
    print(ls1)
    l2.loc[len(l2.index)] = ls1
    l2.to_csv('Patients_main.csv',index=False)
    ls2=[pid,today,today,med,medname,doctype,docname]
    login.loc[len(login.index)]=ls2
    login.to_csv('Prescription.csv',index=False)
    print("Congratulations")
    print("New Account Created")



bk=''
def book_app():
     global bk
     while True:
          print(app_list)
          choice=input('enter the doctor name\n>>>')
          if choice not in app_list:
               print('doctor not found')
          else:
               #bk=app_list[app_list==choice]
               #bk=app_list.loc[:,choice]
               bk=app_list.loc[:,choice]
               print(bk)
               book_app_time()

def book_app_time():
     choice1=input('enter the desired timing\n>>>')
     if choice1 not in bk:
          cs=input('enter the confirmation\n1.YES\n2.NO\n>>>')
          print('Desired Timing Not Available')
          bk_app_continue=input("Do You Wish To Choose Another Timing?\n1).Yes\n2).No\n>>>")
          if bk_app_continue.lower()=='yes':
               print("")
               book_app_time()
          else:
               ask_exit()
     else:
          cs=input('enter the confirmation\n1.YES\n2.NO\n>>>')
          if cs.upper()=='YES':
               print('your booking has been confirmed')
          else:
               print('thanks for visiting')


def ask_exit():
     ask_continue=input("Do You Wish To Perform Any Other Function/Task(Yes/No)?")
     if ask_continue.lower()=='yes':
          ask_start_from_where=input("Do You Wish To Continue Performing The Function/Task In The Records Of the Current Patient Named:-",log1)
          if ask_start_from_where.lower()=='yes':
               customer_records()
          else:
               exit_sys()
     else:
          exit_sys()

def customer_records():
     global app
     print('Welcome Mr.', log2)
     print("""             ***************************************
     Clinic Management System
     ***************************************
     *************C̳U̳S̳T̳O̳M̳E̳R̳ R̳E̳C̳O̳R̳D̳S̳*****************
     1. Previous Records
     2. Old Medicines Given
     3. Appointment
     4. Exit System
     ***************************************""")
     choice2=int(input("Enter you choice-->"))
     if choice2==1:
          pid2=int(input("Enter Patient ID-->"))
          df2=l2.loc[(l2.Patient_ID==pid2)] 
          if df2.empty:
               print("Incorrect Patient ID Entered-->")
          else:
               print('Patients Old Records:-')
               print(df2)
     elif choice2==2:
          pid2=int(input("Enter Patient ID-->"))
          df2=login.loc[(pid2==login.Patient_ID)]
          if df2.empty:
               print("Incorrect Patient ID Entered")
          else:
               print("Medicines Given")
               print(df2)
     elif choice2==3:
          pid2=int(input("Enter Patient ID-->"))
          df2=l2.loc[(pid2==l2.Patient_ID)]
          if df2.empty:
               print("Incorrect Patient ID Entered")
          else:
               print('''             ***************************************
     Clinic Management System
     ***************************************
     *************Appointments****************
     1. Book An Appointment
     2. Upcoming Appointment
     3. Cancel An Appointment
     4. Exit System
     ***************************************
     Enter The Number Of Function You Wish To Use''')
               choice3=int(input(">>>"))
               if choice3==1:
                    book_app()
               elif choice3==2:
                    print("Your Upcoming Appointments are as Follows:-")
                    df3=app.loc[(pid2==app.PatientId)&(l2.Name==log1)&(l2.Lname==log2)]
                    print(df3)
               elif choice3==3:
                    df3=app.loc[(pid2==app.PatientId)]
                    print(df3)
                    i=app.loc[(pid2==app.PatientId)].index
                    app=app.drop(index=i)
                    app.to_csv('Appointment.csv')
                    print("Appointment Cancelled")
               elif choice3==4:
                    exit_sys()
               else:
                    print("Enter a Valid Input")
     elif choice2==4:
          exit_sys()
     else:
          print("Enter a Valid Choice")


def exit_sys():
     print('Clinic Management System Ended')
     t.sleep(2)
     position=py.position()
     py.moveTo(1000000000, 0, duration=2)
     py.click()
     py.moveTo(position)
     py.press('enter')





#print(py.size())
print('''             ***************************************
                    Clinic Management System
             ***************************************
             *************Employee Login System*****************''')
aname=input("Enter your Name-->")
apass=input("Enter your Password-->")
print('''***************************************''')
adminn='Manish'
adminp='nms'
#aif=acsv.loc[(acsv.Name==aname)]
aif3= acsv[(acsv["Name"] == aname.lower()) & (acsv["Password"] == apass.lower())]
#aif2=acsv.loc[(acsv.Password==apass)]
#Checking If The Employee Name Matches A Name In The Clinic DataBase
if aif3.empty:
     print("Failed")
     c=input("Are you a new Employee(Y/N)-->")
     if c.upper()=='Y':
          anamem=input("Enter Administrator Name")
          apassm=input("Enter Administrator Password")
          if anamem==adminn:
               if apassm==adminp:
                    newname=input("Name-->")
                    newpass=input("Password-->")
                    newpass1=input("Password(Confirmation)-->")
                    if newpass==newpass1:
                         list12=[newname.lower(),newpass.lower()]
                         print(list12)
                         acsv.loc[len(acsv.index)] = list12
                         acsv.to_csv('admin.csv',index=False)
                    else:
                         print("The Passwords Do Not Match")
               else:
                    print("Incorrect Admin Password")
          else:
               print("Incorrect Admin Name")
     else:
          print("If You Are Not A New Employee")
else:
     #Checking If The Employee Password Matches The
     #Password In Front Of The Previously Entered Name
     if aif3.empty:
          print("Failed")
          c=input("Are you a new Employee(Y/N)-->")
          if c.upper()=='Y':
               anamem=input("Enter Administrator Name")
               apassm=input("Enter Administrator Password")
               if anamem==adminn:
                    if apassm==adminp:
                         newname=input("Name-->")
                         newpass=input("Password-->")
                         newpass1=input("Password(Confirmation)-->")
                         if newpass==newpass1:
                              list12=[newname,newpass]
                              print(list12)
                              acsv.loc[len(acsv.index)] = list12
                              acsv.to_csv('admin.csv',index=False)
                         else:
                              print("The Passwords Do Not Match")
                    else:
                         print("Incorrect Admin Password")
               else:
                    print("Incorrect Admin Name")
          else:
               print("If You Are Not A New Employee")
     else:
          system_doctor()




ask_exit()
