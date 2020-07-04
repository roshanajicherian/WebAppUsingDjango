from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
# home controls traffic of the homepage. Stored in a list of dictionaries


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # Third argument of render passes the content to the html file. It must be a dictionary
    # of the content to pass
    return render(request, 'blog/home.html', context)

# Class Based Views


# List View used for blogs subscription list in youtube i.e
# anything displayed in the form of a list
# The class inherits from the type of view
class PostListView(ListView):
    model = Post
    # <app>/<model>_<view_type>.html -> default format of searching the template
    # By specifying template name we are
    # overriding the path where django
    # searches for the template
    template_name = 'blog/home.html'
    # By default the context list is reffered
    # as query list by django.
    # To change that specify a varible
    # as below with the required name
    context_object_name = 'posts'
    # Changes the order of display of posts. The '-' sign
    # specified to display the posts as newest to oldest
    ordering = ['-datePosted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-datePosted')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
