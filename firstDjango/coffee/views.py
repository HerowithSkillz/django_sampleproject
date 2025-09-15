from django.shortcuts import render
from .models import CoffeeVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_coffees(request):
    coffeeis = CoffeeVariety.objects.all()
    return render(request, 'coffee/all_coffee.html', {'coffeeis': coffeeis})

def coffee_details(request, coffee_id):
    coffee = get_object_or_404(CoffeeVariety, pk=coffee_id)
    return render(request, 'coffee/coffee_detail.html', {'coffee': coffee})
