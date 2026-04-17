from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=100)
    inn = models.IntegerField()
    legal_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Employees(models.Model):
    employee_fio = models.CharField(max_length=100)
    passport_series = models.IntegerField()
    passport_number = models.IntegerField()
    address = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    start_date = models.DateField()