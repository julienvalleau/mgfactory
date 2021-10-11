from django.shortcuts import render

from django.http import HttpResponse


def suppliers(request):
    context = {}
    return render(request, "rawmaterial/suppliers.html", context)
