from django.urls import path
from .views import RadioStationList

urlpatterns = [
    path('stations/', RadioStationList.as_view(), name='station-list'),
]
