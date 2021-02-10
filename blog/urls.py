from django.urls import path
from .views import HomeView, DetailView

app_name = "blog"
#url patterns for the blog application
urlpatterns = [
	path("",HomeView.as_view(),name="blog_home"),
	path("detail/<int:pk>/",DetailView.as_view(),name="post_detail"),
]