from django.conf import settings
from django.urls import path ,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog ),
    path('<int:blog_id>/', views.detail, name = 'detail' ),

]