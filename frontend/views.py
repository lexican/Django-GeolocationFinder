from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.


def index(request):
    context = {
    }
    return render(request, 'index.html', context)

def geoLocation(request):
    content = str(request.GET.get('ip'))
    url = 'http://localhost:8000/myipfinder/' + content
    print(url)
    r = requests.get(url)
    data = r.json()
    return JsonResponse(data, safe=False)