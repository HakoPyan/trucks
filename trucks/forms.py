from django import forms
from .models import Model, Truck


class TruckForm(forms.ModelForm):
    model = forms.ModelChoiceField(queryset=Model.objects.all(), required=None, empty_label="All")

    class Meta:
        model = Truck
        fields = ('model', )
