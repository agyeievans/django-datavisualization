from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def index(request):
    data = CountryData.objects.all()
    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CountryDataForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

