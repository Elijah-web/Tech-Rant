from django.urls import path
from .views import HomeView, detailview, commentview, aboutmeview

app_name = "blog"
#url patterns for the blog application
urlpatterns = [
	path("",HomeView.as_view(),name="blog_home"),
	path("detail/<int:post_id>/",detailview,name="post_detail"),
	path("detail/<int:post_id>/comment/>", commentview, name="comment"),
	path("elijah/",aboutmeview,name="aboutme"),
]