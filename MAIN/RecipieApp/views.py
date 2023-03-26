from django.shortcuts import render


# Create your views here.
def home( request ):
    return render(request, 'app/home.html',{})

def Recipie( request ):
    return render(request, 'app/Recipie.html',{})

def recipies( request ):
    return render(request, 'app/recipies.html',{})

def base( request ):
    return render(request, 'app/base.html',{})
