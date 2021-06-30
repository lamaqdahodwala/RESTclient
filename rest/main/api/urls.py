from . import views
from django.urls import path

urlpatterns = [
    path("get_project/<int:pk>", views.GetProjectData.as_view()),
    path("get_all_projects", views.GetAllProjects.as_view()),
]
