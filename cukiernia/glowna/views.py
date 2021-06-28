from django.http import HttpResponse
from django.shortcuts import render


def glowna(request):
    return render(request,'glowna/base.html')
