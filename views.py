from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
import datetime

def hello(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
	#return HttpResponse("Hello world")
	
def exercise1(request):
	values = request.META.items()
	values.sort()
	#html = []
	#for k, v in values:
	#	html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return render_to_response('pageinfo.html', {'httpvalues': values})

def my_page(request):
	td = datetime.datetime.now()
	#html = "<html><body>Time is now %s </body></html>" %(td)
	#return HttpResponse(html)
	return render_to_response('mypage.html', {'c_date': td, 'title': "Test Page"})

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	return render_to_response('plus_datetime.html', {'hour_offset': offset, 'next_time': dt})
	#html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset, dt)
	#return HttpResponse(html)
	

