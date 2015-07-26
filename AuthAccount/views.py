from rest_framework import permissions, viewsets

from AuthAccount.models import Account
from AuthAccount.permissions import IsAccountOwner
from AuthAccount.permissions import IsAdmin
from AuthAccount.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        # very basic permission
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        # if request.method == 'GET':

        #     if request.user.is_authenticated():
        #         # redirect to his working page
        #         return redirect('/workplace/')
        # else:
        #     content = {
        #         'user': request.user.username,  # `django.contrib.auth.User` instance.
        #         'auth': request.auth,
        #         'title':'ProLookApp Sign Up'  # None
        #     }
        #     # return redirect('/')
        #     return Response({'content': content}, template_name='./home/register.html')

    # if post then this user passed his info lets save them
        if request.method == 'POST':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                # serializer.save()
                
                Account.objects.create_superuser(**serializer.validated_data)
                content={
                    'created':serializer.validated_data,
                    'status':'VALID_INFO'
                }
                print(serializer.validated_data['username'])
                print(serializer.validated_data['password'])
                user = authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password'])
                auth_login(self.request, user)
                return Response(content)
            content={'content':serializer.errors,
            'status':'INVALID_INFO'}    
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            # any other method
            pass

