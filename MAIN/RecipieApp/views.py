from django.shortcuts import render , get_object_or_404
from .models import Cook, Category, Post


# Create your views here.
def home( request ):
    return render(request, 'app/home.html',{})

def Recipie( request ): 
    return render(request, 'app/Recipie.html',{})

def recipies( request ):
    Post = get_object_or_404(Post, slug=slug) 
    context = {
        'Post':Post
    }
    
    return render(request, 'app/recipies.html', context)

def base( request ):
    return render(request, 'app/base.html',{})
