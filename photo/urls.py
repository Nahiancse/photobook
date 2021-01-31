
from django.urls import path
from photo import views

urlpatterns = [
    path('',views.index),
    path('load_form',views.load_form),
    path('add_item', views.additem),

    # for editing
    path('editPhoto/<int:id>', views.editPhoto),
    path('updatePhoto/<int:id>', views.updatePhoto),

    # for deleting
    path('deletePhoto/<int:id>', views.deletePhoto),

]
