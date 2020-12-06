from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL, related_name='students')
    gpa = models.OneToOneField('Diary', null=True, on_delete=models.SET_NULL)
    book = models.ManyToManyField('Book', null=True, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    serial_number = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.serial_number}'


class Diary(models.Model):
    gpa = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.gpa}'


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    pages_amount = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.book_name}'
