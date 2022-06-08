from django.db import models

# primeira forma de utilizar o UserModel
# from django.contrib.auth.models import User

# segunda forma de utilizar o UserModel
# from django.conf import settings

# terceira forma de utilizar o UserModel - Forma recomendada
from django.contrib.auth import get_user_model

class Denuncia(models.Model):
    # autor = models.ForeignKey(User, verbose_name='autor', on_delete=models.CASCADE)
    # autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='autor', on_delete=models.CASCADE)
    autor = models.ForeignKey(get_user_model(), verbose_name='autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Denuncia', max_length=500)
    criacao = models.DateTimeField('Criação', auto_now_add=True)

    class Meta:
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"

    def __str__(self):
        return self.titulo