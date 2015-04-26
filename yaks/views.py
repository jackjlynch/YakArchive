from django.shortcuts import render
from django.http import HttpResponse
from yaks.models import Yak

# Create your views here.

def index(request):
    return HttpResponse('<br /><br / >'.join([y.message for y in Yak.objects.order_by('-time')]))