from django.urls import path, include
from .views import TrucksView

urlpatterns = [
    path('', TrucksView.as_view(template_name="index.html"))
]