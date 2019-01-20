from django.urls import path

from acticle import views

urlpatterns = [
    path('register0000/', views.register, name='register0000'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_acticle/', views.add_acticle, name='add_acticle'),
    path('add_category/', views.add_category, name='add_category'),
    path('del_category/<int:id>/', views.del_category, name='del_category'),
    path('update_category/<int:id>/', views.update_category, name='update_category'),
    path('article/', views.article, name='article'),
    path('update_article/<int:id>/', views.update_article, name='update_article'),
    path('del_article/<int:id>/', views.del_article, name='del_article'),
]