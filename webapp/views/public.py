from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy

from webapp.forms import CommentForm, PublicForm
from webapp.models import Public
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Follow


class PublicViews(LoginRequiredMixin, generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'publics'
    model = Public
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        followed_users = Follow.objects.filter(follower=user).values_list('following', flat=True)
        return Public.objects.filter(user__in=followed_users) | Public.objects.filter(user=user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            public_id = request.POST.get('public_id')
            comment = form.save(commit=False)
            comment.public_id = public_id
            comment.user = request.user
            comment.save()
            return redirect('index')
        else:
            return super().get(request, *args, **kwargs)


class PostCreate(LoginRequiredMixin, generic.CreateView):
    pk_url_kwarg = 'id'
    model = Public
    template_name = 'posts/create_post.html'
    form_class = PublicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


