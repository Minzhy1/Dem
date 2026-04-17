from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .models import *

def prin(request):
    employes = Employees.objects.all().select_related('company')
    search_sotr = request.GET.get('search', '')
    if search_sotr:
        employes = employes.filter(employee_fio__icontains=search_sotr) # Получаем фио сотрудника

    positions = Position.objects.all()
    filter_sotr = request.GET.get('filter', '')
    if filter_sotr:
        employes = employes.filter(position__name__icontains=filter_sotr)

    return render(request,'home.html', {
        'employes':employes,
        'positions': positions,
        'search_sotr': search_sotr,
        'filter_sotr': filter_sotr
    })

def log_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request,'log.html')

def reg_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        user = User.objects.create_user(username=username, password=password)
        group = Group.objects.get(name=role)
        user.groups.add(group) # Добавляем пользователю уже созданые роли
        login(request, user)
        return redirect('home')
    return render(request, 'reg.html')

def delete_view(request, employees_id):
    employes = Employees.objects.get(id=employees_id)
    employes.delete()
    return redirect('home')

def red_view(request):
    company = Company.objects.all()
    position = Position.objects.all()
    if request.method == 'POST':
        employee_fio = request.POST.get('employee_fio')
        passport_series = request.POST.get('passport_series')
        passport_number = request.POST.get('passport_number')
        address = request.POST.get('address')
        company = Company.objects.get(id=company.id)
        position = Position.objects.get(id=position.id)
        start_date = request.POST.get('start_date')





