from django.contrib import admin
from . models import Pergunta, Alternativa

class AlternativaInline(admin.StackedInline):
    model = Alternativa
    extra = 3

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['texto']}),
        ('Informações de data:', {'fields':['data_pub']}),
    ]
    inlines = [AlternativaInline]

admin.site.register(Pergunta, PerguntaAdmin)

# Register your models here.
