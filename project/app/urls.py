
from django.urls import path 
from .views import *

urlpatterns = [
    # path("home/",home,name='home')
    # path('home/<int:pk>',home,name="home"),
    # path('home/<str:name>',home,name="home"),
    # path('home/<slug:id>',home,name="home"),

    path('combination/<int:pk>/<str:name>/<slug:id>',combination)
   

]