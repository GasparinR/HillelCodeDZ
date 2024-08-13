class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record Book: {self.record_book}"


class GroupFullException(Exception):
    def __init__(self, message="Group is full. Cannot add more students."):
        super().__init__(message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'Bill', 'Gates', 'AN150')
st4 = Student('Female', 22, 'Ada', 'Lovelace', 'AN151')
st5 = Student('Male', 27, 'Elon', 'Musk', 'AN152')
st6 = Student('Female', 24, 'Marie', 'Curie', 'AN153')
st7 = Student('Male', 26, 'Isaac', 'Newton', 'AN154')
st8 = Student('Female', 23, 'Rosalind', 'Franklin', 'AN155')
st9 = Student('Male', 29, 'Albert', 'Einstein', 'AN156')
st10 = Student('Female', 21, 'Grace', 'Hopper', 'AN157')
st11 = Student('Male', 31, 'Nikola', 'Tesla', 'AN158')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except GroupFullException as e:
    print(e)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
