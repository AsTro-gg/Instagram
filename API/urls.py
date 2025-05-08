from tkinter.font import names

from django.urls import path
from API.views import *
urlpatterns =[
    path('register/',RegisterUser.as_view(),name='register'),
    path('login/',loginview,name='login'),

    #Story
    path('story/',StoryAPIview.as_view(),name='Story'),
    path('story/<int:pk>/',StoryDynamicAPIview.as_view(),name='Storydetail'),

    #Post
    path('post/',PostAPIview.as_view(),name ='Post'),
    path('post/<int:pk>/',PostDynamicAPIview.as_view(),name='Postdetail')


]