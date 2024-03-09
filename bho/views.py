from django.shortcuts import render
from django.http import HttpResponse


posts=[
    {
        'author': 'Blaise Haala',
        'title': 'Blog post 1',
        'content': 'Twende',
        'date_posted':'August 27 2024'
    },

      {
        'author': 'Manu Obare',
        'title': 'Blog post 2',
        'content': 'Twendete',
        'date_posted':'September 30 2024'
    },
]


# Create your views here.
def home(request):
    context = {
        'posts':posts 
    }
    return render (request, 'bho/home.html', context)
    


def about(request):
    return render (request, 'bho/about.html', {'title':'About'})    