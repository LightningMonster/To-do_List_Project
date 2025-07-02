from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('tasks/', tasks_view, name='tasks'),
    path('expenses/', expenses_view, name='expenses'),
]
