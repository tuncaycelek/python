from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")     #return HttpResponse("<h3> Ana Sayfa HTTP </h3>")