from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render
from datetime import date
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# user_tasks = ["task one", "task two", "task three"]


class newTaskForm (forms.Form):
    single_task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=2)


# Create your views here.
"""
 Default page
 Show a list of current tasks
 input: tasks as a list
"""


def index(request):
    if "user_tasks" not in request.session:
        request.session["user_tasks"] = []
    context = {
        "tasksList": request.session["user_tasks"],
        "today": date.today()
    }
    return render(request, "tasks/index.html", context)


"""
 Add to the current list of tasks
 input: tasks as a list
        request
 
 request= GET
 - display the current list and allow for additional task to be added.
 request=POST
 - add the new task. redirect to display index 
"""


def add(request):
    if "user_tasks" not in request.session:
        request.session["user_tasks"] = []

    context = {
        "tasksList": request.session["user_tasks"],
        "today": date.today(),
        "form": newTaskForm ()
    }

    if request.method == "POST":
        returned_form: newTaskForm = newTaskForm(request.POST)
        if returned_form.is_valid():
            # request.session["user_tasks"] += returned_form.cleaned_data["single_task"]
            additional_task = returned_form.cleaned_data["single_task"]
            request.session["user_tasks"].append(additional_task)
            request.session.modified = True
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            context["form"] = returned_form

    return render(request, "tasks/add.html", context)


