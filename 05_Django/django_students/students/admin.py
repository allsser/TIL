from django.contrib import admin
from .models  import Students

# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
  list_display = ('pk', 'name', 'age', 'content', 'created_at', 'updated_at',)

admin.site.register(Students, StudentsAdmin)