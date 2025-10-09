from rest_framework.authtoken.models import Token

class TokenRepository:
    def __init__(self):
        pass
    def create_or_get_tokenkey(self,user):
        token,_ = Token.objects.get_or_create(user=user)
        return token
    