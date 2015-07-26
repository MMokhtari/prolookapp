from django.contrib.auth.models import Group
from django.contrib.auth import  get_user_model
# from myuser.models import User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
User = get_user_model()

#the view set is simple class based view that have tow functions list and create

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
