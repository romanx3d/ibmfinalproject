from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarMake, CarModel
from .restapis import get_dealers_from_cf, get_dealer_reviews_from_cf,post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)
def login_page(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/login.html', context)

def signuppage(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/signup.html', context)

def signup(request):
    context = {}
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['userpassword']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']

        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        
        except:
            print("{} is new user".format(username))

        if user_exist is not True:
            user = User.objects.create_user(username=username, first_name=firstname,last_name=lastname,password=password)
            login(request, user)
            print ("Log in the user '{}'".format(request.user.username))
            return redirect('djangoapp:index')
        else:
             return render (request,'djangoapp/signup.html')

    else:
        return render (request,'djangoapp/signup.html')

def logout_request(request):
    context = {}
    print ("Log out the user '{}'".format(request.user.username))
    logout(request)
    return redirect('djangoapp:index')

def login_request(request):
    context = {}
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['userpassword']
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            print ("Log in the user '{}'".format(request.user.username))
            return redirect('djangoapp:index')
        else:
             return render (request,'djangoapp/login.html')

    else:
        return render (request,'djangoapp/login.html')

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/93f6f20e-a46d-4963-b799-ab699b88bd51/ibmfinal/dealership_all.json"
        # Get dealers from the URL
        context = get_dealers_from_cf(url)
       
      
       
        #context = {"data":[{"id":1,"name":"vasya"},{"id":2,"name":"banan"}]}
        

        return render(request, 'djangoapp/index.html', context)

def get_dealer_details(request, dealerid, dealername):
    if request.method=="GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/93f6f20e-a46d-4963-b799-ab699b88bd51/ibmfinal/db_retrieve.json"
        context = {}
        context= get_dealer_reviews_from_cf(url,**({"dealerid":dealerid}) )
        
        context["dealername"]=dealername
        context["dealerid"]=dealerid
        #dealer_reviews=' '.join([reviews.sentiment for reviews in dealer])

        return render(request, 'djangoapp/dealer_details.html', context)


def add_review(request, dealerid):
    if request.user.is_authenticated:
        if request.method == "POST":
            review = {}
            url = "https://us-south.functions.appdomain.cloud/api/v1/web/93f6f20e-a46d-4963-b799-ab699b88bd51/ibmfinal/db_post.json"
            json_payload = {}
            data = request.POST
            purchasedate=data.get("purchasedate")
            #print(purchasedate)
           # print(type(purchasedate))
            #datetime_obj=datetime.strptime(purchasedate, '%m/%d/%Y').date()
            #datetime_obj=datetime_obj.utcnow().isoformat()
            #print("THE DATE IS:")
            #print(datetime_obj)
            review["purchase_date"] =  purchasedate
            review["dealership"] = dealerid
            review["name"] = request.user.username
            review["review"] = data.get("content")
            carid=data.get("car")
            
            car=CarModel.objects.get(id=carid)
            cardate=car.year 
            print(cardate)
            review["car_make"]=car.make.name
            review["car_model"]=car.name
            review["car_year"]=cardate.strftime("%Y")
            if data.get("purchasecheck"):
                review["purchase"]=True 
            else:
                review["purchase"]=False
            json_payload["review"] = review
            response = post_request(url, json_payload)

            return redirect('djangoapp:index')

def add_review_page (request,dealername,dealerid): 
    context = {}
    allcars=CarModel.objects.all().filter(id=dealerid)

    context["cars"]=allcars
    context["dealername"] = dealername 
    context["dealerid"] = dealerid
    
    if request.method == "GET":
        return render(request, 'djangoapp/add_review.html', context)

        



        


