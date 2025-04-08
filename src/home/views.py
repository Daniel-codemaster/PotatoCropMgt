from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

@login_required(login_url='/identity/login')
def index_view(request):
    weather_data = {}
    city = "Bulawayo"
    city = request.GET.get('city')
    if not city:
        city = "Bulawayo"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5305292cb9a1302dd53f917e0e5e2fba&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': f'{data['name']}, {data['sys']['country']}',
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        weather_data = {'error': 'City not found.'}
    context = {
        'welcome': "Welcome",
        'title': "Home",
        'weather_data': weather_data
    }
    return render(request, "index.html", context)

@login_required(login_url='/identity/login')
def fertilizer_pred_view(request):
    if request.method == 'POST':        
        return render(request, 'fertiliser.html', context)
    
    context = {
        'page_title': "Fertiliser prediction",
        'title': "Fertiliser prediction",
        'breadcrumb':"Breadcrumb"
    }
    
    return render(request, 'fertiliser.html', context)

@login_required(login_url='/identity/login')
def irrigation_shedule_pred_view(request):  
    if request.method == 'POST':        
        return render(request, 'irrigation.html', context)
       
    context = {
        'page_title': "Irrigation schedule",
        'title': "Fertiliser prediction",
        'breadcrumb':"Breadcrumb"
    }
    
    return render(request, 'irrigation.html', context)