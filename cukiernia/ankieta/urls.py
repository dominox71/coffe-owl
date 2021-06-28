from django.urls import path

from . import views
app_name='ankieta'
urlpatterns =[
    path('',views.IndexView.as_view(), name='index'),
     # ex: /ankieta/5/detale
    path('detale/<int:pk>',views.DetaleView.as_view(), name='detale'),
    # ex: /ankieta/5/wyniki/
    path('<int:pk>/wyniki',views.WynikiView.as_view(), name='wyniki'),
    # ex: /ankieta/5/glosuj/
    path('<int:pytanie_id>/glosuj',views.glosuj, name='glosuj'),
]