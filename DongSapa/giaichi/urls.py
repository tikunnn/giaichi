from django.urls import include, path
from . import views

urlpatterns = [
    path("giaichi/create", views.GiaiChiCreateView.as_view(), name="giaichi_create"),
    path(
        "giaichi/update/<int:pk>/",
        views.GiaichiUpdateView.as_view(),
        name="giaichi_update",
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]
