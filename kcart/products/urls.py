from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('list_product',views.list_product,name="product_list"),
    path('single_product',views.single_product,name="single_product"),
]