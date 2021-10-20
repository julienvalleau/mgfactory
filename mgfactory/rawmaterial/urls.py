from django.urls import path

from rawmaterial import views
from rawmaterial.views import SuppliersListView

urlpatterns = [
    path('suppliers/', SuppliersListView.as_view(), name='suppliers'),
]