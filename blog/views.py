from django.shortcuts import render
from .models import Post
# Create your views here.

posts= [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'content': 'First Post Content',
        'datePosted': 'September 12, 2022'
    },
    {
        'author': 'John Doe',
        'title': 'Second Post',
        'content': 'Second Post Content',
        'datePosted': 'September 13, 2022'
    }
]

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
        return render(request, 'blog/about.html',{'title': 'About'})
