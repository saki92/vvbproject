from django.http import HttpResponse
from django.shortcuts import render_to_response
from vvb_db.models import Employee
import pprint

def home(request):
	return render_to_response('home.html')

def login(request):
	if request.GET.get('uname') and request.GET.get('pword'):
		uname = request.GET['uname']
		pword = request.GET['pword']
		details = Employee.objects.filter(uname=uname)
		if details[0].psw==pword:
			result="Login successed."
		else:
			result="Login failed."
	else:
		result="Enter both username and password."
	return render_to_response('login.html',{'result':result})
