from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/createpost/', views.createpost, name='createpost'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('update/<int:post_id>/', views.update, name='update'),
    path('update/<int:post_id>/updatepost/', views.updatepost, name='updatepost'),
]