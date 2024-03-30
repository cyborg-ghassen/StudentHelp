from django.urls import path

from post.views import PostCreateView

app_name = 'post'

urlpatterns = [
    path("new/", PostCreateView.as_view(), name="add_post")
]
