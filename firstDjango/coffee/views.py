from django.shortcuts import render
from .models import CoffeeVariety
from django.shortcuts import get_object_or_404
from .forms import CoffeeVarietyForm
from .models import Store

# Create your views here.
def all_coffees(request):
    coffeeis = CoffeeVariety.objects.all()
    return render(request, 'coffee/all_coffee.html', {'coffeeis': coffeeis})

def coffee_details(request, coffee_id):
    coffee = get_object_or_404(CoffeeVariety, pk=coffee_id)
    return render(request, 'coffee/coffee_detail.html', {'coffee': coffee})

def coffee_store_view(request):
    stores = None  # Placeholder for actual store data
    if request.method == 'POST':
        form = CoffeeVarietyForm(request.POST)
        if form.is_valid():
            coffee_variety = form.cleaned_data['coffee_variety']
            stores = Store.objects.filter(coffee_varieties=coffee_variety)
    else:
        form = CoffeeVarietyForm()
    return render(request, 'coffee/coffee_stores.html',
    {'stores': stores, 'form': form})
