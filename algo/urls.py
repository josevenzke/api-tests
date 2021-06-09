from django.urls import path
from algo import views

urlpatterns = [
    path('binary-search/', views.binary_search, name='binary-search'),
    path('quicksort-sort/',views.quicksort_sort, name='quicksort'),

]