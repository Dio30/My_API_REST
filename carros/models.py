from email.policy import default
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

turbo = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

carros_choice = (
    ('Citroen', 'Citroen'),
    ('Chevrolet', 'Chevrolet'),
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Ford', 'Ford'),
    ('Hyundai', 'Hyundai'),
    ('Jeep', 'Jeep'),
    ('Mercedes Benz', 'Mercedes Benz'),
    ('Peugeot', 'Peugeot'),
    ('Outros', 'Outros'),
    ('Renault', 'Renault'),
    ('Toyota', 'Toyota'),
    ('Volkswagen', 'Volkswagen'),
)

motor_carros = (
    ('1.0', '1.0'),
    ('1.4', '1.4'),
    ('1.6', '1.6'),
    ('1.8', '1.8'),
    ('2.0', '2.0'),
    ('2.4', '2.4'),
    ('2.8', '2.8'),
    ('3.2', '3.2'),
    ('4.0', '4.0'),
)

ano_fabricacao = (
    ('Não sabe informar o ano de fabricação', 'Não sabe informar o ano de fabricação'),
    ('2022', '2022'),
    ('2021', '2021'),
    ('2020', '2020'),
    ('2019', '2019'),
    ('2018', '2018'),
    ('2017', '2017'),
    ('2016', '2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004', '2004'),
    ('2003', '2003'),
    ('2002', '2002'),
    ('2001', '2001'),
    ('2000', '2000'),
    ('1999', '1999'),
    ('1998', '1998'),
    ('1997', '1997'),
    ('1996', '1996'),
    ('1995', '1995'),
    ('1994', '1994'),
    ('1993', '1993'),
    ('1992', '1992'),
    ('1991', '1991'),
    ('1990', '1990'),
)

ano_modelo = (
    ('Não sabe informar o ano do modelo', 'Não sabe informar o ano do modelo'),
    ('2023', '2023'),
    ('2022', '2022'),
    ('2021', '2021'),
    ('2020', '2020'),
    ('2019', '2019'),
    ('2018', '2018'),
    ('2017', '2017'),
    ('2016', '2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004', '2004'),
    ('2003', '2003'),
    ('2002', '2002'),
    ('2001', '2001'),
    ('2000', '2000'),
    ('1999', '1999'),
    ('1998', '1998'),
    ('1997', '1997'),
    ('1996', '1996'),
    ('1995', '1995'),
    ('1994', '1994'),
    ('1993', '1993'),
    ('1992', '1992'),
    ('1991', '1991'),
    ('1990', '1990'),
)

class Carros(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do Carro', unique=True)
    modelo = models.CharField(max_length=200, verbose_name='Modelo do Carro', choices=carros_choice, default='Outros')
    ano_de_fabricacao = models.CharField(max_length=200, verbose_name='Ano de Fabricação', choices=ano_fabricacao, default='Não sabe informar o ano de fabricação')
    ano_do_modelo = models.CharField(max_length=200, verbose_name='Ano do Modelo', choices=ano_modelo, default='Não sabe informar o ano do modelo')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    motor = models.CharField(max_length=200, choices=motor_carros)
    motorizacao = models.CharField(max_length=200, choices=turbo, default='Não', verbose_name='Turbo')
    chegou_loja = models.DateField(verbose_name='Quando chegou na loja')
    saiu_loja = models.DateField(verbose_name='Quando foi vendido', null=True, blank=True)
    ativo = models.BooleanField(default=True, verbose_name='Tem em estoque?')
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