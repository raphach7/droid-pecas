from django.contrib import admin
from core.models import Endereco, Anunciante, Contato, Demanda

class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        "rua",
        "numero",
        "complemento",
        "bairro",
        "cep",
        "estado",
        "cidade",
    )
  
    search_fields = ("cep",)

class AnuncianteAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
    )

    search_fields = ("usuario",)
  
class ContatoAdmin(admin.ModelAdmin):
    list_display = (
        "ddd",
        "celular"
    )
  
class DemandaAdmin(admin.ModelAdmin):
    list_display = (
        "descricao",
        "endereco_entrega",
        "anunciante",
        "contato",
        "status_finalizacao"
    )

    list_filter = ["status_finalizacao"]
    search_fields = ("anunciante", "descricao",)

  
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Anunciante, AnuncianteAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Demanda, DemandaAdmin)