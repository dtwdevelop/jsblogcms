from django.contrib import admin
from blog.models import Category,Tag,Page,Comment,Config,Item,Gallery
from django.http import HttpResponse
from django.core import serializers
from imagekit.admin import AdminThumbnail

def hide(modeladmin, request, queryset):
    
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

hide.short_description = 'operations'
# Register your models here.
class BlogAdminCategory(admin.ModelAdmin):
    
    

    actions = [
        hide
    ]
    save_on_top= True
    list_display =('title_category','pub_date','hide_me','up_me',)
    
    def hide_me(self, obj):
        # how to send param not from post but   get like category
        return '<a href="" class="btn">Hide</a> '.format(obj.id)
      
    
    hide_me.short_description = 'Hide'
    hide_me.allow_tags = True
    
    def up_me(self, obj):
        # how to send param not from post but   get like category
        return '<a href="" class="btn">Up</a><br/><a href="" class="btn">Down</a>'.format(obj.id) 
    
    up_me.short_description = 'up'
    up_me.allow_tags = True
   
    #fields = ['title','post','pub_date']
    
    
class BlogAdminPage(admin.ModelAdmin):
    save_on_top= True
    
    list_display =['id','title','topic']
    list_filter = ['pub_date']
    search_fields = ['title']
#     actions = [make_page,pageup]
    list_display_links = ('title',)
    
    def title_category(self, instance):
        return instance.category.title_category

       
class BlogAdminTag(admin.ModelAdmin):
    list_display =('name',)
    #fields = ['title','post','pub_date']
    pass

class BlogAdminItem(admin.ModelAdmin):
    save_on_top= True
    list_display =('title','item_id','item_url',)
    
    
    def category(self, instance):
        return Category()
    
    
class BlogAdminGallery(admin.ModelAdmin):
    list_display =('title','avatar','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')
    
    pass

    
admin.site.register(Category,BlogAdminCategory)
admin.site.register(Tag,BlogAdminTag)
admin.site.register(Page,BlogAdminPage)
admin.site.register(Comment)
admin.site.register(Config)
admin.site.register(Item,BlogAdminItem)
admin.site.register(Gallery,BlogAdminGallery)
# admin.site.add_action(hide, 'hide')