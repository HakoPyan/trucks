from django import forms
from .models import Truck


class TruckForm(forms.ModelForm):
    class Meta:
        field_name = forms.ModelChoiceField(
            queryset=Truck.objects.all().values_list('model', ),
            empty_label="All"
        )
