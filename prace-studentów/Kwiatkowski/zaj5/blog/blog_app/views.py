from django.shortcuts import loader, HttpResponse, get_object_or_404
from django.shortcuts import redirect

from .models import BlogPost


def index(request):
    posts = BlogPost.objects.all().order_by('-posted_at')
    template = loader.get_template('index.html')
    context = {'posts': posts}
    return HttpResponse(template.render(context))

def edit_post(request):
    template = loader.get_template('edit_post.html')
    context = {'has_text': True}
    if request.method == 'GET':
        if 'post_id' in request.GET:
            post_id = request.GET['post_id']
            post = get_object_or_404(BlogPost, pk=post_id)
            context['post_text'] = post.text
            context['edited'] = post_id
        return HttpResponse(template.render(context))

    elif request.method == 'POST':
        if 'text' not in request.POST or \
        request.POST['text'].strip() == '':
            context['has_text'] = False
            return HttpResponse(template.render(context))
        else:
            if 'edited' in request.POST and request.POST['edited']!='':
                blogpost = BlogPost.objects.get(pk=request.POST['edited'])
            else:
                blogpost = BlogPost()
            blogpost.text = request.POST['text']
            blogpost.save()
            return redirect("/index")

    else:
        return HttpResponse(status=405)
