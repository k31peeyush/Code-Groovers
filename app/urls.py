from django.urls import path
from . import views

urlpatterns = [
    path('count/', views.get),
    path('mean/', views.mean),
    path('median/', views.median),
    path('percentile/', views.get_percentile, name='percentile'),
]
