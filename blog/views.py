from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def personal_details(request):
    return render(request, 'blog/personal_details.html', {})
