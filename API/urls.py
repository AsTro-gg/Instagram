from tkinter.font import names

from django.urls import path
from API.views import *
urlpatterns =[
    path('register/',RegisterUser.as_view(),name='register'),
    path('login/',loginview,name='login'),

    #Story
    path('story/',StoryAPIview.as_view(),name='Story'),

]