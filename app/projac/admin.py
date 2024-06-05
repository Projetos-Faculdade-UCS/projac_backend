'''admin module'''

from django.contrib import admin
from projac.models import Area, SubArea, Projeto,ProducaoAcademica,ValorArrecadado,AgenciaFomento

# Register your models here.

admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Projeto)
admin.site.register(ProducaoAcademica)
admin.site.register(ValorArrecadado)
admin.site.register(AgenciaFomento)
