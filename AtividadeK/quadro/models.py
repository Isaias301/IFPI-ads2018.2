from django.db import models

# Create your models here.
class Quadro(models.Model):

    titulo = models.CharField("Titulo", max_length=150)
    particular = models.BooleanField("E particular?", default=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True, null=False, blank=False)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = 'Quadro'
        verbose_name_plural = 'Quadros'
        ordering = ('titulo',)


    def __str__(self):
        return self.titulo