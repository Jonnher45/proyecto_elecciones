from django.contrib import admin
from app1 import models

# Register your models here.
admin.site.register([models.Lista, models.Candidato,  models.Usuario, models.Voto])