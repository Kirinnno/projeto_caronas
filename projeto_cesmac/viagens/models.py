from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    TIPO_USUARIO_CHOICES = [
        ('motorista', 'Motorista'),
        ('passageiro', 'Passageiro'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f'{self.nome} {self.sobrenome} ({self.get_tipo_usuario_display()})'


class Viagem(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    horario = models.DateTimeField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    vagas = models.IntegerField()
    motorista = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.origem} -> {self.destino} ({self.horario})'
