from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupUser, name="signup"),
    path('addTask/', views.addTask, name='addTask'),
    # path('todo/', views.todo, name='todo'),
    path('inprogress/', views.inprogress, name='inprogress'),
    path('task/inprogress/<int:task_id>/', views.change_p, name='change_p'),
    path('completed/', views.completed, name='completed'),
    path('task/completed/<int:task_id>/', views.changeto_completed, name='changeto_completed'),
    path('deleted/', views.deleted, name='deleted'),
    path('task/deleted/<int:task_id>/', views.changeto_deleted, name='changeto_deleted'),

]