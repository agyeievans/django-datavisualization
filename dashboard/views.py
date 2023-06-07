from django.shortcuts import render
from .models import CountryData

# Create your views here.
def index(request):
    data = CountryData.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'dashboard/index.html', context)