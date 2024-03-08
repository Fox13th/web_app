from .models import Records
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class RecordsForm(ModelForm):
    class Meta:
        model = Records
        fields = ['title', 'anons', 'full_text', 'date']

        widgets ={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название записи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс записи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст записи'
            })
        }