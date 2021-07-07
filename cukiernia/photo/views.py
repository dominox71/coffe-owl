from django.views.generic import ListView, CreateView
from .models import Photo
from django.urls import reverse_lazy

from .forms import PostForm

class Zdjecia(ListView):
    model = Photo
    template_name = 'zdjecia/photo.html'

class CreatePostView(CreateView):
    model = Photo
    form_class = PostForm
    template_name = 'zdjecia/post.html'
    success_url = reverse_lazy('photo:photo')