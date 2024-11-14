from django.db import models

class Evento(models.Model):
    ator = models.CharField(max_length=255)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)

    def __str__(self):
        return self.ator
