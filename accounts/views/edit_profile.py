
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import reverse, redirect
from django.contrib.auth import get_user_model, views
from django.views import generic
from django.urls import reverse_lazy

from accounts.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Profile


class ChangePasswordView(LoginRequiredMixin, views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'auth/change_password.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})


class SimpleUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'auth/simple_update_user.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_id': self.object.user_id})

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super().form_valid(form)


class BusinessUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'auth/business_update_user.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_id': self.object.id})

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super().form_valid(form)

