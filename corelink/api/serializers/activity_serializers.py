from infrastructure.models import Activity
from rest_framework.serializers import ModelSerializer

class ActivitySerializer(ModelSerializer):
    class Meta:
        model=Activity
        fields= "__all__"
        