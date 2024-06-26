from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path('account',views.account,name="account"),
    path('signout',views.signout,name="signout")
    
]