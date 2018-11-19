from django.db import models

# Create your models here.
class Cartao(models.Model):

    titulo = models.CharField("Titulo", max_length=45)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True, null=False, blank=False)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = 'Cartao'
        verbose_name_plural = 'Cartões'
        ordering = ('titulo',)


    def __str__(self):
        return self.titulo