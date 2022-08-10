from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Account
from users.API.serializers import RegistrationSerializer, AccountSerializer
from rest_framework import generics
from rest_framework import permissions
class AccountList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser]

class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser]

class AccountDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser]

#ver datos del usuario
class Profile(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = AccountSerializer(self.request.user)
        return Response(serializer.data)



#AUTH
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['reponse'] = 'el registro fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'access': str(refresh.access_token)
            }
            return Response(data)

        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    data = {}
    if request.method =='POST':
        email = request.data.get('email')
        password = request.data.get('password')

        account = auth.authenticate(email=email, password=password)
        if account is not None:
            data['response'] = 'el login fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)

            data['token'] = {
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['response'] = 'credenciales incorrectas'
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)