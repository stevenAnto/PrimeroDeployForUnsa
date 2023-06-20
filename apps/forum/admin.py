from django.contrib import admin
from .models import Customuser, School, Section, Tag, Post, Comment, ReactPost, SavePost, Report 

# Register your models here.

admin.site.register(Customuser)
admin.site.register(School)
admin.site.register(Section)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ReactPost)
admin.site.register(SavePost)
admin.site.register(Report)