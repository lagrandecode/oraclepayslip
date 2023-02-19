from django.contrib import admin
from .models import Grade, staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','gross_salary')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('positon','basic_salary')

admin.site.register(Grade,GradeAdmin)
admin.site.register(staff,StaffAdmin)



