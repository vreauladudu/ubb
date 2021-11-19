class Student:
    '''
    Creeaza un nou student cu un ID (studentId), un nume (studentName) si o grupa (studentGroup)
    paramtype:                          int                  string                    int
    '''

    def __init__(self, studentId, studentName, studentGroup):
        self.__studentId = studentId
        self.__studentName = studentName
        self.__studentGroup = studentGroup

    def getStudentId(self) -> int:
        return self.__studentId

    def getStudentName(self) -> str:
        return self.__studentName

    def getStudentGroup(self) -> int:
        return self.__studentGroup

    def setStudentId(self, id):
        self.__studentId = id

    def setStudentName(self, name):
        self.__studentName = name

    def setStudentGroup(self, group):
        self.__studentGroup = group

    def __eq__(self, other) -> bool:
        return self.__studentId == other.getStudentId()

    def __str__(self) -> str:
        return 'ID: ' + str(self.__studentId) + ' | Nume: ' + self.__studentName + ' | Grupa: ' + str(self.__studentGroup)

def test_Student():
    student1 = Student(1001, 'Mihai Panduru', 215)
    assert(student1.getStudentId() == 1001)
    assert(student1.getStudentName() == 'Mihai Panduru')
    assert(student1.getStudentGroup() == 215)

    student1.setStudentId(1002)
    student1.setStudentName('Andrei Paunescu')
    student1.setStudentGroup(212)

    assert(student1.getStudentId() == 1002)
    assert(student1.getStudentName() == 'Andrei Paunescu')
    assert(student1.getStudentGroup() == 212)

    student2 = Student(1002, 'Alberto Mihai', 215)
    assert(student1 == student2)

    student3 = Student(1001, 'Alberto Mihai', 215)
    assert(student2 != student3)

test_Student()

class Task:
    '''
    Creeaza o noua problema cu un ID (laboratory_task), o descriere (description) si un termen limita (deadline)
    paramtype:                            string                       string                           string
    '''

    def __init__(self, laboratory_task, description, deadline):
        self.__laboratory_task = laboratory_task
        self.__description = description
        self.__deadline = deadline

    def getLaboratory_Task(self) -> str:
        return self.__laboratory_task

    def getDescription(self) -> str:
        return self.__description

    def getDeadline(self) -> str:
        return self.__deadline

    def setLaboratory_Task(self, laboratory_task):
        self.__laboratory_task = laboratory_task

    def setDescription(self, description):
        self.__description = description

    def setDeadline(self, deadline):
        self.__deadline = deadline

    def __eq__(self, other) -> bool:
        return self.__laboratory_task == other.getLaboratory_Task()

    def __str__(self) -> str:
        self.__laboratoryNumber, self.__taskNumber = self.__laboratory_task.split('_')
        return 'Laborator: ' + self.__laboratoryNumber + ' | Problema: ' + self.__taskNumber + ' | Descriere: ' + self.__description + ' | Termen limita: ' + self.__deadline

def test_Task():
    task1 = Task('7_2', 'Catalog', '8/11/2021')
    assert(task1.getLaboratory_Task() == '7_2')
    assert(task1.getDescription() == 'Catalog')
    assert(task1.getDeadline() == '8/11/2021')

    task1.setLaboratory_Task('8_4')
    task1.setDescription('Gestionare')
    task1.setDeadline('3/12/2021')

    assert(task1.getLaboratory_Task() == '8_4')
    assert(task1.getDescription() == 'Gestionare')
    assert(task1.getDeadline() == '3/12/2021')

    task2 = Task('8_4', 'Complex', '2/3/2022')
    assert(task1 == task2)

    task3 = Task('7_2', 'Complex', '2/3/2022')
    assert(task2 != task3)

test_Task()
