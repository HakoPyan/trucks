from django.db.models import F, When, Case, Q, Value
from django.views.generic import ListView
from .models import Truck
from .forms import TruckForm


class TrucksView(ListView):
    model = Truck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TruckForm()
        return context

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.GET['model']:
            qs = qs.filter(model=self.request.GET['model'])

        qs = qs.annotate(overload=((F('current_capacity') - F('max_capacity')) * 100)/F('max_capacity'))
        qs = qs.annotate(overload=Case(When(overload__lte=0, then=0), default=F('overload')))
        return qs
