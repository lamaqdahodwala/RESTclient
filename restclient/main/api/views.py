from rest_framework.response import Response

from .serializers import RestSerializer
from rest_framework.views import APIView
from ..models import RestProject


class CreateNewProject(APIView):
    http_method_names = ["POST"]

    def post(self, req):
        if req.user.is_authenticated:
            data = {
                "user": req.user,
                "name": req.data.get("name"),
                "api_url": req.data.get("api_url"),
            }
            ser = RestSerializer(data=data)
            if ser.is_valid():
                ser.save()


class LoadProject(APIView):
    http_method_names = ["GET"]

    def get(self, req, pk):
        if req.user.is_authenticated:
            project = RestProject.objects.get(pk=pk, user=req.user)
            ser = RestSerializer(project)
            return Response(ser.data)
