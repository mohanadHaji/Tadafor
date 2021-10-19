from django.urls import path
from . import views

urlpatterns = [
    path('index.html/', views.index),
    path('', views.index),
    path('staff.html/',views.staff),
    path('psych.html/', views.psych),
    path('rights.html/', views.rights),
    path('feed.html/', views.feed),
    path('callus.html/', views.callus),
    path('others.html/', views.others),
    path('register.html/', views.register),
    path('psych.html/<int:id>/', views.psych,name="newUser"),
    path('rights.html/<int:id>/', views.rights),
    path('feed.html/<int:id>/', views.feed),
]