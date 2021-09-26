from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    bdate = f"{date.today().month}{ date.today().day }" == "11"
    context = {"date": bdate}
    return render(request, "newyear/index.html", context)

# "date": str(date.today())

