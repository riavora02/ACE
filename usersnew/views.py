from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas
import ast 

# Use a service account
cred = credentials.Certificate('aceseniorproject-a4727-firebase-adminsdk-wfz5j-6382966246.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
# Create your views here.

config = {
	'apiKey': "AIzaSyAdvU-RuyH54gMBS7fBVsd_bGeW0csYn30",
	'authDomain': "aceseniorproject-a4727.firebaseapp.com",
	'databaseURL': "https://aceseniorproject-a4727.firebaseio.com",
	'projectId': "aceseniorproject-a4727",
	'storageBucket': "aceseniorproject-a4727.appspot.com",
	'messagingSenderId': "251073104111",
	'appId': "1:251073104111:web:231df9085c8237e02eb31a",
	'measurementId': "G-WX7KRG41WW",
  };

firebase = pyrebase.initialize_app(config)
authorization = firebase.auth();

def signin(request):
	return render(request, 'usersnew/signin.html')

def home(request):
	email = request.POST.get('email')
	passw = request.POST.get("password")

	try:
		user = authorization.sign_in_with_email_and_password(email, passw)

	except: 
		message = "Invalid Credentials"
		return render(request, 'usersnew/signin.html', {"error": message})

	return render(request, 'usersnew/home.html', {"e": email})

def new(request):
	users = []
	newusers = db.collection(u'users').where('Status', '==', 'Pending').get()
	for newuser in newusers:
		hi = str(u'{}'.format(newuser.to_dict()))
		dictionary = ast.literal_eval(hi)
		users.append(dictionary)

	return render(request, 'usersnew/new.html', {"users": users} )

def all(request):
	users = []
	documents = db.collection(u'users').where('Status', '==', 'Approved').get()
	for document in documents:
		hi = str(u'{}'.format(document.to_dict()))
		dictionary = ast.literal_eval(hi)
		users.append(dictionary)

	return render(request, 'usersnew/all.html', {"users": users} )

def logout(request):
	auth.logout(request)
	return render(request, 'usersnew/signin.html')

def approve(request):

	name = str(request.POST.get("person"))

	approved = db.collection(u'users').document(name).update(
	{ u'Status': 'Approved' })

	users = []
	newusers = db.collection(u'users').where('Status', '==', 'Pending').get()
	for newuser in newusers:
		hi = str(u'{}'.format(newuser.to_dict()))
		dictionary = ast.literal_eval(hi)
		users.append(dictionary)

	return render(request, 'usersnew/new.html', {"users": users}) 

def deny(request):

	name = str(request.POST.get("person"))

	approved = db.collection(u'users').document(name).update(
	{ u'Status': 'Denied' })

	users = []
	newusers = db.collection(u'users').where('Status', '==', 'Pending').get()
	for newuser in newusers:
		hi = str(u'{}'.format(newuser.to_dict()))
		dictionary = ast.literal_eval(hi)
		users.append(dictionary)

	return render(request, 'usersnew/new.html', {"users": users}) 

def signup(request):
	return render(request, 'usersnew/signup.html')

def postsignup(request):
	name = request.POST.get('Name')
	make = request.POST.get('Make')
	license = request.POST.get('License')

	approved = db.collection(u'users').document(name).set(
	{ u'Name': name, 
	  u'Make': make,
	  u'License': license,
	  u'Status': "Pending"})

	return render(request, 'usersnew/signin.html')

