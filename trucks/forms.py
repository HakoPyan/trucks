from django.forms import ModelForm
from .models import Truck


class TruckForm(ModelForm):

    class Meta:
        model = Truck
        fields = '__all__'
