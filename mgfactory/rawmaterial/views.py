from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from rawmaterial.models import Supplier

class SuppliersListView(ListView):
  model = Supplier
  paginate_by = 25
  template_name = 'rawmaterial/suppliers.html'
