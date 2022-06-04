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
# TODO: split instances for different files, from . import views as supp_views; 

class SupportStuffCreate(APIView): # signup_user
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = serializers.CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                if user:
                    tokens = jwt_views.TokenObtainPairView.as_view()(request=request._request)
                    return tokens
            except IntegrityError:
                return Response(data={"error": "already exists"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupportStuffLoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        tokens = jwt_views.TokenObtainPairView.as_view()(request=request._request)
        return tokens
    

class CreateBookView(APIView):
    def post(self, request):
        data = request.data.dict()
        data.update({'user_id': request.user.id})
        serializer = serializers.BookSerializer(data=data)
        if serializer.is_valid():
            book = serializer.save()
            if book:
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_200_OK)


class UpdateBookView(APIView):
    # allow only by stuff
    def post(self, request):
        data = request.data.dict()
        serializer = serializers.BookSerializer(data=data)
        if serializer.is_valid():
            book = serializer.update()
            if book:
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_200_OK)

    
class CreateOfferView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        data = request.data.dict()
        serializer = serializers.OfferSerializer(data=data)
        if serializer.is_valid():
            offer = serializer.save()
            if offer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_200_OK)


class UpdateOfferView(APIView):
    def post(self, request):
        data = request.data.dict()
        serializer = serializers.OfferResolveSerializer(data=data)
        if serializer.is_valid():
            offer = serializer.save()
            if offer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_200_OK)
    
    
@csrf_exempt
def test_headers(request):
    headers = [i for i in request.META if i.startswith('HTTP_')]
    for h in headers:
        print(h, request.META[h])
    return HttpResponse('OK')
