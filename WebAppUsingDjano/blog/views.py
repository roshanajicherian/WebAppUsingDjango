from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# home controls traffic of the homepage. Stored in a list of dictionaries
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # Third argument of render passes the content to the html file. It must be a dictionary
    # of the content to pass
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
