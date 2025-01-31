from django.core.validators import ValidationError
import re

def validar_preco_positivo(valor):
  if valor <= 0:
    raise ValidationError('O preço deve ser maior que zero')
  
def quantidade_estoque_inteiro_positivo(valor):
  if not isinstance(valor, int): #isinstance permite vericar o tipo de dado do objeto, nesse caso se o valor é um inteiro
    raise ValidationError('A quantidade deve ser um número inteiro')
  if valor <= 0:
    raise ValidationError('A quantidade deve ser maior que zero')
  
def validar_codigo(valor):
  if not re.match(r'^[a-zA-Z0-9]+$', valor):
    raise ValidationError('O código deve conter apenas letras e números')