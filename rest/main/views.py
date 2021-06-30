from django.shortcuts import render
from django.views.generic import CreateView
from .models import Project
# Create your views here.
def index(req):
    return render(req, "index.html")

class NewProjectView(CreateView):
    model = Project
    template_name = 'new_project.html' 
    success_url = '/'
