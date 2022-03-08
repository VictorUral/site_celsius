from django import forms
from .models import *


class CelsiusForm(forms.Form):
	choice_degrees = (
		('C', 'Цельсий'),
		('F', 'Фаренгейт'),
	)
	
	celsius = forms.ChoiceField(choices = choice_degrees, label='Выбирите градусы:', widget=forms.RadioSelect())
	value = forms.IntegerField(label='Введите значение:',)
