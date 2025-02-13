from django.contrib import admin
from .models import DateLisDB, MultiDateLisDB, divisionName, modelNames, TrendCharts, PlanetGroupNames, PlanetGroupers


admin.site.register(DateLisDB)
admin.site.register(MultiDateLisDB)
admin.site.register(divisionName)
admin.site.register(modelNames)
admin.site.register(TrendCharts)
admin.site.register(PlanetGroupNames)
admin.site.register(PlanetGroupers)