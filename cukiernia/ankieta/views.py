from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Pytanie, Wybor
# Create your views here.

class IndexView(generic.ListView):
    template_name='ankieta/index.html'
    context_object_name= 'lista_pytan'
    queryset = Pytanie.objects.filter(data_publikacji__lte=timezone.now()).order_by('-data_publikacji')[:5]

class DetaleView(generic.DetailView):
    model = Pytanie
    template_name = 'ankieta/detale.html'

class WynikiView(generic.DetailView):
    model = Pytanie
    template_name = 'ankieta/wyniki.html'
    
""" def detale(request, pytanie_id):
    try:
        pytanie = Pytanie.objects.get(pk = pytanie_id)
    except Pytanie.DoesNotExist:
        raise Http404('Nie ma takiego pytania!!!')
    return render(request,'ankieta/detale.html',{'pytanie':pytanie}) """



def glosuj(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie,pk=pytanie_id)
    try:
        wybrany=pytanie.wybor_set.get(pk=request.POST['wybor'])
    except (KeyError, Wybor.DoesNotExist):
        return render(request, 'ankieta/detale.html', {
            'pytanie':pytanie, 'error_message': "Nie wybrałeś pola wyboru!!!"
        })
    else:
        wybrany.glosy +=1
        wybrany.save()
        return HttpResponseRedirect(reverse('ankieta:wyniki',args=(pytanie.id,)))
