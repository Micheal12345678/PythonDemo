from django.conf.urls import patterns, include, url
#Index就是路由的名称，源自于什么文件
from DjangoWeb.View.Index import index,detail,hours_ahead,template,home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	#元组中第一个元素是模式匹配字符串（正则表达式）；
	#第二个元素是那个模式将使用的视图函数
	('^$',index ), 
	('^detail/$', detail), 
	#r的意义在于\不需要作为转义字符
	('^detail/plus/(\d{1,2})/$', hours_ahead),
	('^index/$', template),
	('^home/$', home),
)


# # 以下是URL的优化写法
# urlpatterns = patterns('mysite.views',
# 	(r'^hello/$', 'hello'),
# 	(r'^time/$', 'current_datetime'),
# 	(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
# )

# urlpatterns += patterns('weblog.views',
# 	(r'^tag/(\w+)/$', 'tag'),
# )

# #在调试的时候利用Debug信息
# if settings.DEBUG:
#	urlpatterns += patterns('',
#	(r'^debuginfo/$', views.debug),
#	)

#带有组名的参数，也就是说URL为
#可以增加其可读性，但是简洁性就大为降低了
#其调用相当于month_archive(request, year='2006', month='03')
# urlpatterns = patterns('',
# 	(r'^articles/(?P<year>\d{4})/$', views.year_archive),
# 	(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive),
# )

#如果两个视图,逻辑基本上一样，但是视图不一样
#可以设置第三个参数：Template
# urlpatterns = patterns('',
# 	(r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
# 	(r'^bar/$', views.foobar_view, {'template_name': 'template2.html'}),
# )
#在View层中这样去写代码
# from django.shortcuts import render_to_response
# from mysite.models import MyModel
# def foobar_view(request, template_name):
# 	m_list = MyModel.objects.filter(is_new=True)
# 	return render_to_response(template_name, {'m_list': m_list})

#伪造捕捉到的URLconf值
#共用一个视图，但是URL有所变化，但是引用的内容是一样的
# urlpatterns = patterns('',
# 	(r'^mydata/birthday/$', views.my_view, {'month': 'jan', 'day': '06'}),
# 	(r'^mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', views.my_view),
# )


# #也可以用include()
# # urls.py
# from django.conf.urls.defaults import *
# urlpatterns = patterns('',
#     (r'^blog/', include('inner'), {'blogid': 3}),
# )
# # inner.py
# from django.conf.urls.defaults import *
# urlpatterns = patterns('',
#     (r'^archive/$', 'mysite.views.archive'),
#     (r'^about/$', 'mysite.views.about'),
#     (r'^rss/$', 'mysite.views.rss'),
# )



