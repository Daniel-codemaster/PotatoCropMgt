from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import joblib, os, requests, random
import pandas as pd
from django.conf import settings

# Load the model once (global load — efficient)
MODEL_PATH = os.path.join(settings.BASE_DIR, 'home', 'model', 'fertilizer_npk_model.pkl')
# fertilizer_model = joblib.load(MODEL_PATH)

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
        # Load model
        #fertilizer_model = joblib.load('fertilizer_npk_model.pkl')

        # Example prediction 
        sample = pd.DataFrame([{
            "Soil Type": "Loamy Sand",
            "pH": 6.5,
            "Drainage": "Poor",
            "Soil Color": "Orange",
            "Soil Characteristics": "Alkaline soil, requires conditioning"
        }])

        # pred = fertilizer_model.predict(sample)[0]
        npk, fertilizer = get_random_fertilizer_recommendation()
        context = {
            'page_title': "Fertiliser prediction",
            'title': "Fertiliser prediction",
            'breadcrumb':"Breadcrumb",
            'npk': npk,
            'fertilizer': fertilizer
        }
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

def get_random_fertilizer_recommendation():
    recommendations = [
        ("110-80-80", "Green manure, farmyard manure (4.5 t/ha)"),
        ("95-65-65", "Vermicompost, cow manure (5 t/ha)"),
        ("110-80-80", "Bone meal, seaweed extract (4.5 t/ha)"),
        ("85-55-55", "Green manure, farmyard manure (4.5 t/ha)"),
        ("95-65-65", "Compost, green manure (4 t/ha)"),
        ("90-60-60", "Compost, poultry manure (5-7 t/ha)"),
        ("70-40-40", "Cow manure, green compost (6 t/ha)"),
        ("70-40-40", "Farmyard manure, compost (5.5 t/ha)"),
        ("100-70-70", "Bone meal, seaweed extract (4.5 t/ha)"),
        ("85-55-55", "Vermicompost, cow manure (5 t/ha)"),
        ("80-50-50", "Compost, poultry manure (5-7 t/ha)"),
        ("80-50-50", "Vermicompost, farmyard manure (4 t/ha)"),
        ("90-60-60", "Compost, poultry manure (5-7 t/ha)"),
        ("70-40-40", "Mulch, biochar (5-6 t/ha)"),
        ("110-80-80", "Vermicompost, cow manure (5 t/ha)"),
        ("85-55-55", "Biochar, poultry manure (6 t/ha)"),
        ("65-35-35", "Cow manure, green compost (6 t/ha)"),
        ("90-60-60", "Compost, poultry manure (5-7 t/ha)"),
        ("100-70-70", "Vermicompost, cow manure (5 t/ha)"),
        ("80-50-50", "Bone meal, seaweed extract (4.5 t/ha)"),
    ]
    
    return random.choice(recommendations)