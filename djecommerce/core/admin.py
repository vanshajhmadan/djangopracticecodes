from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(Orders)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Refund)
