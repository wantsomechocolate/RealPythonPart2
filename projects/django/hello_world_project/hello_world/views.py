from django.shortcuts import render
from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('<html><body>Hello, World!</body></html>')

def about(request):
	return HttpResponse('And that triggers an ice bucket challeeeeeeeeeeeeenge')

def better(request):
	t=loader.get_template('betterhello.html')
	c=Context({'current_time': datetime.now(),})
	return HttpResponse(t.render(c))
