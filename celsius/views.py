from django.shortcuts import render
from .forms import *


menu = [
	{'title': 'Главная страница', 'url_name': 'main'},
	{'title': 'Конвертация Цельсия в Фаренгейты', 'url_name': 'celsius'},
]

def main (request):
	return render (request, 'celsius\main.html', {'menu': menu, 'title': 'Главная страница'})

def celsius (request):
	rez = None
	degrees = None
	if request.method == 'POST':
		form = CelsiusForm(request.POST)
		if form.is_valid():
			celsius_form = form.cleaned_data.get('celsius')
			value_form = form.cleaned_data.get('value')
			if celsius_form == 'F':
				rez = 5/9*(value_form-32)
				degrees = celsius_form
			else:
				rez = value_form*1.8+32
				degrees = celsius_form
	else:
		form = CelsiusForm()
		
	return render (request, 'celsius\celsius.html', {'menu': menu, 'form': form, 'degrees': degrees, 'rez': rez, 'title': 'Конвертация Цельсия в Фаренгейты'})  
