from django.contrib import admin
from hierarchyapp.models import File
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
# Register your models here.


admin.site.register(File, DraggableMPTTAdmin)