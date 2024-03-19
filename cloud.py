import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred,{'databaseURL':'https://camerarental-d3ccd-default-rtdb.firebaseio.com/'})

#save data/insert build a new database on firestone
ref = db.reference('py/')
users_ref = ref.child('user')
users_ref.set({
    100001: {
        'major': 'Computer Science',
        'gpa': '3.5',
        'name': 'John Smith',
        'contact': '123-456-7890'
    },
    100002: {
        'major': 'Biology',
        'gpa': '3.9',
        'name': 'Alice Johnson',
        'contact': '987-654-3210'
    },
    100003: {
        'major': 'Mathematics',
        'gpa': '3.2',
        'name': 'Bob Anderson',
        'contact': '555-123-4567'
    },
    100005: {
        'major': 'Physics',
        'gpa': '3.7',
        'name': 'David Miller',
        'contact': '444-555-6666'
    },
    100006: {
        'major': 'English',
        'gpa': '3.1',
        'name': 'Sophia Wilson',
        'contact': '777-888-9999'
    },
    100007: {
        'major': 'History',
        'gpa': '3.8',
        'name': 'Matthew Taylor',
        'contact': '555-777-8888'
    },
    100008: {
        'major': 'Psychology',
        'gpa': '3.6',
        'name': 'Olivia Martinez',
        'contact': '333-111-0000'
    },
    100009: {
        'major': 'Economics',
        'gpa': '3.4',
        'name': 'Michael Davis',
        'contact': '999-888-7777'
    },
    100010: {
        'major': 'Art',
        'gpa': '3.9',
        'name': 'Emma Thompson',
        'contact': '123-789-4560'
    },
    100011: {
        'major': 'Physics',
        'gpa': '3.2',
        'name': 'Daniel Robinson',
        'contact': '777-222-5555'
    },
    100013: {
        'major': 'Sociology',
        'gpa': '3',
        'name': 'Christopher White',
        'contact': '666-333-9999'
    },
    100014: {
        'major': 'Business Administration',
        'gpa': '3.8',
        'name': 'Ava Turner',
        'contact': '888-444-2222'
    },
    100015: {
        'major': 'Engineering',
        'gpa': '3.5',
        'name': 'Andrew Hall',
        'contact': '555-666-1111'
    },
    100016: {
        'major': 'Environmental Science',
        'gpa': '3.9',
        'name': 'Mia Garcia',
        'contact': '333-555-9999'
    },
    100017: {
        'major': 'Accounting',
        'gpa': '3.4',
        'name': 'William Wright',
        'contact': '777-444-1111'
    },
    100018: {
        'major': 'Communications',
        'gpa': '3.7',
        'name': 'Sophie Clark',
        'contact': '999-555-2222'
    },
    100019: {
        'major': 'Marketing',
        'gpa': '3.3',
        'name': 'Ethan Adams',
        'contact': '111-777-8888'
    },
    100020: {
        'major': 'Graphic Design',
        'gpa': '3.6',
        'name': 'Isabella Baker',
        'contact': '444-666-5555'
    },
    100021: {
        'major': 'Philosophy',
        'gpa': '3.8',
        'name': 'James Lee',
        'contact': '555-333-9999'
    },
    100022: {
        'major': 'Anthropology',
        'gpa': '3.2',
        'name': 'Grace Rodriguez',
        'contact': '666-777-2222'
    },
    100023: {
        'major': 'Linguistics',
        'gpa': '3.7',
        'name': 'Liam Hall',
        'contact': '777-555-1111'
    },
    100024: {
        'major': 'Theater Arts',
        'gpa': '3.5',
        'name': 'Ella Allen',
        'contact': '888-111-4444'
    },
    100025: {
        'major': 'Statistics',
        'gpa': '3.9',
        'name': 'Daniel Davis',
        'contact': '999-666-3333'
    },
    100026: {
        'major': 'Music',
        'gpa': '3.1',
        'name': 'Avery King',
        'contact': '111-777-4444'
    },
    100027: {
        'major': 'Chemical Engineering',
        'gpa': '3.6',
        'name': 'Benjamin Taylor',
        'contact': '333-222-6666'
    },
    100028: {
        'major': 'Social Work',
        'gpa': '3.7',
        'name': 'Scarlett Adams',
        'contact': '555-666-9999'
    },
    100029: {
        'major': 'Criminal Justice',
        'gpa': '3.4',
        'name': 'Logan Mitchell',
        'contact': '777-444-8888'
    },
    100030: {
        'major': 'Nursing',
        'gpa': '3.8',
        'name': 'Abigail Martin',
        'contact': '999-555-1111'
    },
    100031: {
        'major': 'Electrical Engineering',
        'gpa': '3.5',
        'name': 'Jackson Moore',
        'contact': '111-888-5555'
    },
    100032: {
        'major': 'Dance',
        'gpa': '3.9',
        'name': 'Lily Brown',
        'contact': '555-111-7777'
    },
    100033: {
        'major': 'Mechanical Engineering',
        'gpa': '3.2',
        'name': 'Caleb Martinez',
        'contact': '777-999-1111'
    },
    100034: {
        'major': 'Psychiatry',
        'gpa': '3.6',
        'name': 'Hannah Williams',
        'contact': '999-111-7777'
    },
    100035: {
        'major': 'Architecture',
        'gpa': '3.7',
        'name': 'Henry Hernandez',
        'contact': '111-666-3333'
    },
    100036: {
        'major': 'Astrophysics',
        'gpa': '3.4',
        'name': 'Amelia Turner',
        'contact': '333-111-6666'
    },
    100037: {
        'major': 'Education',
        'gpa': '3.5',
        'name': 'Samuel Scott',
        'contact': '555-666-8888'
    },
    100038: {
        'major': 'International Relations',
        'gpa': '3.9',
        'name': 'Victoria Thompson',
        'contact': '777-333-5555'
    },
    100039: {
        'major': 'Film Studies',
        'gpa': '3.1',
        'name': 'David Rodriguez',
        'contact': '999-666-2222'
    },
    100040: {
        'major': 'Health Sciences',
        'gpa': '3.8',
        'name': 'Eleanor Davis',
        'contact': '111-888-4444'
    },
    100041: {
        'major': 'Marketing',
        'gpa': '3.3',
        'name': 'Joseph Anderson',
        'contact': '555-777-2222'
    },
    100042: {
        'major': 'Public Health',
        'gpa': '3.6',
        'name': 'Penelope Garcia',
        'contact': '777-444-9999'
    },
    100043: {
        'major': 'Data Science',
        'gpa': '3.7',
        'name': 'Christopher Miller',
        'contact': '999-555-6666'
    },
    100044: {
        'major': 'Graphic Design',
        'gpa': '3.2',
        'name': 'Aria Harris',
        'contact': '111-333-7777'
    },
    100045: {
        'major': 'Philosophy',
        'gpa': '3.5',
        'name': 'Daniel Adams',
        'contact': '333-777-1111'
    },
    100046: {
        'major': 'Environmental Studies',
        'gpa': '3.9',
        'name': 'Zoe Turner',
        'contact': '555-111-9999'
    },
    100047: {
        'major': 'Geology',
        'gpa': '3.4',
        'name': 'Andrew Wright',
        'contact': '777-999-5555'
    },
    100048: {
        'major': 'Nutrition',
        'gpa': '3.6',
        'name': 'Natalie Wilson',
        'contact': '999-555-8888'
    },
    100049: {
        'major': 'Public Relations',
        'gpa': '3.7',
        'name': 'Jack Clark',
        'contact': '111-888-6666'
    },
    100050: {
        'major': 'Chemical Engineering',
        'gpa': '3.3',
        'name': 'Sophia Baker',
        'contact': '555-666-7777'
    }
    })

