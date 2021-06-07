from modifystr.serializers import ModifySerializer
from django.urls import path
from modifystr import views

urlpatterns = [
    path('', views.ModifyUrls, name='modify-urls'),
    path('string-list/', views.StringList, name='string-list'),
    path('string-reverse/', views.StringReverse, name='string-reverse'),
    path('string-randomize/', views.StringRandomize, name='string-randomize'),
    path('string-space/', views.StringSpace, name='string-space'),

]   