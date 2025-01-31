from django.core.validators import ValidationError

def validar_preco_positivo(valor):
  if valor <= 0:
    raise ValidationError('O preço deve ser maior que zero')