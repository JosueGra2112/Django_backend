from django.urls import path
from .views import RadioStationList, update_favorite_status

urlpatterns = [
    path('', RadioStationList.as_view(), name='station-list'),
    path('update_favorite/', update_favorite_status, name='update-favorite'),
]
