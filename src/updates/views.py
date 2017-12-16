from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Update



def update_user_model(request):
    data = {
        "count": 1000,
        "content": "Some content"
    }
    return JsonResponse(data)
