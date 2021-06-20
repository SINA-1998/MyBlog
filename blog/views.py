from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello World! Hello Django!")


def api(request):
    data = {
        "1": {
            "title": "first article",
            "id": 1,
            "slug": "first-article"
        },
        "2": {
            "title": "second article",
            "id": 2,
            "slug": "second-article"
        },
        "3": {
            "title": "third article",
            "id": 3,
            "slug": "third-article"
        },
        "4": {
            "title": "fourth article",
            "id": 4,
            "slug": "fourth-article"
        },
        "5": {
            "title": "fiveth article",
            "id": 5,
            "slug": "fiveth-article"
        }
    }
    return JsonResponse(data)
