from django.shortcuts import render, redirect
from .models import News, Product

def index(request):
    news = News.objects.all().order_by("-created_at")
    return render(request, "news/index.html", {"news": news})

def product(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "news/product.html", {"products": products})


def news_detail(request, id):
    news = News.objects.get(id=id)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context)


def create_news(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        News.objects.create(title=title, content=content, image=image)
        return redirect("index")
    return render(request, "news/create_news.html")



def delete_news(request, id):
    news = News.objects.get(id=id)
    news.delete()
    return redirect("index")

def edit_news(request, id):
    news = News.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        news.title = title
        news.content = content
        # Обновляем изображение только если загружено новое
        if image:
            news.image = image
        news.save()
        return redirect("news_detail", id=id)
    return render(request, "news/edit_news.html", {"news": news})