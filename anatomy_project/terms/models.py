"""
Модели приложения для работы с анатомическими терминами.

Содержит определение модели Term для хранения пар терминов (русский-латинский).
"""
from django.db import models

class Term(models.Model):
    """Модель для хранения пар анатомических терминов (русский-латынь).
    
    Attributes:
        russian (CharField): Термин на русском языке
        latin (CharField): Соответствующий термин на латыни
        created_at (DateTimeField): Дата и время добавления записи (автоматически)
    
    Methods:
        __str__: Возвращает строковое представление в формате "Русский - Латынь"
    """
    russian = models.CharField(max_length=100, verbose_name="Русский термин")
    latin = models.CharField(max_length=100, verbose_name="Латинский термин")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.russian} - {self.latin}"
