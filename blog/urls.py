from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="all"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("delete/<str:slug>", views.PostDeleteView.as_view(), name="post_delete"),
    path("update/<str:slug>", views.PostUpdateView.as_view(), name="post_update"),
    path("read/<str:slug>", views.PostDetailView.as_view(), name="post_detail"),
]