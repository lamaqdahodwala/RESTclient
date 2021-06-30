from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Project
from django.shortcuts import get_object_or_404


class GetProjectData(APIView):
    http_method_names = ["GET"]

    def get(self, req, pk):
        if req.user.is_authenticated:
            project = get_object_or_404(Project, pk=pk, owner=req.user)
            ser = ProjectSerializer(project)
            return Response(ser.data)
