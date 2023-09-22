from django.contrib import admin

from .models import (
    Catergory,
    Region,
    District,
    Color,
    Item,
)

admin.site.register(Catergory)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Color)
admin.site.register(Item)
