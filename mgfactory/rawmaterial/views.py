from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from rawmaterial.models import Supplier
from .forms import SupplierForm

def supplier(request):
  suppliers_list = Supplier.objects.all()
  page = request.GET.get('page', 1)

  paginator = Paginator(suppliers_list, 25)
  try:
    suppliers = paginator.page(page)
  except PageNotAnInteger:
    suppliers = paginator.page(1)
  except EmptyPage:
    suppliers = paginator.page(paginator.num_pages)

  if request.META.get('HTTP_HX_REQUEST') != 'true':
    return render(request, 'rawmaterial/suppliers.html', { 'name_view' : _('suppliers'), 'suppliers': suppliers })
  
  return render(request, 'rawmaterial/suppliers_list.html', { 'suppliers': suppliers })

def supplier_details(request, pk):
  supplier = get_object_or_404(Supplier, pk=pk)
  form = SupplierForm(instance=supplier)

  return render(request, 'rawmaterial/supplier_details.html', {'form' : form})
      

    
