# temp = ['1a - [1, 2, 3]', '1b - [4, 5, 6]']

def GetClasses():
    with open('Lesson_008\school\classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ') 
            print(classes)


#['1a','[1, 2, 3]', '1b','[4, 5, 6]']

GetClasses()