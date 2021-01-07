import random


class Student:
    def __init__(self, name, age, surname, group):
        self.name = name
        self.age = age
        self.surname = surname
        self.group = group
        self.points = []
        self.grade = 1
        self.sredni = 0

    def marks(self, point):
        if 0 < point < 100:
            self.points.append(point)

    def random_osenka(self, x, y):
        for i in range(20, 100):
            j = random.randint(x, y)
            self.points.append(j)

    def srednya(self):
        a = sum(self.points) / len(self.points)
        self.sredni = a

    def prohod(self):
        if self.sredni >= 60:
            self.grade += 1
            self.points.clear()
        else:
            self.grade = self.grade
            self.points.clear()


student1 = Student(name='Ruslan', age=15, surname='sultangaziev', group=1)


class Cursavay:
    def __init__(self, student, len_of_text):
        self.student = student
        self.len_of_text = len_of_text
        self.sredniy = 0
        self.point = 0

    def class_work(self):
        self.sredniy = self.len_of_text // 20
        if self.sredniy >= 60:
            self.point += 10
        elif self.point > 0:
            if self.sredniy <= 40:
                self.point -= 10
        else:
            self.point = self.point
        name = self.student
        if name.startswith('R'):
            self.point += 3
        elif name.startswith('D'):
            self.point += 5
        elif name.startswith('H'):
            self.point += 2
        elif name.startswith('F'):
            self.point += 1
        elif name.startswith('S'):
            self.point += 4
        elif name.startswith('A'):
            self.point -= 3
        elif name.startswith('C'):
            self.point -= 5
        elif name.startswith('N'):
            self.point -= 2
        elif name.startswith('L'):
            self.point -= 1
        elif name.startswith('T'):
            self.point -= 4


cursavay1 = Cursavay(student1.name, random.randint(500, 2000))
cursavay1.class_work()
print(cursavay1.student.name)
'''
import random


class Student:

    def __init__(self, name, age, surname, group):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.points = []
        self.grade = 1
        self.avg = 0

    def marks(self, point):
        if 0 < point < 100:
            self.points.append(point)

    def average(self):
        averag = sum(self.points) / 100
        self.avg = averag

    def judge(self):
        ave = sum(self.points) / 100
        if ave < 61:
            if self.grade == 1:
                self.grade = self.grade = 1
            else:
                self.grade = self.grade - 1
        else:
            self.grade = self.grade + 1


student1 = Student(name='Asan', age='45', surname='Kulikov', group='IB1-17')

i = 0
while i < 100:
    x = random.randint(50, 100)
    student1.marks(x)
    i = i + 1


class StudentWork:

    def __init__(self, student, total_words):
        self.student = student
        self.total_words = total_words
        self.score = 0

    def get_score(self):
        self.score = self.total_words / 20
        if self.student.avg > 50:
            self.score += 10
        elif 30 < self.student.avg < 50:
            self.score -= 10


work1 = StudentWork(student1, random.randint(500, 2000))
work1.get_score()
print(work1.student.name, work1.score)
'''
