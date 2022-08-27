from django.shortcuts import render, redirect
from .forms import Postform
from .models import Post

def postview(request):
    post = Post.objects.all()

    return render (request, 'index.html', {
      'post': post,

    })

def editview(request,post_id):
    update = Post.objects.get(pk=post_id)
    form = Postform(request.POST or None, instance=update)  

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'update.html', {
        'update' : update,
        'form' : form
    })

def deleteview(request,post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request,'delete.html')

def readview(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request,'view.html',{
        'post': post
    })

def formsview(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Postform()

    form = Postform()

    return render (request, 'form.html', {
      'form': form  
    })

