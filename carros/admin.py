from django.contrib import admin
from .models import Carros

class CarrosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modelo', 'ano_de_fabricacao', 'ano_do_modelo', 
        'valor', 'motor', 'motorizacao', 'chegou_loja', 'saiu_loja', 'estoque', 'usuario')

admin.site.register(Carros, CarrosAdmin)