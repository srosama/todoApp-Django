from django.urls import path
from .views import *
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('todo/', MainToDoList.as_view(), name='main-list'),
    path('todo/delete-row/<pk>', DeleteRow.as_view(), name='delete-row'),
    path('todo/update-row/<pk>', UpdateRow.as_view(), name='update-row'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
