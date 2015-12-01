from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import BlogPost

def index(request):
    posts = BlogPost.objects.order_by('-posted_at') # lisa studentów
    template = loader.get_template('blog_app/index.html') # Ładuje szablon
    context = {'posts': posts} # Definiuje dane z których korzysta szablon
    return HttpResponse(template.render(context)) # Wyświetlam szablon i tworzę odpowiedź

def edit(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = BlogPost.objects.filter(pk=post_id)
        template = loader.get_template('blog_app/edit.html') # Ładuje szablon
        context = {'post_id' : post_id, 'post' : post }
        return HttpResponse(template.render(context)) # Wyświetlam szablon i tworzę odpowiedź
    elif request.method == 'POST':
        post_id = request.POST['post_id']
        post = BlogPost()
        post.text = request.POST['text']
        post.save()
        return redirect("/index")