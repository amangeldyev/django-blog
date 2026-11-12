from django.shortcuts import render
from django.http import HttpResponse

def blog_list(request):
    return render(request, 'blog/blog_list.html')

def about(request):
    return HttpResponse("Biz haqimizda sahifasi")

def contact(request):
    return HttpResponse("Aloqa sahifasi")

def blog_detail(request, blog_id):
    return HttpResponse(f"Blog ID: {blog_id} tafsilotlari")