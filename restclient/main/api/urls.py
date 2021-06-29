from django.urls import path
from . import views

urlpatterns = [
    path("/new", views.CreateNewProject.as_view()),
    path("/load/<int:pk>", views.LoadProject.as_view()),
]
