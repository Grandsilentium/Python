import view
import model




def Start():
    model.GetLastStudentId()
    model.GetClasses()
    stop = False
    while not stop:
        model.SaveStudents(model.AddNewStudent())
        if view.GetNewStudentInfo(' "q" to stop').lower() == 'q':
            stop = True
    model.SaveClasses()
    model.SaveLastStudentId()