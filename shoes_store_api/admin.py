from django.contrib import admin
from shoes_store_api.models import ShoeType, Shoe, Attributes

admin.site.register(ShoeType)
admin.site.register(Shoe)
admin.site.register(Attributes)
