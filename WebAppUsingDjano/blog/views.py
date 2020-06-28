from django.shortcuts import render
from django.http import HttpResponse
# home controls traffic of the homepage. Stored in a list of dictionaries
posts = [
    {'author': 'Roshan Aji Cherain',
     'title': 'Blog post sample',
     'date_posted': '22nd Jan 2019',
     'content': 'lorem episulm1'
     },
    {'author': 'John Doe',
     'title': 'Blog post sample by john',
     'date_posted': '22nd Jan 2020'
     }
]


def home(request):
    context = {
        'posts': posts
    }
    # Third argument of render passes the content to the html file. It must be a dictionary
    # of the content to pass
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
