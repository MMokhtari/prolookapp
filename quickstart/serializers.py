from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers
# password = serializers.CharField(
#     style={'input_type': 'password'}
# )
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('url','username','password','email', 'groups')  #this are the labels that will be shown in the API
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        # return User.objects.create(**validated_data)
    def Update(self,instance,validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password',instance.password)
        instance.groups = validated_data.get('groups',instance.groups)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
