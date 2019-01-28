from django.urls import path
from . import views

urlpatterns = [
    path('<entry_name>/', views.TrackingView.as_view(), name='tracking'),
]