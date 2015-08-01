from django.contrib import admin
from .models import *

class ProgrammeAdmin(admin.ModelAdmin):
	list_display=['heading','description','album','image1','image2','image3']

class GuestAdmin(admin.ModelAdmin):
	list_display=['name','email']

class MessageAdmin(admin.ModelAdmin):
	list_display=['message','author']

class PhotoAdmin(admin.ModelAdmin):
	list_display=['image_tag','album']

class ArticleAdmin(admin.ModelAdmin):
	list_display=['title','author']

admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Album)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Article,ArticleAdmin)
