from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import Project
from .forms import ProjectModelForm
# Create your views here.
def index(req):
    return render(req, "index.html")

def new_project(req):
    if req.method == 'POST':
        if req.user.is_authenticated:
            try:
                data = req.POST
                form = ProjectModelForm(data or None)
                inst = form.save(commit=False)
                inst.owner = req.user
                inst.save()
                return HttpResponseRedirect('/')
            except:
                messages.error(req, 'There was an error with your form')
                return HttpResponseRedirect('/new')
    else:
        form = ProjectModelForm
        return render(req, 'new_project.html', {'form': form})
