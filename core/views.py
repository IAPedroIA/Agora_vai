from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404  #
from django.template import loader
from django.http.response import  HttpResponse

# Create your views here.

def index(request):
    produtos_dict = Produto.objects.all()

    context = {
        'curso': 'Programação_Web',
        'Produtos': produtos_dict
    }

    return render(request, "index.html", context)


def contato(request):
    return render(request,"contato.html")

def produto(request,pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto,id=pk)
    context = {'produto':prod}
    return render(request,"produto.html",context)


def error404(request,ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),content_type='text/thml; charset=utf-8',status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),content_type='text/thml; charset=utf-8',status=500)