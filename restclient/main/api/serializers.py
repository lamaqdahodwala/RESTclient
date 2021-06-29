from rest_framework.serializers import ModelSerializer
from ..models import RestProject


class RestSerializer(ModelSerializer):
    class Meta:
        model = RestProject
        fields = ("user", "name", "url")
