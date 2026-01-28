from django.urls import path
from .import views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('mypost/', views.myPost, name='mypost'),
    path('newpost/', views.newPost, name='newpost'),
    path('signout/', views.signout, name='signout'),
]