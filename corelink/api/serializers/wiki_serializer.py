from infrastructure.models import Wiki,Request_To_Change_Wiki
from rest_framework.serializers import ModelSerializer


class WikiSerializer(ModelSerializer):
    class Meta:
        model = Wiki
        fields = "__all__"

class Reques_to_change_serializer(ModelSerializer):
    class Meta:
        model = Request_To_Change_Wiki
        fields = "__all__"