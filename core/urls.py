# core/urls.py

from django.urls import path
from . import views
from .api_views import ProjectListCreateAPI, TaskListCreateAPI


urlpatterns = [
    path('', views.home_redirect_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('projects/<int:project_id>/tasks/create/', views.task_create, name='task_create'),
    path('api/projects/', ProjectListCreateAPI.as_view(), name='api_projects'),
    path('api/tasks/', TaskListCreateAPI.as_view(), name='api_tasks')

]
