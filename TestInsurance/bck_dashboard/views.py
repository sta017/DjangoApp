from django.shortcuts import render
from .forms import HeroInsuranceForm
from .models import HeroInsurance

def insurance_form(request):
    if request.method == 'POST':
        form = HeroInsuranceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            hero_insurance = HeroInsurance(**form.cleaned_data)
            hero_insurance.save()
    else:
        form = HeroInsuranceForm()
    return render(request, 'dashboard/templates/insurance_form.html', {'form': form})
