from django.db import models
from django.contrib.auth.models import User


# Classes abstratas
class Base(models.Model):
    registrado_em = models.DateTimeField(auto_created=True)
    atualizaocao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Base_Ativos(models.Model):
    registrado_em = models.DateTimeField(auto_created=True)
    atualizaocao = models.DateTimeField(auto_now=True)
    condicao = models.CharField(max_length=255)

    class Meta:
        abstract = True


# Classes pro DB
class Proprietario(Base):
    pro_name = models.CharField(max_length=255)
    email = models.EmailField()
    prop_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'usu_table'
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"
        unique_together = ['email', 'prop_id']

    def __str__(self):
        return self.pro_name


class Complexo(Base):
    name_com = models.CharField(max_length=255, unique=True)
    propri_f_id = models.ForeignKey(Proprietario, related_name='complexo', on_delete=models.CASCADE)
    num_parks = models.IntegerField()

    class Meta:
        db_table = 'comp_table'
        verbose_name = 'Complexo'
        verbose_name_plural = 'Complexos'

    def __str__(self):
        return self.name_com


class Parque(Base):
    cod_park = models.CharField(max_length=255, unique=True)
    id_complexo = models.ForeignKey(Complexo, related_name='parque', on_delete=models.CASCADE)
    num_wtg = models.IntegerField()

    class Meta:
        db_table = 'parl_table'
        verbose_name = 'Parque'
        verbose_name_plural = 'Parques'

    def __str__(self):
        return self.cod_park


class Turbina(Base_Ativos):
    wtg_id = models.CharField(max_length=255, unique=True)
    pk_intalado = models.ForeignKey(Parque, related_name='turbina', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wtg_table'
        verbose_name = 'Turbina'
        verbose_name_plural = 'Turbinas'

    def __str__(self):
        return self.wtg_id
