from django.urls import path
from . import views
app_name = "glowna"
urlpatterns = [
    path('', views.glowna, name="glowna"),
]