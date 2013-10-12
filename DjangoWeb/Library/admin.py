from django.contrib import admin
from DjangoWeb.Library.models import Publisher, Author, Book

#设置Admin也面的列表
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    #-表示排序的正或者反
    ordering = ('-publication_date',)
    #修改表单的feild
    #fields = ('title', 'authors', 'publisher')
    #多对多关系的表单填写
    filter_horizontal = ('authors',)

    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
