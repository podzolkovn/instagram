
from django.views import generic
from accounts.views.custom_login import CustomLoginView
from accounts.views.profile import ProfileView
from accounts.views.edit_profile import ChangePasswordView, SimpleUserUpdateView, BusinessUserUpdateView
from accounts.views.registration import RegisterView
from accounts.views.search import SearchView


class LoginRedirectView(generic.RedirectView):
    pattern_name = 'login'
