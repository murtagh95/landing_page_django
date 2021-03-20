from django.contrib import admin
from .models import Registrado

# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    # Campos que se veran en las columnas
    list_display = ["email", "nombre", "timestamp"]
    # Se coloca este atributo para poder cambiar el campo que dirije
    # a la vista de tipo formulario
    # list_display_links = ["nombre"]

    list_filter = ["timestamp"]

    # Indicamos que campo se puede modificar desde la misma vista
    # list_editable = ["email"]
    list_editable = ["nombre"]
    
    search_fields = ["email", "nombre"]
    class Meta:
        model = Registrado

admin.site.register(Registrado, AdminRegistrado)
