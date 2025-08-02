from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def profile(request):
  user_data = {
    "name": "Abir",
    "age" :16
  }
  marks = [
    {
      "id":1,
      "subject": "Math",
      "marks":90
    },
    {
        "id":2,
      "subject": "H.math",
      "marks":80
    },
    {
        "id":3,
      "subject": "Bangla",
      "marks":60
    },
    {
        "id":4,
      "subject": "English",
      "marks":70
    },
    {
        "id":5,
      "subject": "Science",
      "marks":50
    }

  ]
  #student table er sob data querry kore niye asa
  student_data = models.Student.objects.all()
  # print(student_data)
  return render(request, 'student/index.html', {"marks":marks,
                'student_data': student_data})


def delete_student(request, id):
  student = models.Student.objects.get(id=id)
  student.delete()
  return HttpResponse("Student delete successfully")


