from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'app/index.html', context=context)


class blog_page(ListView):
    """Displays the blog posts"""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'app/blog_page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['title'] = 'Blog'
        return context

class blog_post_detail(DetailView):
    """Displays one blog post in detail"""
    model = Post
    template_name = 'app/blog_post_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['title'] = 'Blog'
        return context


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
