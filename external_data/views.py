import requests
from django.shortcuts import render

def weather_view(request):
    url = "https://api.open-meteo.com/v1/forecast?latitude=54.51&longitude=18.53&current_weather=true"
    data = None
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json().get('current_weather')
    except:
        pass
    return render(request, 'external_data/weather.html', {'weather': data})