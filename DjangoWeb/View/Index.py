from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
from DjangoWeb.Library.models import Book
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from DjangoWeb.Form.Contact import ContactForm


import datetime

# coding=utf-8

#第一个参数就是django.http.HttpRequest的实例request
def index(request):
	v_path = request.path
	v_host = request.get_host()
	v_url =  request.get_full_path()
	v_https = request.is_secure()
	meta_list =request.META.items()
	
	return render_to_response("Login.html",locals())

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


@csrf_protect 
def search(request):
	if  'query' in request.GET and  request.GET['query']:  
		queryText = request.GET['query']
		books = Book.objects.filter(title=queryText)

	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			subject_v = request.POST['subject']
			email_v = request.POST['email']
			message_v = request.POST['message']
			return render_to_response('Search.html',locals(),context_instance=RequestContext(request))
						
	return render_to_response('Search.html',locals(),context_instance=RequestContext(request))

@csrf_protect
def contact(request):
	if request.method == 'POST':
		method_v = "POST"
		#通过我们自定义的FORM类去生成
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject_v = cd['subject']
			email_v = cd['email']
			message_v = cd['message'] + 'Mark'
			return render_to_response('ContactForm.html',locals(),context_instance=RequestContext(request))
	else:
		#pass
		method_v = "GET"
		form = ContactForm(initial={'subject': 'I love your site!'})
		return render_to_response('ContactForm.html',locals(),context_instance=RequestContext(request))
	method_v = "GET2"
	return render_to_response('ContactForm.html',locals(),context_instance=RequestContext(request))
	#return HttpResponse('msg.html')
