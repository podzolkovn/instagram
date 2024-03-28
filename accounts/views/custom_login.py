from django.shortcuts import redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView

from accounts.backend import CustomAccountBackend


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = CustomAccountBackend().authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user, backend='accounts.backend.CustomAccountBackend')
            return redirect(reverse('profile', kwargs={'user_id': user.id}))

        return super().form_invalid(form)

