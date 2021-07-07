from django.urls import path
from .views import Zdjecia, CreatePostView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name= 'photo'
urlpatterns = [
    path('',Zdjecia.as_view(),name='photo'),
    path('post/', CreatePostView.as_view(), name='add_post'),
]
urlpatterns += staticfiles_urlpatterns()