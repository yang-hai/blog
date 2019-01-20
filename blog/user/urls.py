from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('article_list/', views.article_list, name='article_list'),
    path('info/<int:id>/', views.info, name='info'),
    path('logout/', views.logout, name='logout'),
    path('category/', views.category, name='category')
]