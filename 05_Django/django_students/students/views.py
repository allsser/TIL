from django.shortcuts import render, redirect
from .models import Students


# Create your views here.
def index(request):
  students = Students.objects.all()[::-1]
  context = {'students': students}
  return render(request,'students/index.html', context)

def new(request):
  return render(request, 'students/new.html')

def detail(request, students_pk):
  students = Students.objects.get(pk=students_pk)
  context = {'students':students}
  return render(request, 'students/detail.html',context)

def create(request):
  name = request.POST.get('name')
  age = request.POST.get('age')
  content = request.POST.get('content')

  student = Students(name=name, age=age, content=content)
  student.save()

  return redirect('students:detail', student.pk)

def edit(request, students_pk):
  student = Students.objects.get(pk=students_pk)
  context = {'student':student}
  return render(request,'students/edit.html', context)

def update(request, students_pk):
  student = Students.objects.get(pk=students_pk)
  student.name = request.POST.get('name')
  student.age = request.POST.get('age')
  student.content = request.POST.get('content')
  student.save()
  return redirect('students:detail', student.pk)

def delete(request, students_pk):
  student = Students.objects.get(pk=students_pk)
  student.delete()
  return redirect('students:index')