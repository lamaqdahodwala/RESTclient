from .serializers import RestSerializer
from rest_framework.views import APIView


class CreateNewProject(APIView):
    http_method_names = ["POST"]

    def post(self, req):
        if req.user.is_authenticated:
            data = {'user': req.user, 'name': req.data.get('name'), 'url': req.data.get('url')}
            ser = RestSerializer(data=data)