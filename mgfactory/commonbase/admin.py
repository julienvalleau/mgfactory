from django.contrib import admin
from commonbase.models import City
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _('mgFactory administration')
admin.site.site_title = _('mgFactory administration')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name', 'zip_code',)
    list_filter = ('country',)

    def get_form(self, request, obj=None, **kwargs):
            form = super(CityAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['zip_code'].widget.attrs['style'] = 'width: 70px;'
            return form