from django.shortcuts import render
from django.http import HttpResponse


posts=[
    {
        'author': 'Blaise Haala',
        'title': 'Blog post 1',
        'content': 'Twende',
        'date_time':'August 27 2024'
    },

      {
        'author': 'Blaise Haala',
        'title': 'Blog post 1',
        'content': 'Twende',
        'date_time':'August 27 2024'
    },
]


# Create your views here.
def home(request):
    return render (request, 'bho/home.html')
    


def about(request):
    return render (request, 'bho/about.html')
    