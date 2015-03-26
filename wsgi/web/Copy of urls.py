from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from blog.views import BlogController
import settings
admin.autodiscover()


urlpatterns = patterns('',
    
    # url(r'^$', 'web.views.home', name='home'),
     
#    url(r'^index/', include('web.blog.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^i18n/', include('django.conf.urls.i18n')),
     
     
    
)

urlpatterns +=  i18n_patterns('blog.views',
#   url(r'^index/', include('blog.urls')),

   
    url(r'^$', "index",name='home'),
    url(r'^index', "index",name='home'),
    url(r'^/index/(?P<orderby>\w+)/',"index",name='home'),
    url(r'^blog/page/pid=(\d+)', "viewpage",name='view'),
    url(r'^blog/page', "list", name='page'),
    url(r'^blog/contact', "contact",name='contact'),
    url(r'^blog/menu', "menu"),
    url(r'^blog/admin', "manager",name='manager'),
    url(r'^blog/video', "video",name='video'),
    url(r'^search/', include('haystack.urls')),
    url(r'^gallery/list', "gallery",name='gallery'),
)

urlpatterns +=  i18n_patterns('userprofile.views',

    url(r'^blog/login', "logins",name='login'),
    url(r'^blog/register', "signup",name='register'),
    url(r'^blog/logout', "out",name='logout'),
    url(r'^blog/user', "usercp",name='profile'),
    
    
)

urlpatterns += i18n_patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )




