from abc import abstractmethod, ABC


class People(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def talk(self):
        pass


class Teacher(People):

    def walk(self):
        return "Иду в универ"

    def talk(self):
        return "Разоговариваю со студентами"


class Student(People):

    def walk(self):
        return "Иду в универ"

    def talk(self):
        return "Разговариваю с преподавателем"


student = Student()
teacher = Teacher()

print(isinstance(student, People), student.talk())
print(isinstance(teacher, People), teacher.talk())

