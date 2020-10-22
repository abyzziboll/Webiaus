import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings

class Usuario(models.Model):
    FUNCAO_CHOICES = [
        ["A", "Administrador"],
        ["U", "Usuário"]
    ]

    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    senha = models.CharField(max_length=20, null=False)
    funcao = models.CharField(max_length=1, choices=FUNCAO_CHOICES)

    def gravar(self):
        self.save()

    def __str__(self):
        return self.nome


