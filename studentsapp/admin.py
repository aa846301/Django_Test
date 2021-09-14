from django.contrib import admin
from studentsapp.models import student

# Register your models here.
""" admin.site.register(student) """

class studentAdmin(admin.ModelAdmin):
    #第三種方式，
    list_display = ('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter = ('cName','cSex')
    search_fields = ('cName',)
    ordering = ('id',)

""" class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr') """
admin.site.register(student,studentAdmin)
