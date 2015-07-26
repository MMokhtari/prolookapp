# import the Account object
from django.contrib.auth.models import check_password
from AuthAccount.models import Account

# Name my backend 'MyCustomBackend'
class ProlookappBackend:

    # Create an authentication method
    # This is called by the standard Django login procedure
    def authenticate(self, username=None, password=None):

        try:
            # Try to find a user matching your username
            user = Account.objects.get(username=username)
            if user != None:
                pwd_valid = check_password(password, user.password)
                if pwd_valid:
                    return user
            return None
        except Account.DoesNotExist:
            try:
                user = Account.objects.get(email=username)
                if user != None:
                    pwd_valid = check_password(password, user.password)
                    if pwd_valid:
                        return user
                return None
            except Account.DoesNotExist:
                return None
    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None