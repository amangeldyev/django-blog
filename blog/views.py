from django.shortcuts import render
from django.http import Http404

BLOGS = [
    {"id": 1, "title": "django nima", "author": "Nurjigit",
     "text": "Django bu Python uchun kuchli veb-framework. U tez va xavfsiz saytlar yaratishga yordam beradi."},
    {"id": 2, "title": "shablonlar bilan ishlash", "author": "Nurjigit",
     "text": "Shablonlar HTML ichida Python ma'lumotlarini ko'rsatish imkonini beradi."},
    {"id": 3, "title": "url va view'lar", "author": "Nurjigit",
     "text": "URL manzilni view bilan bog'laydi, view esa javob qaytaradi."},
]

def blog_list(request):
    return render(request, 'blog/blog_list.html', {"blogs": BLOGS})

def about(request):
    return render(request, 'blog/about.html', {"name": "Django blog", "year": 2026})

def contact(request):
    return render(request, 'blog/contact.html', {"email": "info@example.com", "phone": "+998 90 123 45 67"})

def blog_detail(request, blog_id):
    for blog in BLOGS:
        if blog["id"] == blog_id:
            return render(request, 'blog/blog_detail.html', {"blog": blog})
    raise Http404("Maqola topilmadi")