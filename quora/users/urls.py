from django.urls import path
from . import views
from .views import user_list,user_form, user_delete

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('users/', user_list, name='user-list'),
    path('users/add/', user_form, name='user-add'),
    path('users/edit/<int:id>/', user_form, name='user-edit'),
    path('users/delete/<int:id>/', user_delete, name='user-delete'),
]
