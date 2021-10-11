from django.db import models
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _

"""
Pays
"""
COUNTRY = (
    # Translators: Pays
    (1, _('France')),
    (2, _('Canada')),
    (3, _('United States')),
)

class City(models.Model):
    """
    Ville
    """
    name = models.CharField(max_length=100, blank=False)
    zip_code = models.CharField(max_length=20, blank=False, )
    state = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    community = models.CharField(max_length=100, null=True)
    country = models.IntegerField(choices=COUNTRY, blank=False)

    class Meta:
        verbose_name_plural = _('Cities')
        verbose_name = _("City")

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.zip_code, self.state, self.country.name.upper())