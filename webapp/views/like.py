from django.shortcuts import redirect
from webapp.models import Like
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class LikePostView(LoginRequiredMixin, generic.View):
    def post(self, request):
        if request.method == 'POST':
            public_id = request.POST.get('public_id')
            user = request.user
            existing_like = Like.objects.filter(public_id=public_id, user=user).first()
            if existing_like:
                existing_like.delete()
            else:
                Like.objects.create(public_id=public_id, user=user)
            return redirect('index')
