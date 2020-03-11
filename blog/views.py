from django.shortcuts import get_object_or_404, render
from blog.models import Blog
def home1(request):
    projects=Blog.objects.all()
    return render(request,'blog/home1.html',{'blog':projects})
def home2(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/home2.html',{'blog2':blog})