from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/identity/login')
def index_view(request):
    context = {
        'welcome': "Welcome",
        'title': "Home"
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
        'page_title': "Irrigation schedule"
    }
    
    return render(request, 'irrigation.html', context)