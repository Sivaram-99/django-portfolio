
from django.urls import path
from django.conf.urls import include
from . import views
app_name='blog'
urlpatterns = [
    path('',views.home1,name='home1'),
    path('<int:blog_id>/', views.home2,name='home2'),
    ]