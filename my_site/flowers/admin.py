from django.contrib import admin
from flowers.models import Flowers

# Register your models here.
class FlowersAdmin(admin.ModelAdmin):
    fields = ["name_flower"]
    list_display = ["name_flower"]


admin.site.register(Flowers, FlowersAdmin)