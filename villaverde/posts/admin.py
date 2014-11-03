from django.contrib import admin

from .models import Post, Category, Image

class ImageInline(admin.StackedInline):
	model = Image
	extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'creation_date', 'category', 'user')
	inlines = [ImageInline,]

admin.site.register(Category)
admin.site.register(Image)