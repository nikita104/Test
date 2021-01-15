from django.conf.urls import url

from django.urls import path

from core import views

urlpatterns = (
    url(r'^$', views.Index.as_view(), name='index'),
    path('test_student', views.tests, name='tests'),
    # url(r'^$', views.tests, name='tests'),
    path('test_student/<int:id>/', views.test_student, name='test_student'),
)

