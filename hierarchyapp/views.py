from django.shortcuts import render
from hierarchyapp.models import File

# Create your views here.


def indexview(request):
    files = File.objects.all()
    return render(request,"index.html",{"files":files})
