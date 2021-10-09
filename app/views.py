from django.shortcuts import render

from .models import Tweet
from .serializers import TweetSerializer

from rest_framework import viewsets

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-datetime')
    serializer_class = TweetSerializer