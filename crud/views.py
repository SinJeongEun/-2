from django.shortcuts import  get_object_or_404, render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
# Create your views here.

def layout(request):
    return render(request, 'crud/layout.html')

def home(request):
    blogs=Blog.objects
    return render(request, 'crud/home.html', {'blogs': blogs})

def form(request):
    full_text=request.GET['fulltext']
    return render(request,'app/form.html',{'fulltext:full_text'})

def new(request):
    return render(request, 'crud/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/crud/home/')

def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'crud/new.html', {'form':form})  

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)  


def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')