from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from accounts.forms import SearchForm


class SearchView(LoginRequiredMixin, generic.View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'base.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = get_user_model().objects.filter(
                Q(username__icontains=query) |
                Q(email__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            ).distinct()
            return render(request, 'search_results.html', {'results': results, 'query': query})
        return render(request, 'base.html', {'form': form})
