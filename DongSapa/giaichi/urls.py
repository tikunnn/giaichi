from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.giaichi_form, name='giaichi_form'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
