from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from post.models import Post


# Create your views here.
class PostListView(ListView, PermissionRequiredMixin):
    model = Post
    template_name = 'post/post_list.html'
    permission_required = 'post.view_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('account_login'))

        return response


class PostDetailView(DetailView, PermissionRequiredMixin):
    model = Post
    template_name = 'post/post_detail.html'
    permission_required = 'post.view_post'


class PostCreateView(CreateView, PermissionRequiredMixin):
    model = Post
    permission_required = 'post.add_post'
    fields = ['image', 'type']
    success_url = reverse_lazy('index')
