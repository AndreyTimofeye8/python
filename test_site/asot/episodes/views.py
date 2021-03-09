from django.shortcuts import render

# Create your views here.

def index(requests):
    print(requests)
    return HttpResponse ('Hello world')
