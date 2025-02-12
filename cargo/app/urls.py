from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    path('add_car',views.add_car),
    path('edit_car/<id>',views.edit_car),
    # path('delete_car/<id>',views.delete_car),

    path('register',views.register),
    
    
]