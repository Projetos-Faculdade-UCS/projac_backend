from django.db import models

class Area(models.Model):
    """
        Modelo de área do conhecimento
    """
    nome = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome

class SubArea(models.Model):
    """
        Modelo de subárea do conhecimento
    """
    nome = models.CharField(max_length=255, null=False)
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name='subarea_set'
    )

    def __str__(self):
        return self.nome
