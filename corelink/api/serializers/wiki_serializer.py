from infrastructure.models import Wiki
from rest_framework.serializers import ModelSerializer

class WikiSerializer(ModelSerializer):
    class Meta:
        model = Wiki
        fields = "__all__"