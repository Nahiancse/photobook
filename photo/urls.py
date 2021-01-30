
from django.urls import path
from photo import views

urlpatterns = [
    path('',views.index),
    path('load_form',views.load_form),
    path('add_item', views.additem),

]
