
from django.shortcuts import redirect, reverse
from django.contrib.auth import login, get_user_model
from django.views import generic

from accounts.forms import CustomUserCreationForm

User = get_user_model()


class RegisterView(generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'auth/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.request.POST.get('next') or self.request.GET.get('next') or reverse('login')
