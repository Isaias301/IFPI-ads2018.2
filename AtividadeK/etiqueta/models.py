from django.db import models

# Create your models here.
class Etiqueta(models.Model):

    nome = models.CharField("Nome", max_length=150)
    cor = models.CharField("Cor", max_length=45)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True, null=False, blank=False)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ('nome',)


    def __str__(self):
        return self.nome