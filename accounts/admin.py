from django.contrib import admin
from .models import Product  # 👈 حرف كبير

admin.site.register(Product)