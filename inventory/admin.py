from django.contrib import admin
from inventory.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Tag)
