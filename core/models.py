from django.db import models

class Anime(models.Model):
    STATUS_CHOICES = [
        ('PLANNING', 'Planejo Assistir'),
        ('WATCHING', 'Assistindo'),
        ('COMPLETED', 'Concluído'),
    ]

    mal_id = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=255)
    imagem_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNING')
    nota = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo