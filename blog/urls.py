from django.urls import path
from .views import homeview, detailview, commentview, aboutmeview,postcreateview, AllPostsView, draftview, reviewview

app_name = "blog"
#url patterns for the blog application
urlpatterns = [
	path("",homeview,name="blog_home"),
	path("detail/<int:post_id>/",detailview,name="post_detail"),
	path("detail/<int:post_id>/comment/>", commentview, name="comment"),
	path("elijah/",aboutmeview,name="aboutme"),
	path("post_create",postcreateview,name="create"),
	path("all/",AllPostsView.as_view(),name="all"),
	path("draft/<int:post_id>/",draftview,name="draft"),
	path("review/",reviewview,name="review")
]