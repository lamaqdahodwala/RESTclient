from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new', views.NewProjectView.as_view(), name='new_project')
]
