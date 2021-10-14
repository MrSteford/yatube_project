from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:list>/', views.posts, name='group')
]

#  path('', views.index, name='index'),
#     path('group/<slug:list>/', views.group_list, name = 'group_list'),
#     path('posts/<int:pk>/', views.group_posts_detail, name='groupposts_detail'),
# ] 