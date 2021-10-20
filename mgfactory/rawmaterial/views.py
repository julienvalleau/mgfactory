from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from rawmaterial.models import Supplier

class SuppliersListView(ListView):
  model = Supplier
  context_object_name = 'suppliers'
  paginate_by = 30
  template_name = 'rawmaterial/suppliers.html'
