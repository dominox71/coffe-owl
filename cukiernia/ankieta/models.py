import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Pytanie(models.Model):
    tekst_pytania=models.CharField(max_length=300)
    data_publikacji=models.DateTimeField()
    
    def byl_publikowany_ostatnio(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data_publikacji <= now
    byl_publikowany_ostatnio.admin_order_field ='data_publikacji'
    byl_publikowany_ostatnio.boolean =True
    byl_publikowany_ostatnio.short_description ="Publikowany ostatnio?"
    
    def __str__(self):
        return self.tekst_pytania
    
    class Meta:
        verbose_name="Pytanie"
        verbose_name_plural="Pytania"

class Wybor(models.Model):
    pytanie = models.ForeignKey(Pytanie,on_delete=models.CASCADE)
    tekst_odpowiedzi=models.CharField(max_length=300)
    glosy=models.IntegerField(default=0)

    def __str__(self):
        return self.tekst_odpowiedzi
    
    class Meta:
        verbose_name="Wybór"
        verbose_name_plural="Wybory"