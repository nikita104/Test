from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model): #Студент
    name = models.CharField(max_length=30, verbose_name= 'Имя')
    patronymic = models.CharField(max_length=30, verbose_name= 'Отчество')
    surname = models.CharField(max_length=30, verbose_name= 'Фамилия')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=4, verbose_name= 'Группа')

    def __str__(self):
        return str(self.user)

    def fio(self):
        return f'{self.surname} {self.name} {self.patronymic}'



class TestStudent(models.Model): #Тест
    name = models.CharField(max_length=100, verbose_name='Название теста')
    discipline = models.CharField(max_length=100, verbose_name='Дисциплина')

    def __str__(self):
        return str(self.name)


class Question(models.Model): #Вопрос
    name = models.TextField(verbose_name='Вопрос')
    test = models.ForeignKey(TestStudent, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Answer(models.Model): #Варянты ответа
    name = models.CharField(verbose_name='Название', max_length=100)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return str(self.name)


class StudentAnswer(models.Model): #СтудентыОтветы
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    dc = models.DateTimeField(auto_now_add=True, db_index=1, verbose_name="Дата прохождения")

    def __str__(self):
        return str(self.id)


class Result(models.Model): #Htpekmnfn
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(TestStudent, on_delete=models.CASCADE)
    dc = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата прохождения")
    count_true = models.IntegerField()
    count_false = models.IntegerField()

    def __str__(self):
        return str(self.student)

# todo: methods __str__s