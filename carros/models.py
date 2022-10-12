from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Carros(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do Carro', unique=True)
    modelo = models.CharField(max_length=200, verbose_name='Modelo do Carro', default='Não sabe informar')
    ano_de_fabricacao = models.IntegerField(verbose_name='Ano de Fabricação')
    ano_do_modelo = models.IntegerField(verbose_name='Ano do Modelo')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    motor = models.DecimalField(max_digits=2, decimal_places=1)
    motorizacao = models.CharField(max_length=3, default='Não', verbose_name='Turbo')
    chegou_loja = models.DateField(verbose_name='Quando chegou na loja')
    saiu_loja = models.DateField(verbose_name='Quando foi vendido')
    estoque = models.CharField(max_length=200, default='Sim', verbose_name='Tem em estoque?')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['id']
        
    def __str__(self):
        return self.nome
        

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)