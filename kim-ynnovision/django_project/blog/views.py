from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Kim',
        'title': 'Blog post1',
        'content':'First post content',
        'date_posted':'February 6, 2025',
    },
    {
        'author': 'Jerome',
        'title': 'Blog post2',
        'content': 'Second post content',
        'date_posted': 'February 6, 2025',
    },

]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})