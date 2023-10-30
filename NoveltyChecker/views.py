from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "NoveltyChecker/index.html")

def login(request):
    return render(request, "NoveltyChecker/login.html")

def register(request):
    return render(request, "NoveltyChecker/register.html")

def account(request):
    return render(request, "NoveltyChecker/account.html")

def report(request):
    return render(request, "NoveltyChecker/report.html")

def searchResult(request):
    return render(request, "NoveltyChecker/listrecommendation.html")

def search(request):
    return render(request, "NoveltyChecker/search.html")

def feedback(request):
    return render(request,"NoveltyChecker/feedback.html")

def adminfeedback(request):
    return render(request,"NoveltyChecker/adminfeedback.html")
