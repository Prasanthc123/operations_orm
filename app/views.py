from django.shortcuts import render
from django.http  import HttpResponse
from app.models import *

from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def display_dept(request):
    QLDO=Department.objects.all()
    QLDO=Department.objects.all().order_by('dept_name')
    QLDO=Department.objects.all().order_by('-dept_name')
    QLDO=Department.objects.filter(dept_loc='blr').order_by('-dept_name')
    QLDO=Department.objects.all().order_by(Length('dept_name'))
    QLDO=Department.objects.all().order_by(Length('dept_name').desc())
    QLDO=Department.objects.exclude(dept_loc='blr').order_by('dept_name')
    QLDO=Department.objects.filter(dept_loc='blr').order_by('dept_name')
    QLDO=Department.objects.all()
    QLDO=Department.objects.filter(dept_no__gt=50)
    QLDO=Department.objects.filter(dept_no__lt=50)
    QLDO=Department.objects.filter(dept_no__lte=50)
    QLDO=Department.objects.filter(dept_no__gte=50)
    QLDO=Department.objects.filter(dept_name__endswith='o')
    QLDO=Department.objects.filter(dept_name__startswith='o')
    QLDO=Department.objects.filter(dept_no__in=(10,20,30,40,50))

    QLDO=Department.objects.filter(dept_name__contains='t')
    QLDO=Department.objects.filter(dept_name__regex=r'\wt$')
    QLDO=Department.objects.filter(dept_name__regex=r'^o')

    QLDO=Department.objects.filter(dept_name='operation')
    QLDO=Department.objects.all().order_by('dept_no')[5:]
    QLDO=Department.objects.all()
    QLDO=Department.objects.filter(Q(dept_no=20) | Q(dept_no=60))
    QLDO=Department.objects.all()
    QLDO=Department.objects.filter(dept_loc='blr',dept_name='operation')
    Department.objects.filter(dept_no=50).update(dept_name='Police')
    QLDO=Department.objects.all()

    d={'Department':QLDO}

    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO=Employee.objects.all()
    #QLEO=Employee.objects.update_or_create(dept_no=10).filter(emp_name='Giri')
    d={'Employee':QLEO}

    return render(request,'display_emp.html',d)

def insert_dept(request):
    dn=input('enter the dn')
    dno=int(input(''))
    dl=input()
    NDO=Department.objects.create(dept_name=dn,dept_no=dno,dept_loc=dl)
    NDO.save()

    return render(request,'display_dept.html')
   
def insert_emp(request):
    en=input('enter the ename:')
    dno=input('enter the eno:')
    esal=int(input('enter the sal:'))
    NEO=Employee.objects.create(emp_name=en,dept_no=dno,emp_sal=esal)
    NEO.save()

    return render(request,'display_emp.html')

def update_emp(request):
    Department.objects.filter(dept_no=40).update(dept_no=10)

    QLDO=Department.objects.all()
    d={'Department':QLDO}

    return render(request,'display_dept.html',d)
