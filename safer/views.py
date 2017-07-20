from django.shortcuts import render

import simplejson as json

def get_home_chart():
    data_file = './static/safer/json/home.json'
    with open(data_file) as f:
        data = json.load(f)
    return data

# Create your views here.
def deploy_test(request):
    return render(request, 'deploy_test.html', {})

def index(request):
    data = get_home_chart()
    price = data['price']
    volume = data['volume']
    return render(request, 'safer/index.html', {'price': price, 'volume': volume})

def tinder(request):
    return render(request, 'safer/tinder_prac.html', {})