from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from book_app import models as book_app_models

# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
# from . import serializers

#from rest_framework_simplejwt import views as jwt_views
from django.db.utils import IntegrityError

import datetime
import json
import os
import requests
# Create your views here.


@csrf_exempt
def test_headers(request):
    headers = [i for i in request.META if i.startswith('HTTP_')]
    for h in headers:
        print(h, request.META[h])
    return HttpResponse('OK')
