"""admin module"""

from django.contrib import admin
from projac.models import (
    AgenciaFomento,
    Area,
    Pesquisador,
    PesquisadorProjeto,
    ProducaoAcademica,
    Projeto,
    SubArea,
    ValorArrecadado,
)

# Register your models here.

admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Projeto)
admin.site.register(ProducaoAcademica)
admin.site.register(ValorArrecadado)
admin.site.register(AgenciaFomento)
admin.site.register(Pesquisador)
admin.site.register(PesquisadorProjeto)
