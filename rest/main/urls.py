from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new', views.new_project, name='new_project'),
    path('project/<int:pk>', views.workspace, name='workspace')
]
