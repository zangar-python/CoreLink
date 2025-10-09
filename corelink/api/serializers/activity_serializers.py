from corelink.infrastructure.db.models.activity import Activity
from rest_framework.serializers import ModelSerializer

class ActivitySerializer(ModelSerializer):
    class Meta:
        model=Activity
        fields= ["username","email","id"]
        