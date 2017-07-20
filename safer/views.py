from django.shortcuts import render

# Create your views here.
def deploy_test(request):
    return render(request, 'deploy_test.html', {})

def index(request):
    return render(request, 'safer/index.html', {})

def tinder(request):
    return render(request, 'safer/tinder_prac.html', {})