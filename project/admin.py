from django.contrib import admin

# Register your models here.
from .models import Laptop , Profile , Review
admin.site.register(Laptop)
admin.site.register(Profile)
admin.site.register(Review)