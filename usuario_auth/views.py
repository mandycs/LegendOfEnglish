from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer


@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def user_register_view(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully registered a new user.'
            data['email'] = account.email
            data['username'] = account.username
            
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)