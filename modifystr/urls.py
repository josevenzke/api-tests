from django.urls import path
from modifystr import views

urlpatterns = [
    path('string-list/', views.StringList, name='string-list'),
    path('string-reverse/', views.StringReverse, name='string-reverse')
]