from django.db import models

# Create your models here.

class Produto(models.Model): # herda de models
    nome = models.CharField('Nome',max_length=100) # Definimos que é um caractere e o maximo é 100
    preco = models.DecimalField('Preço',decimal_places=2,max_digits=8) # Definimos que é um valor decimal
    estoque = models.IntegerField('Quantidade em Estoque') # Definimos que é um inteiro

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField("Nome",max_length=100)
    sobre_nome = models.CharField("Sobrenome",max_length=100) # Entrada e E-mail
    email = models.EmailField("Email",max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobre_nome}'
