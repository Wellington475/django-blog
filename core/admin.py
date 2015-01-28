from django.contrib import admin
from core.models import Post, Comment
# Register your models here.
class CommentInline(admin.StackedInline):
	model = Comment
	extra = 1

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,   {'fields' : ['title']}),
		('Message', {'fields' : ['message']}),
		('Date', {'fields' : ['date_publication']})
	]
	list_display = ('title', 'message', 'date_publication', 'publication_today')
	inlines = [CommentInline]

admin.site.register(Post, PostAdmin)