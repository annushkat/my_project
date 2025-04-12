from django.contrib import admin
from .models import Term

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Term.
    
    """
    list_display = ('russian', 'latin', 'created_at')
    search_fields = ('russian', 'latin')
    