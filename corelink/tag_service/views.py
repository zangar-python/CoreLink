from rest_framework.views import APIView
from rest_framework.response import Response
from .services.service_tag import Tag_Service

class get_all_tags_views(APIView):
    def get(self,request):
        return Response(Tag_Service().get_tags())
class tag_info_views(APIView):
    def get(self,request,pk):
        return Response(Tag_Service().get_tag_info(pk))
    def delete(self,request,pk):
        if not request.user.is_superuser:
            return Response(data={"err":"Вам запрещен доступ к удалению тэгов"})
        return Response(Tag_Service().delete_tag(pk))