from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomAccountBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None
        else:
            user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            return user
        else:
            return None

