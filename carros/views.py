from rest_framework import viewsets
from django.shortcuts import render
from .models import Carros
from .serializer import CarrosSerializer
from django.contrib import messages
import requests

class CarrosViewSet(viewsets.ModelViewSet):
    """
    API para fazer um CRUD completo de carros simulando uma conssessionária.
    """
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer

def list_carros(request):
    pesquisar = request.GET.get("id")
    try:
        link = requests.get(f'http://127.0.0.1:8000/api/v1/carros/{pesquisar}')
        resposta = link.json()
        id_unico = resposta['id']
        nome = resposta['nome']
        modelo = resposta['modelo']
        ano_de_fabricacao = resposta['ano_de_fabricacao']
        ano_do_modelo = resposta['ano_do_modelo']
        valor = resposta['valor']
        motor = resposta['motor']
        motorizacao = resposta['motorizacao']
        chegou_loja = resposta['chegou_loja']
        saiu_loja = resposta['saiu_loja']
        estoque = resposta['estoque']
        context = {
            'id_unico': id_unico,
            'nome': nome,
            'modelo': modelo,
            'ano_de_fabricacao': ano_de_fabricacao,
            'ano_do_modelo': ano_do_modelo,
            'valor': valor,
            'motor': motor,
            'motorizacao': motorizacao,
            'chegou_loja': chegou_loja,
            'saiu_loja': saiu_loja,
            'estoque': estoque,
        }
        
        return render(request,'carros/carros_list.html', context)
    
    except:
        return render(request,'carros/carros_list.html')
    
def post_carros(request):
    link = 'http://127.0.0.1:8000/api/v1/carros/'
    header = {'Authorization': 'Token 8d2d9c4b689423f30f0745f08e68e0096983bf2a'}
    nome = request.POST.get("nome")
    modelo = request.POST.get("modelo")
    ano_de_fabricacao = request.POST.get("ano_de_fabricacao")
    ano_do_modelo = request.POST.get("ano_do_modelo")
    valor = request.POST.get("valor")
    motor = request.POST.get("motor")
    motorizacao = request.POST.get("motorizacao")
    chegou_loja = request.POST.get("chegou_loja")
    saiu_loja = request.POST.get("saiu_loja")
    estoque = request.POST.get("estoque")
    texto = {
        'nome': nome,
        'modelo': modelo,
        'ano_de_fabricacao': ano_de_fabricacao,
        'ano_do_modelo': ano_do_modelo,
        'valor': valor,
        'motor': motor,
        'motorizacao': motorizacao,
        'chegou_loja': chegou_loja,
        'saiu_loja': saiu_loja,
        'estoque': estoque,
    }
    
    if request.method == 'GET':
        return render(request,'carros/carro_form.html')
    
    elif request.method == 'POST':
        site = requests.post(url=link, headers=header, data=texto)
        resposta = site.json()
        messages.success(request, 'Dados inseridos com sucesso')
        return render(request,'carros/carro_form.html', resposta)

    messages.error(request, 'Algum dado foi prenchido incorretamente')
    return render(request,'carros/carro_form.html')

def editar_carro(request):
    pass