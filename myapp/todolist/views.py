from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Category
import datetime


# Create your views here.

from django.shortcuts import render,redirect
from .models import TodoList, Category, Fruits


# Idea: make a fruit and a task for each task you make
#     When you delete the task, the fruit is not deleted
#     when the task is checked, the fruit appears and will stay there since it exists
#     eventually, the "fruit" wiill be checked



def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    allFruits = Fruits.objects.all()

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
            checkedList = request.POST.getlist("checkedbox")
            for i in checkedList:
                toDelete = TodoList.objects.get(id = int(i))
                toDelete.delete()

        if "addBasket" in request.POST:
            checkedList = request.POST.getlist("checkedbox")
            for i in checkedList:
                toDelete = TodoList.objects.get(id=int(i))
                toDelete.delete()
                newFruit = Fruits(title=toDelete.title)
                newFruit.save()

        if "emptyBasket" in request.POST:
            for i in allFruits:
                i.delete()
            return redirect("/list")


    return render(request, "index.html", {"todos": todos, "categories": categories, "allFruits": allFruits})


def login(request):
    return render(request, "login.html")


def home(request):
    return render(request, "home.html")
