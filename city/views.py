from django.shortcuts import render

"""
API endpoint: https://data.sfgov.org/resource/65ik-7wqd.geojson

Doc: https://dev.socrata.com/foundry/data.sfgov.org/65ik-7wqd

Open Street Maps: https://www.openstreetmap.org/about
"""

# Create your views here.
def index(request):
    return render(request, 'index.html', {})