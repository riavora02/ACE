from django.urls import path
from . import views 

urlpatterns = [
    path('', views.signin, name='users-signin'),
    path('new/', views.new, name='users-new'),
    path('all/', views.all, name='users-all'),
    path('home/', views.home, name='users-home'),
    path('logout/', views.logout, name='users-logout'),
    path('approve/', views.approve, name='users-approve'),
    path('deny/', views.deny, name='users-deny'),
    path('signup/', views.signup, name='users-signup'),
    path('postsignup/', views.postsignup, name='users-postsignup')
]