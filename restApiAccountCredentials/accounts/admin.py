from django.contrib import admin
# Register your models here.
from . models import Student

@admin.register(Student) # decorator
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuname', 'stuemail', 'stupass')
# #
# # @admin.register(Student) # decorator
# # # class StudentAdmin(admin.ModelAdmin):
# # #     list_display = ('stuname', 'stuemail', 'stupass')