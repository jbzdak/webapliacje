from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import BlogPost
from .models import BlogComment


def index(request):
    posts = BlogPost.objects.order_by('-posted_at')  # lisa studentów
    template = loader.get_template('blog_app/index.html')  # Ładuje szablon
    context = {'posts': posts}  # Definiuje dane z których korzysta szablon
    return HttpResponse(template.render(context))  # Wyświetlam szablon i tworzę odpowiedź


def edit(request):
    if request.method == 'GET':
        try:
            context = check_post_id(request.GET)
        except BlogPost.DoesNotExist:
            return HttpResponse('Wrong post id', status=404)
        template = loader.get_template('blog_app/edit.html')  # Ładuje szablon
        return HttpResponse(template.render(context))  # Wyświetlam szablon i tworzę odpowiedź
    elif request.method == 'POST':
        if 'text' not in request.POST or len(request.POST['text'].strip()) == 0:
            try:
                context = check_post_id(request.POST)
            except BlogPost.DoesNotExist:
                return HttpResponse('Wrong post id', status=404)
            template = loader.get_template('blog_app/edit.html')
            return HttpResponse('Please add post text' + template.render(context), status=200)
        if request.POST['post_id'] != '':
            post = BlogPost.objects.get(pk=request.POST['post_id'])
        else:
            post = BlogPost()
        post.text = request.POST['text']
        post.save()
        return redirect("/index")


def check_post_id(request_type):
    if 'post_id' in request_type:
        post_id = request_type['post_id']
        post = BlogPost.objects.get(pk=post_id)
        context = {'post_id': post_id, 'post': post, 'comments': BlogComment.objects.order_by('posted_at')}
    else:
        context = {}
    return context


def post(request):
    template = loader.get_template('blog_app/post.html')
    if request.method == 'GET':
        try:
            context = check_post_id(request.GET)
        except BlogPost.DoesNotExist:
            return HttpResponse('Wrong post id', status=404)
        return HttpResponse(template.render(context))
    elif request.method == 'POST':
        if 'owner' not in request.POST or len(request.POST['text'].strip()) == 0 \
                or 'text' not in request.POST or len(request.POST['text'].strip()) == 0:
            try:
                context = check_post_id(request.POST)
            except BlogPost.DoesNotExist:
                return HttpResponse('Wrong post id', status=404)
            template = loader.get_template('blog_app/post.html')
            return HttpResponse('Please add both: nickname and commentary text' + template.render(context), status=200)
        comment = BlogComment()
        if request.POST['post_id'] != '' and 'post_id' in request.POST:
            try:
                comment.post = BlogPost.objects.get(pk=request.POST['post_id'])
            except BlogPost.DoesNotExist:
                return HttpResponse('Wrong post id', status=404)
        else:
            return HttpResponse('Wrong post id', status=404)
        comment.owner = request.POST['owner']
        comment.text = request.POST['text']
        comment.save()
        context = {'post': BlogPost.objects.get(pk=request.GET['post_id']), 'post_id':request.GET['post_id'], 'comments' : BlogComment.objects.order_by('posted_at')}
        return HttpResponse(template.render(context))
