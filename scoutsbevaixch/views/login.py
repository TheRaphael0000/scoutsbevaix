from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.conf import settings


def log(request):
    context = {
        "auth": request.session.get("auth", default=False)
    }
    return render(request, "log.html", context=context)


def login(request):
    args = dict(request.POST)
    if "pass" in args and args["pass"][0] == settings.PASSWORD:
        request.session["auth"] = True
    return redirect("log")


def logoff(request):
    request.session["auth"] = False
    return redirect("log")
