from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_no=models.IntegerField(primary_key=True)
    dept_loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    dept_no=models.ForeignKey(Department,on_delete=models.CASCADE)
    emp_sal=models.IntegerField()

    def __str__(self):
        return self.emp_name

class Bonus(models.Model):
    bonus_amount=models.IntegerField()

    def __str__(self):
        return str(self.bonus_amount)

class Salgrade(models.Model):
    lowsal=models.IntegerField()
    highsal=models.IntegerField()
    grade=models.IntegerField()

    def __str__(self):
        return str(self.lowsal)