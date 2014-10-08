from django.http import *
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
import myapp
from myapp.forms import *
from django.contrib import auth
from django.forms.util import ErrorList
from random import choice
from django.db.models import Q
import datetime
from django.utils.timezone import utc
from django import forms
from django.template import RequestContext
from myapp.forms import UserForm, UserProfileForm
import sys
import os
from django.conf import settings
sys.path.insert(0, '/home/shekhark/project/cs654/myapp/beautifulsoup/')
sys.path.insert(0, '/home/shekhark/project/cs654/menu/')
from py_curl import *
from sms import *
from getdatabypnr import *
from processorder import *
import codecs
from twilio.rest import TwilioRestClient
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rail Tadka account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)


def train(request):
    if 'train_number' in request.POST and not request.POST['train_number'] == '':
        a = request.POST['train_number']
        date = request.POST['date']
        message = 'You searched for: %r' % request.POST['train_number']
	temp,code_list=route(a,date)
	fi=open((os.path.join(settings.MEDIA_ROOT, 'stationlist')), 'r').read()
#	f=fi.read()
	f = fi
	#fi.close()
	f=f.split("\n")
	code_list2=[]
	temp2=[]
	for index3,j in enumerate(code_list):
		for index2,i in enumerate(f):
			if index2!=len(f)-1:
				tempo=i.split(',')
				code=tempo[1]
				code=code.upper()
				if code==j:
					code_list2.append(code)
					temp2.append(temp[index3])
				
        our_list = zip(temp,code_list)
        our_list2 = zip(temp2,code_list2)
#        context = {'b': temp}
        return render(request,'response.html',{'our_list' : our_list, 'our_list2' : our_list2})
        #return HttpResponse('a')
    elif 'pnr' in request.POST:
        pnr = request.POST['pnr']
        train_no = getdatabypnr(pnr)
        temp,code_list=route2(train_no)
	fi=open((os.path.join(settings.MEDIA_ROOT, 'stationlist')), 'r').read()
#	f=fi.read()
	f = fi
	#fi.close()
	f=f.split("\n")
	code_list2=[]
	temp2=[]
	for index3,j in enumerate(code_list):
		for index2,i in enumerate(f):
			if index2!=len(f)-1:
				tempo=i.split(',')
				code=tempo[1]
				code=code.upper()
				if code==j:
					code_list2.append(code)
					temp2.append(temp[index3])
				
        our_list = zip(temp,code_list)
        our_list2 = zip(temp2,code_list2)
#        context = {'b': temp}
        return render(request,'response.html',{'our_list' : our_list, 'our_list2' : our_list2})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

def order(request):
   if 'station_selection' in request.POST:
        a = request.POST['station_selection']
        message = 'You searched for: %r' % a
	status,nameofjoint,avgorder,minorder,jain,menu_list=menu_generate(a)
        return render(request,'order.html',{'status' : status, 'nameofjoint' : nameofjoint, 'avgorder' : avgorder, 'minorder' : minorder , 'jain' : jain , 'menu_list' : menu_list})
   elif 'time' in request.POST:
        status,nameofjoint,avgorder,minorder,jain,menu_list=menu_generate('ndls')
        return render(request,'order.html',{'status' : status, 'nameofjoint' : nameofjoint, 'avgorder' : avgorder, 'minorder' : minorder , 'jain' : jain , 'menu_list' : menu_list})
   else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
def final(request):
  if 'pnr' in request.POST:
      pnr = request.POST['pnr']
      name = request.POST['name']
      mobile = request.POST['mobile']
      commments = request.POST['comments']
      account_sid = "AC77709cad71509b163f6f3ec522c8c7da"
      auth_token = "c858b7751cc0d1260efbe9153ef5f8b4"
      client = TwilioRestClient(account_sid, auth_token)
# Make the call
      call = client.calls.create(to="919559753562", # Any phone number
      from_="7045869183", # Must be a valid Twilio number
      url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
      send_mail('Order Confirmation', 'Hi, your order at Rail Tadka has been placed successfully','arpitjain099@email.com', ['shekharkadyan@gmail.com'])
      placesms()
      return HttpResponse("order placed")
  else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

def confirm(request):
   if 'totalValue' in request.POST:
       a = request.POST['totalValue']
       return render(request,'confirm.html',{'total' : a})
   else:
       return HttpResponse("you submitted an empty form")


def homeview(request):
   return render(request, 'index.html')

#def login(request):
#    if(request.user.is_authenticated()):
#        return HttpResponseRedirect("/profile")
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
#        
#        if form.is_valid():
#            cd = form.cleaned_data
#            user = auth.authenticate(username=cd['username'],password=cd['password'])
#            if user is not None and user.is_active:
#                auth.login(request, user)
#                return HttpResponseRedirect("/profile")
#            else:
#                errors = form._errors.setdefault("__all__", ErrorList())
#                errors.append(u"wrong username or password")
#    else:
#        form = LoginForm()
#    return render_to_response('index.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

def home(request):
    return render(request, 'index.html')

#def login(request):
#    if request.method != 'POST':
#        raise Http404('Only POSTs are allowed')
#    try:
#        m = Member.objects.get(username=request.POST['username'])
#        if m.password == request.POST['password']:
#            request.session['member_id'] = m.id
#            return HttpResponseRedirect('/you-are-logged-in/')
#    except Member.DoesNotExist:
#        return HttpResponse("Your username and password didn't match.")

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/profile")
    else:
        # Show an error page
        return HttpResponseRedirect("/error")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/home/")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

# Create your views here.
