from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from AuthAccount.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False,style={'input_type': 'password'})
    company = serializers.StringRelatedField()
    # confirm_password = serializers.CharField(write_only=True, required=False,style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name','is_admin','is_super_staff','is_staff', 'company','tagline', 'password',
                  )
        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.tagline = validated_data.get('tagline', instance.tagline)
        instance.company = validated_data.get('company', instance.company)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.is_super_staff = validated_data.get('is_super_staff', instance.is_super_staff)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()

        password = validated_data.get('password', None)
        # confirm_password = validated_data.get('confirm_password', None)
        # (password == confirm_password) and
        if (password != None):
            instance.set_password(password)
            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

        return instance
    # def validate(self, data):
    #     """
    #     Check that the start is before the stop.
    #     """
    #     if data['username'] == 'poolgazal@gmail.com':
    #         raise serializers.ValidationError("rambo dos exist dude")
    #     else:
    #         return data
