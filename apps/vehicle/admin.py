from django.contrib import admin

from .models import Vehicle, VehicleType, Park, Asign
# Register your models here.

class AsignInline(admin.TabularInline):
    """Tabular Inline View for Recipe"""

    model = Asign
    extra = 0


class VehicleAdmin(admin.ModelAdmin):
    inlines = [AsignInline]
    list_display = ('plate','color', 'Vehicle_type')



admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleType)
admin.site.register(Park)