from django.contrib import admin

from .models import (
    Category,
    Region,
    District,
    Color,
    Item,
)

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Color)
admin.site.register(Item)
