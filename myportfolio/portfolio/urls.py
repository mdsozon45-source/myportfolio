from  django.urls import include, path
from django.conf.urls import include, url

from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	#path('about/', views.AboutView.as_view(), name='about'),
]