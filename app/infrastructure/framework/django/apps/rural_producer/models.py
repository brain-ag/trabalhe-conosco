from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class RuralProducer(models.Model):
    documento_tipo = models.CharField(max_length=4)
    documento_numero = models.CharField(max_length=14, unique=True)
    nome_produtor = models.CharField(max_length=100)
    nome_fazenda = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    area_total_hectares = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    area_agricultavel_hectares = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    area_vegetacao_hectares = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    culturas_plantadas = models.CharField(max_length=20)

    class Meta:
        ordering = ('id',)

        indexes = [
            models.Index(fields=['documento_numero'], name='documento_numero_idx'),
            models.Index(fields=['culturas_plantadas'], name='culturas_plantadas_idx'),
            models.Index(fields=['estado'], name='estado_idx')
        ]

    def __str__(self):
        return f'{self.nome_produtor} - {self.nome_fazenda}'
