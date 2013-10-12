from django.conf.urls import patterns, include, url
#Index就是路由的名称，源自于什么文件
from DjangoWeb.View.Index import index,detail,hours_ahead,template,home,search,contact



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#元组中第一个元素是模式匹配字符串（正则表达式）；
	#第二个元素是那个模式将使用的视图函数
	('^$',index ), 
	('^index/$',index ), 
	('^detail/$', detail), 
	#r的意义在于\不需要作为转义字符
	('^detail/plus/(\d{1,2})/$', hours_ahead),
	('^template/$', template),
	('^home/$', home),
	('^admin/',include(admin.site.urls)),
	('^search/$', search),
	('^contact/$', contact),
)
