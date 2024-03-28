
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Follow, Profile

User = get_user_model()


class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = 'auth/profile.html'
    context_object_name = 'user_obj'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_user = self.get_object()
        Profile.objects.get_or_create(user=self.object)
        context['is_following'] = False

        if self.request.user.is_authenticated and self.request.user != target_user:
            context['is_following'] = Follow.objects.filter(follower=self.request.user, following=target_user).exists()

        return context

    def post(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        target_user = self.get_object()

        if request.user.is_authenticated and request.user != target_user:
            if 'follow' in request.POST:
                Follow.objects.get_or_create(follower=request.user, following=target_user)
            elif 'unfollow' in request.POST:
                Follow.objects.filter(follower=request.user, following=target_user).delete()

        return redirect('profile', user_id=user_id)

