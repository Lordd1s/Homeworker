from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from ORM_train import models
from utils import DB

# Create your views here.
def home(request):
    return render(request=request, template_name="home.html")


def create(request):
    if request.method == "GET":
        return render(request=request, template_name="create.html")

    elif request.method == "POST":
        name = str(request.POST.get("name"))
        title = str(request.POST.get("title"))
        description = str(request.POST.get("description"))

        # TODO request with SQL
        # DB.insert_to_db("INSERT INTO something (name, title, description) VALUES (?, ?, ?)", (name, title, description))

        # TODO request with ORM
        models.Something.objects.create(something=name, title=title, description=description)
        return redirect(reverse('all_list'))


def all_list(request):
    # TODO request with SQL
    # row = DB.select_all("SELECT name, title, description FROM something")
    # context = [
    #     {"name": x[0],
    #      "title": x[1],
    #      "description": x[2]
    #      } for x in row
    # ]

    # TODO request with ORM
    some_objs = models.Something.objects.all()
    return render(request=request, template_name="alls.html", context={'context': some_objs})
