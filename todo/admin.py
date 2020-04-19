from django.contrib import admin
from .models import Item 
# Register your models here.
admin.site.register(Item)

# this gives us a more readable friendly item object in the admin panel
def __str__(self):
    return self.name
