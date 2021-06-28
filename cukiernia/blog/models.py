from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')
     

class Post(models.Model):
    STATUS_CHICES = (('draft','Wersja robocza'),
                     ('published','Opublikowany'),
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHICES,default='draft')
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,
                                                self.publish.strftime('%m'),
                                                self.publish.strftime('%d'),
                                                self.slug])    
        
          
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posty"
        ordering =('-publish',)
    
    def __str__(self):
        return self.title        



class Comment(models.Model): 
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name=models.CharField(max_length=80)
    email = models. EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name="Komentarz"
        verbose_name_plural="Komentarze"
        ordering =('created',)
    
    def __str__(self):
        return f'Komentarz dodany przez {self.name} do posta {self.post}'    