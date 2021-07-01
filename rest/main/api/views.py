from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Project
from django.shortcuts import get_list_or_404, get_object_or_404


class GetProjectData(APIView):
    # http_method_names = ['GET',]

    def get(self, req, pk):
        if req.user.is_authenticated:
            project = get_object_or_404(Project, pk=pk, owner=req.user)
            ser = ProjectSerializer(project)
            return Response(ser.data)


class GetAllProjects(APIView):
    def get(self, req):
        if req.user.is_authenticated:
            projects = get_list_or_404(Project, owner=req.user)
            ser = ProjectSerializer(projects, many=True)
            return Response(ser.data)

class ChangeNameOfProject(APIView):
    http_method_names = ['POST',]
    def post(self, req):
        if req.user.is_authenticated:
            p_id = req.data.get('id')
            to = req.data.get('to')
            project: Project = Project.objects.get(pk=p_id)
            project.project_name = to
            project.save()
            