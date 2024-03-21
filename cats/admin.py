from django.contrib import admin
from cats.models import Student, Cat

#class CatAdmin(admin.ModelAdmin):
  #  list_display = ('name', 'student')


#class StudentAdmin(admin.ModelAdmin):
 #   list_display = ('first_name', 'last_name', 'number_of_cats')


# Register your models here.
admin.site.register(Cat)
admin.site.register(Student)
