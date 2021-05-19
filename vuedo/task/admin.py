from django.contrib import admin

from .models import Variable, BooleanValue, StringValue

admin.site.register(Variable)
admin.site.register(BooleanValue)

admin.site.register(StringValue)
