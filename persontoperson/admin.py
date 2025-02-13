from django.contrib import admin
from .models import concatenation_points, distance_multiplier, plotimages, birthchartdb, PersonDegree, GlobalDegree
# Register your models here.
admin.site.register(concatenation_points)
admin.site.register(distance_multiplier)
admin.site.register(plotimages)
admin.site.register(birthchartdb)
admin.site.register(PersonDegree)
admin.site.register(GlobalDegree)
