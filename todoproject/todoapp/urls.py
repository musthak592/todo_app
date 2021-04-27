from django.contrib import admin
from django.urls import path,include
from todoapp import views

urlpatterns = [
      path('',views.demo,name='demo'),
      path('delete/<int:id>/',views.delete,name='delete'),
      path('update/<int:id>/',views.update,name='update'),
      # path('csvtask/', views.Tasklistview.as_view(),name='csvtask'),
      # path('csvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='csvdetail'),
      # path('csvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='csvupdate'),
      # path('csvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='csvdelete'),

]