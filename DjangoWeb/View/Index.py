from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

#第一个参数就是django.http.HttpRequest的实例request
def index(request):
	return HttpResponse("<html><body><h1>Welcome to the Django world</h1><br/></body></html>")

def detail(request):
	now = datetime.datetime.now()
	html = ("<html><body><h1>It is now</h1><br/> %s.</body></html>"%now)
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	#assert False
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def template(request):
	#now = datetime.datetime.now()
	#t = get_template('Index.html')
	#html = t.render(Context({'ship_date':now}))
	#与模版中的变量名字相统一，利用locals()函数
	ship_date = datetime.datetime.now()
	#最为捷径的方法
	return render_to_response('Index.html', locals())
	#return render_to_response('Index.html', {'ship_date': now})
	#return HttpResponse(html)

def home(request):
	current_date = datetime.datetime.now()
	return render_to_response('Home.html', locals())
