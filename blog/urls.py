from django.urls import path
from .views import HomeView


#url patterns for the blog application
urlpatterns = [
	path("",HomeView.as_view(),name="blog_home"),
]