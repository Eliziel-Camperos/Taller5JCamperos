from django.shortcuts import render
from cbtis_app import urls
# Create your views here.
def index(request):
    return render(request,"index.html")
