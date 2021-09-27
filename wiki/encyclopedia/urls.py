from django.urls import path

from . import views

app_name = 'wiki'


urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("error", views.error, name="error"),
    path("edit", views.edit, name="edit"),
    path("<str:title>", views.page, name="page"),
]
