from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Category
import datetime


# Create your views here.

from django.shortcuts import render,redirect
from .models import TodoList, Category


def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager

    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            return redirect("/list")  # reloading the page

        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            if "checkedbox" in request.POST:
                checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
                toDelete = TodoList.objects.get(id = int(checkedlist))
                toDelete.delete()



    return render(request, "main.html", {"todos": todos, "categories": categories})

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")
