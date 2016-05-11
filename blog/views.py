from django.shortcuts import render

#from .models import Post

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(id > 0 )
    return render(request, 'blog/home.html')
def personal_details(request):
    return render(request, 'blog/personal_details.html')
def login(request):
    return render(request,'blog/login.html')
