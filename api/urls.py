from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('listAllBlogs/', listAllBlogs, name='listAllBlogs'),
    path('listThreeBlogs/', listThreeBlogs, name='listThreeBlogs'),
    path('getBlog/<int:blogID>', getBlog, name='getBlog'),
    path('searchBlogs/<str:searchQuery>', searchBlogs, name='searchBlogs'),
]