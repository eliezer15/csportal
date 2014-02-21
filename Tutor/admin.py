from django.contrib import admin
from Tutor.models import Post, Classes
# Register your models here.

admin.site.register(Classes)

class PostAdmin(admin.ModelAdmin):
    list_display=('pk','Title','Added','Updated','Course','Fname','Lname')
    
    
admin.site.register(Post, PostAdmin)