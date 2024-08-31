from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'),    #bugrayilmaz.com/tweetapp/
    path('addtweet/',views.addtweet,name='addtweet'), #bugrayilmaz.com/tweetapp/addtweet
    path('addtweetbyform',views.addtweetbyform,name='addtweetbyform'),#bugrayilmaz.com/tweetapp/addtweetbyform
    path('addtweetbymodelform',views.addtweetbymodelform,name='addtweetbymodelform'),#bugrayilmaz.com/tweetapp/addtweetbymodelform
    path('signup/',views.SignUpView.as_view(),name='signup'),#bugrayilmaz.com
    path('deletetweet/<int:id>',views.deletetweet,name='deletetweet'),#bugrayilmaz.com
]
