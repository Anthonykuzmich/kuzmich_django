from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def home(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'home_page.html', context)


def add_student(request):
    errors = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            errors = form.errors

    form = StudentForm()
    context = {
        'form': form,
        'errors': errors,
    }

    return render(request, 'add_student.html', context)
