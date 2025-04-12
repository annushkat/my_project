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

    # def clean(self):
    #     """Кастомная валидация данных формы.
        
    #     Проверяет:
    #     - Что оба поля заполнены
    #     - Что термин с таким русским названием ещё не существует
        
    #     Raises:
    #         forms.ValidationError: Если проверки не пройдены.
    #     """
    #     cleaned_data = super().clean()
    #     russian = cleaned_data.get('russian')
    #     latin = cleaned_data.get('latin')
        
    #     if not russian or not latin:
    #         raise forms.ValidationError("Оба поля должны быть заполнены!")
        
    #     if Term.objects.filter(russian=russian).exists():
    #         raise forms.ValidationError("Этот русский термин уже существует!")
        
    #     return cleaned_data
    