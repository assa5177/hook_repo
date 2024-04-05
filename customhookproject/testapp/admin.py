from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    my_list=['name']
admin.site.register(Student,StudentAdmin)

