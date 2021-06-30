from . import views
from django.urls import path

urlpatterns = [path("get_project", views.GetProjectData.as_view())]
