from django.urls import path
# from .views import home ,string,integer,path123,slug123
from .views import *



urlpatterns=[

path('home/',home, name='home'),
path('integer/<int:pk>',integer,name='integer'),
path('string/<str:pk>',string,name='string'),
path('slug123/<slug:pk>',slug123,name='slug123'),
path('path123/<path:pk>',path123,name='path123'),

path('combination/<path:pk>/<str:id>/<slug:pkid>/<int:idpk>',combination,name='combination')


]
