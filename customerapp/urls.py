from django.urls import path

from customerapp.views.fileviewer import fileupload
from customerapp.views.homepageview import homepageview
from customerapp.views.login import Login, logout
from customerapp.views.signup import Signup

urlpatterns = [
    path('', homepageview, name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('uploadfile', fileupload, name='uploadfile'),

]