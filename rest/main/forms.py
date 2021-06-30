from django.forms import ModelForm
import django.forms
from .models import Project
class ProjectModelForm(ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'request_url')
        widgets = {
            'project_name': django.forms.TextInput(attrs={'class': 'input'}),
            'request_url': django.forms.TextInput(attrs={'class': 'input'})

        }