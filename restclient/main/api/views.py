from .serializers import RestSerializer
from rest_framework.views import APIView


class CreateNewProject(APIView):
    http_method_names = ["POST"]

    def post(self, req):
        if req.user.is_authenticated:
            ...
