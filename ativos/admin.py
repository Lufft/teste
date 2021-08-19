from django.contrib import admin
from .models import Base,Base_Ativos ,Proprietario, Complexo, Parque, Turbina
# Register your models here.

@admin.register(Proprietario)
class PropAdmin(admin.ModelAdmin):
    list_display = ['prop_id', 'pro_name', 'email']

@admin.register(Complexo)
class CompAdmin(admin.ModelAdmin):
    list_display = ['name_com', 'num_parks', 'propri_f_id']

@admin.register(Parque)
class PkAdmin(admin.ModelAdmin):
    list_display = ['cod_park', 'num_wtg', 'id_complexo']

@admin.register(Turbina)
class WtgAdmin(admin.ModelAdmin):
    list_display = ['wtg_id', 'pk_intalado', 'condicao']

