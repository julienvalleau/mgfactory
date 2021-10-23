from django.db import models
from django.utils.translation import ugettext_lazy as _
from commonbase import models as Commonbase

class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    adress = models.CharField(max_length=200, blank=True, verbose_name=_('Adress'))
    zipcode = models.CharField(max_length=10, blank=True, verbose_name=_('Zip code'))
    city = models.CharField(max_length=50, blank=True, verbose_name=_('City'))
    province = models.CharField(max_length=2, choices=Commonbase.PROVINCE, blank=True, verbose_name=_('Province'))
    state = models.CharField(max_length=2, choices=Commonbase.STATE, blank=True, verbose_name=_('State'))
    country = models.CharField(max_length=2, choices=Commonbase.COUNTRY, default='FR', blank=False, verbose_name=_('Country'))

    def __str__(self):
        return self.name.upper()

    class Meta:
        verbose_name = _('supplier')
        ordering = ['name']
