from urllib.request import Request
from rest_framework import viewsets
from django.shortcuts import render
from .models import Carros
from .serializer import CarrosSerializer
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
        ano_de_modelo = resposta['ano_do_modelo']
        valor = resposta['valor']
        motor = resposta['motor']
        motorizacao = resposta['motorizacao']
        chegou_loja = resposta['chegou_loja']
        saiu_loja = resposta['saiu_loja']
        ativo = resposta['ativo']
        context = {
            'id_unico': id_unico,
            'nome': nome,
            'modelo': modelo,
            'ano_de_fabricacao': ano_de_fabricacao,
            'ano_de_modelo': ano_de_modelo,
            'valor': valor,
            'motor': motor,
            'motorizacao': motorizacao,
            'chegou_loja': chegou_loja,
            'saiu_loja': saiu_loja,
            'ativo': ativo,
        }
        return render(request,'carros/carros_list.html', context)
    
    except:
        return render(request,'carros/carros_list.html')