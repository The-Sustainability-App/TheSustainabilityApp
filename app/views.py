from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'app/index.html', context=context)


def blog_page(request):
    context = {
        'title': 'Blog',
    }
    return render(request, 'app/blog_page.html', context=context)


def app(request):
    context = {
        'title': 'Our App',
    }
    return render(request, 'app/app.html', context=context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'app/about.html', context=context)
