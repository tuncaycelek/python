from django.shortcuts import render, HttpResponse, redirect
from .forms import ArticleForm
from .models import Article
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")     #return HttpResponse("<h3> Ana Sayfa HTTP </h3>")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request,"dashboard.html",{"articles":articles})

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale girişi yapıldı.")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    article = Article.objects.filter(id = id).first()
    return render(request,"detail.html",{"article":article})


