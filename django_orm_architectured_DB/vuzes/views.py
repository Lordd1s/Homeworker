from django.shortcuts import render
from vuzes import models

# Create your views here.
def home(request):
    students = models.Student.objects.all()
    print(students)
    return render(request=request, template_name="home.html", context={"students": students})
