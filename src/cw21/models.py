from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    profession = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'