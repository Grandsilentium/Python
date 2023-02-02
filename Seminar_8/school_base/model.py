import view

# students
{1: {'First Name': 'Иван', 'Last Name': 'Иванов', 'Birthday': '2000-01-01'}}
# class
{'1a': [],'1b': []}
student_id_counter = 0
students = {}
classes = {}



def AddNewStudent():
    new_student = dict()
    new_student['Id'] = GetNewId()
    new_student['First Name'] = view.GetNewStudentInfo('student`s first name')
    new_student['Last Name'] = view.GetNewStudentInfo('student`s last name')
    new_student['Birthday'] = view.GetNewStudentInfo('student`s birthday')
    AddStudentsInClasses(new_student['Id'])
    return new_student


def GetNewId():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter


def SaveStudents(student):
    with open('Seminar_8\school_base\students.csv', 'a') as file:
        file.write(f"{student['Id']};{student['First Name']};{student['Last Name']};{student['Birthday']}\n")


def AddStudentsInClasses(student_id):
    global classes
    student_class = view.GetNewStudentInfo('student`s class')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]


def GetLastStudentId():
    global student_id_counter
    with open('Seminar_8\school_base\last_student_id.txt', 'r',encoding='utf-8') as file:
        student_id_counter = int(file.read())


def SaveLastStudentId():
    global student_id_counter
    with open('Seminar_8\school_base\last_student_id.txt', 'w',encoding='utf-8') as file:
        file.write(str(student_id_counter))


def SaveClasses():
    with open('Seminar_8\school_base\classes.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')


def GetClasses():
    with open('Seminar_8\school_base\classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ') 
            print(classes)
