from ..models import Project
from rest_framework.serializers import ModelSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("owner", "request_url", 'project_name', 'pk')
