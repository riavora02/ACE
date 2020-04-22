from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas
import ast 

# Use a service account
cred = credentials.Certificate('ace-database-d7458-firebase-adminsdk-vdocy-211646616e.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
# Create your views here.

config = {
  "apiKey": "AIzaSyDiKcH45hbm6pZMMM7rae_pHupB4gzbsE4",
  "authDomain": "ace-database-d7458.firebaseapp.com",
  "databaseURL": "https://ace-database-d7458.firebaseio.com",
  "projectId": "ace-database-d7458",
  "storageBucket": "ace-database-d7458.appspot.com",
  "messagingSenderId": "359861837278",
  "appId": "1:359861837278:web:8013d78f77b42d48f3914f",
  "measurementId": "G-FY47QSVC83"
};

firebase = pyrebase.initialize_app(config)
authorization = firebase.auth();
	

def signin(request):
	return render(request, 'usersnew/signin.html')

def postsignin(request):
	email = request.POST.get('email')
	passw = request.POST.get("password")

	try:
		user = authorization.sign_in_with_email_and_password(email, passw)

	except: 
		#message = "Invalid Credentials"
		messages.success(request, "Invalid Credentials")
		return render(request, 'usersnew/signin.html')

	return render(request, 'usersnew/home.html', {"e": email})

def home(request):
	return render(request, 'usersnew/home.html')

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
	return render(request, 'usersnew/userhome.html')

def approve(request):

	license = str(request.POST.get("license"))

	approved = db.collection(u'users').document(license).update(
	{ u'Status': 'Approved' })

	users = []
	newusers = db.collection(u'users').where('Status', '==', 'Pending').get()
	for newuser in newusers:
		hi = str(u'{}'.format(newuser.to_dict()))
		dictionary = ast.literal_eval(hi)
		users.append(dictionary)

	return render(request, 'usersnew/new.html', {"users": users}) 

def deny(request):

	license = str(request.POST.get("license"))

	approved = db.collection(u'users').document(license).update(
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

	approved = db.collection(u'users').document(license).set(
	{ u'Name': name, 
	  u'Make': make,
	  u'License': license,
	  u'Status': "Pending"})

	messages.success(request, "Account has been created")

	return render(request, 'usersnew/signup.html')

def userhome(request):
	return render(request, 'usersnew/userhome.html')

def about(request):
	return render(request, 'usersnew/about.html')

def alarm(request):
	alarm = "alarm"
	return render(request, 'usersnew/home.html', {"alarm": alarm})

# Create a callback on_snapshot function to capture changes
#def on_snapshot(doc_snapshot, changes, read_time):
    #for doc in doc_snapshot:
        #print(u'Received document snapshot: {}'.format(doc.id))

#doc_ref = db.collection(u'users').document(u'LA')

# Watch the document
#doc_watch = doc_ref.on_snapshot(on_snapshot)

