from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def home(request): # Read - list view
    blogs = Blog.objects.all() # select * from Blog
    return render(request, "home.html", {"blogs":blogs})

def detail(request,id): # Read - detail view
    blog = get_object_or_404(Blog, pk=id)
    return render(request,'detail.html', {'blog':blog})
    # Blog : <title="생략", content="생략", created_at=생략>

def new(request): # Create를 위해 리소스 띄우기
    return render(request, "new.html")

def create(request): # Create
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content']
    new_blog.save()
    return redirect('blog:detail', new_blog.id)

def edit(request, id): # Update를 위해 렌더링한 리소스 띄우기
    edit_blog = get_object_or_404(Blog, pk=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id): # Update
    update_blog = get_object_or_404(Blog, pk=id)
    update_blog.title = request.POST["title"]
    update_blog.content = request.POST["content"]
    update_blog.save()
    return redirect("blog:detail", update_blog.id)

def delete(request, id): # Delete
    delete_blog = get_object_or_404(Blog, pk=id)
    delete_blog.delete()
    return redirect('blog:home')

