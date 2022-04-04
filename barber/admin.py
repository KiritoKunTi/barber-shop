from django.contrib import admin
from .models import FAQ, Comments, Services, Barbers

# Register your models here.
admin.site.register(FAQ)
admin.site.register(Comments)
admin.site.register(Services)
admin.site.register(Barbers)


