from django import forms
from .models import Term

class TermForm(forms.ModelForm):
    """Форма для добавления и редактирования терминов.
    
    Attributes:
        Meta (class): Вложенный класс для конфигурации формы.
    
    Inherits:
        forms.ModelForm: Базовый класс Django для форм, связанных с моделями.
    """
    class Meta:
        """Конфигурация формы, связанной с моделью Term.
        
        Attributes:
            model (Term): Модель, с которой связана форма.
            fields (list): Поля модели, включаемые в форму.
            labels (dict): Пользовательские labels для полей формы.
            widgets (dict): Кастомизация виджетов полей формы.
        """
        model = Term
        fields = ['russian', 'latin']
        labels = {
            'russian': 'Русский термин',
            'latin': 'Латинский термин',
        }
        widgets = {
            'russian': forms.TextInput(attrs={'class': 'form-control'}),
            'latin': forms.TextInput(attrs={'class': 'form-control'}),
        }
