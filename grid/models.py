from tabnanny import verbose
from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        