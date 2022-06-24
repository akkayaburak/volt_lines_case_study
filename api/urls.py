from django.urls import path
from api.views import (
    PassengerApiView,
)

urlpatterns = [
    path('api/', PassengerApiView.as_view()),
]