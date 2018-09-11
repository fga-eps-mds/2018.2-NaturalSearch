from django.shortcuts import render

def home(request):
    return render(request,'natural_search/home.html')
    