from . import views
from django.urls import path

urlpatterns = [path("get_project/<int:pk>", views.GetProjectData.as_view())]
