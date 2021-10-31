from django.urls import path

from rawmaterial import views

urlpatterns = [
    path('suppliers/', views.supplier, name='suppliers'),
    path('suppliers/<int:pk>/', views.supplier_details, name='supplier_details'),
]