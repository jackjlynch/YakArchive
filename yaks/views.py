from django.shortcuts import render
from django.http import HttpResponse
from yaks.models import Yak, Comment, YakLocation

# Create your views here.

def index(request):
    output = ""
    for location in YakLocation.objects.all():
        output += "<h1>" + location.name + "</h1>"
        for yak in Yak.objects.filter(yaklocation=location).order_by("-time"):
            output += "<p><h2>" + yak.message + " (" + str(yak.likes) + ")</h2>"
            for comment in Comment.objects.filter(message_id=yak.message_id).order_by("-time"):
                output += comment.comment + " (" + str(comment.likes) + ")<br/>"
            output += "</p>"
    return HttpResponse(output)