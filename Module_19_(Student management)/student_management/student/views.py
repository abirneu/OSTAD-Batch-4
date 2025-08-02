from django.shortcuts import render, HttpResponse, redirect
from .import models
from . import forms
from django.contrib import messages

# Create your views here.
#Three types oḟform in django

#This is HTML form

#This is model form

def create_student(request):
    if request.method == 'POST': #1. user post requesţkoreche
        form = forms.StudentForm(request.POST, request.FILES) #2. user post request capture korlam
        if form.is_valid(): #3. user input validation 
            form.save() #4. form er data save korlam
            messages.add_message(request, messages.SUCCESS, 'Student Created  successfully.')

            return redirect('home')
        
    else:
        form = forms.StudentForm() 
        
    return render( request, 'student/create_edit_student.html', {'form': form})

def home(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students': students})
#student data updater er jonno
def update_student(request, id):
    student = models.Student.objects.get(id=id) #collecting student info using id
    form = forms.StudentForm(instance=student) #student form er data fill up kora thakbe

    # form = forms.StudentForm() 
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Updated  successfully.')

            return redirect('home')

    return render( request, 'student/create_edit_student.html', {'form': form , 'edit':True})
# student selete  er jonno
def delete_student(request, id):
    student = models.Student.objects.get(id= id) #1. id=id wala student ke khuje ber korlam
    student.delete() #2. oi student object ke delete korlam
    messages.add_message(request, messages.SUCCESS, 'Student Deleted  successfully.')

    return redirect('home') #3. successfull hole take home page e redirect kore dew


