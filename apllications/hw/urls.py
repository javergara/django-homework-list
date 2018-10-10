from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homeworks_list, name='index'),
    url(r'^new/', views.new_task, name='new_task'),
]