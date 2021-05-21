from django.db import models

class UrlRedirect(models.Model):
    destino = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f'UrlRedirect para {self.destino}'

class UrlLog(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    origem = models.URLField(max_length=512, null=True, blank=True)
    #null significa "campo opcional" e blank quer dizer que é um campo que pod ficar em branco
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.IPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(UrlRedirect, models.DO_NOTHING, related_name='logs')
    #ForeignKey é para "importar" ou fazer uma ligação entre a outra class e essa