from django.urls import path
from . import views 

urlpatterns = [
    path('', views.userhome, name='users-userhome'),
    path('new/', views.new, name='users-new'),
    path('all/', views.all, name='users-all'),
    path('home/', views.home, name='users-home'),
    path('logout/', views.logout, name='users-logout'),
    path('approve/', views.approve, name='users-approve'),
    path('deny/', views.deny, name='users-deny'),
    path('signup/', views.signup, name='users-signup'),
    path('postsignup/', views.postsignup, name='users-postsignup'),
    path('postsignin/', views.postsignin, name='users-postsignin'),
    path('signin', views.signin, name='users-signin'),
    path('about', views.about, name='users-about'),
]