from django.contrib import admin
from . import models


class VariacaoIncline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome',
               'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoIncline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
