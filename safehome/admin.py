from django.contrib import admin
from .models import Region, Children, Crime, Fire_damage, Flood, Alcohol, House, Population,\
    Total, Total_rate, Draw_data

admin.site.register(Region)
admin.site.register(Children)
admin.site.register(Crime)
admin.site.register(Fire_damage)
admin.site.register(Flood)
admin.site.register(Alcohol)
admin.site.register(House)
admin.site.register(Population)
admin.site.register(Total)
admin.site.register(Total_rate)
admin.site.register(Draw_data)

# Register your models here.