#input, insert a new student into the database
def insert(id, major, contactinfo, name, gpa=0):
    ref = db.reference('py/')
    users_ref = ref.child('user')
    users_ref.update({
        id : {
        'major': f'{major}',
        'gpa': f'{gpa}',
        'name': f'{name}',
        'contact': f'{contactinfo}'
        }
    })
    data = db.reference(f'py/user/{id}').get()
    print(f"""With Student ID: {id} we found student:{data['name']}, his/her phone number is {data['contact']};
        GPA of this student is {data['gpa']}, with major of {data['major']}.""")

#modify
def update(id, new):
    data = db.reference(f'py/user/{id}').get()
    major = data['major']
    name = data['name']
    contact = data['contact']
    ref = db.reference('py/')
    users_ref = ref.child('user')
    users_ref.update({
        id : {
        'major': f'{major}',
        'gpa': f'{new}',
        'name': f'{name}',
        'contact': f'{contact}'
        }
    })

#read
def generateRep(id):
    data = db.reference(f'py/user/{id}').get()
    print(f"""With Student ID: {id} we found student:{data['name']}, his/her phone number is {data['contact']};
        GPA of this student is {data['gpa']}, with major of {data['major']}.""")

#dalete the relative data was found with the studentid
def delete(id):
    db.reference(f'py/user/{id}').delete()
    print('Deleted')



#call all the functions
def functionSelections():
    while True:                                                                 #looping the options we have here, qustions.
        print('''
        Please type the number of the options:
          1.Add new student to the system
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
                id = int(input('Please type in the student id: '))
                name = input('Please type in the student name: ')
                phone = input('please enter student s phone number, if not hit ENTER key: ')
                major = input('please enter student s major: ')
                gpa = input('please enter student s GPA, if none, hit enter key: ')
                insert(id, major, phone, name, gpa) #call newstudnet function
            elif iput == 2:
                new = ''
                while True:
                    new = input('Are you hoping to create a new record(Y/N): ')
                    if new in ('Y','y','n','N'):
                        if new in ('Y','y'):
                            new = 1
                        break
                id = int(input('Please type in the student id: '))
                gpa = input('Please type in the students GPA: ')
                update(id, gpa) #call updateGrades function
            elif iput == 3:
                id = 0 
                while True:
                    try:
                        id = int(input('Please enter student ID: '))
                    except ValueError:
                        print('ERROR: please enter numbers only!')
                    else:
                        break
                generateRep(id) #call generatingReport function
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
    functionSelections()                #call function, where all the options will be provided and choice there


        
        

main()