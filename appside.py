import mysql.connector

mydb = mysql.connector.connect( #connect to database
    host="localhost",
    user="root",
    passwd="jackes78",
    database="studentrecords" # database name
    )
mycursor = mydb.cursor() 

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# cred = credentials.Certificate("serviceAccountKey.json")


def newstudet(studentid, name, phone = 0, email = 0):                       # adding new student
    sql = "INSERT INTO studentname(student_id, name) VALUES (%s, %s)"
    val = (studentid, name)
    mycursor.execute(sql, val)                                              #asking for student name/ id, and put the name with id into the studentname table.
    mydb.commit()
    print(mycursor.rowcount, "studnet name record inserted.")
    if (phone,email) != 0:                                                  #add phone and email to studentcontact table 
        sql = "INSERT INTO studentcontactinfo(student_id, phone, email) VALUES (%s, %s, %s)"
        val = (studentid, phone, email)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "student contact record inserted.")
    


def updateGrades(studentid, grade, subject, new = 0):
    if new == 1:                                                                #option 1 add a new student'd grade
        sql = "INSERT INTO studentgrade(student_id, grade, subject) VALUES (%s, %s, %s)"
        val = (studentid, grade, subject)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "student grade record inserted.")
    else:                                                                       #option 2 update a new student's contact info
        sql = "UPDATE studentgrade SET grade = %s, subject = %s WHERE student_id = %s;"
        val = (grade, str(subject), studentid)
        mycursor.execute(sql,val)
        mydb.commit()
        print("1 student grade record updated.")

def generatingReport(studentid):                                                # using studnetid to find all the info ralate to this student, generate a report
    mycursor.execute(f"SELECT major_name FROM major Where student_id ={studentid}")
    major =mycursor.fetchone()
    mycursor.execute(f"SELECT phone FROM studentcontactinfo Where student_id ={studentid}")
    phone =mycursor.fetchone()
    mycursor.execute(f"SELECT grade FROM studentgrade Where student_id = {studentid}")
    grade =mycursor.fetchone()
    mycursor.execute(f"SELECT name FROM studentname Where student_id = {studentid}")
    name =mycursor.fetchone()                                                  #list type tuple
    print(f"""With Student ID: {studentid} we found student:{name[0]}, his/her phone number is {phone[0]};
          GPA of this student is {grade[0]}, with major of {major[0]}.""")
    
def delete(studentid):                                                          #delete student from different tables
    mycursor.execute(f'DELETE FROM studentname WHERE student_id = {studentid}')
    mycursor.execute(f'DELETE FROM studentgrade WHERE student_id = {studentid}')
    mycursor.execute(f'DELETE FROM studentcontactinfo WHERE student_id = {studentid}')
    mycursor.execute(f'DELETE FROM major WHERE student_id = {studentid}')
    mydb.commit()
    print("1 student deleted from system.")

def functionSelections():
    while True:                                                                 #looping the options we have here, qustions.
        print('''
        Please type the number of the options:
          1. Add new student to the system
          2.Update grade for an student
          3.Generate Report for a student
          4.Delete student
          5.Exit
          ''')
        try:                                                                      #make sure only enter the numbers,except error when enter is not a int
            iput = int(input('Please type the selection: '))
        except ValueError:
            print('ERROR: please type in number from 1-4!')
        else:
            if iput == 1:                                                         #options, and ask to inputs so can be pass to functions
                id = input('Please type in the student id: ')
                name = input('Please type in the student name: ')
                phone = input('please enter student s phone number, if not hit ENTER key: ')
                email = input('please enter student s Email, if not hit ENTER key: ')
                newstudet(id,name, phone, email) #call newstudnet function
            elif iput == 2:
                new = ''
                while True:
                    new = input('Are you hoping to create a new record(Y/N): ')
                    if new in ('Y','y','n','N'):
                        if new in ('Y','y'):
                            new = 1
                        break
                id = input('Please type in the student id: ')
                grade = input('Please type in the students GPA: ')
                subject = input('please enter the subject: ')
                updateGrades(id, grade, subject, new) #call updateGrades function
            elif iput == 3:
                id = 0 
                while True:
                    try:
                        id = int(input('Please enter student ID: '))
                    except ValueError:
                        print('ERROR: please enter numbers only!')
                    else:
                        break
                generatingReport(id) #call generatingReport function
            elif iput == 4:
                id = 0
                while True:
                    try:
                        id = int(input('Please enter student ID you want to delete from the system: '))
                    except ValueError:
                        print('ERROR: please enter numbers only!')
                    else:
                        break
                delete(id) #call generatingReport function
            elif iput == 5:
                break


def main():
    print('Welcome to Student Records Managent system!')
    print('''There are all the options we have for now, 
          ''')
    functionSelections()                                                                #call function, where all the options will be provided and choice there.


        
        

main()