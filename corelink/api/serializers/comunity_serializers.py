from comunity_service.models import Comunity,Message
from rest_framework.serializers import ModelSerializer

class ComunitySerializer(ModelSerializer):
    class Meta:
        model = Comunity
        fields = "__all__"
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"