from django.contrib import admin

from .models import Contact,Person

@admin.register(Contact,Person)
class ContactAdmin(admin.ModelAdmin):
 	pass
# admin.site.register(Contact)
# admin.site.register(Person)
