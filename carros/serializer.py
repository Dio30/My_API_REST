from rest_framework import serializers
from .models import Carros

class CarrosSerializer(serializers.ModelSerializer):
    chegou_loja = serializers.DateField(format='%d/%m/%Y')
    saiu_loja = serializers.DateField(format='%d/%m/%Y')
    class Meta:
        model = Carros
        fields = (
        'id', 'nome', 'modelo', 'ano_de_fabricacao', 'ano_do_modelo', 
        'valor', 'motor', 'motorizacao', 'chegou_loja', 'saiu_loja', 'estoque'
        )