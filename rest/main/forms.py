from django.forms import ModelForm
from .models import Project
class ProjectModelForm(ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'req_url')