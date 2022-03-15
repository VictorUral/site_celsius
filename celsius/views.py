from django.shortcuts import render, redirect
from .forms import *


menu = [
	{'title': 'Главная страница', 'url_name': 'main'},
	{'title': 'Конвертация Цельсия в Фаренгейты', 'url_name': 'celsius'},
]

def main (request):
	return render (request, 'celsius\main.html', {'menu': menu, 'title': 'Главная страница'})

def celsius (request):
	rez = None
	conversion = request.session.get('conversion')
	if request.method == 'POST':
		form = CelsiusForm(request.POST)
		if form.is_valid():
			celsius_form = form.cleaned_data.get('celsius')
			value_form = form.cleaned_data.get('value')
			if celsius_form == 'F':
				rez = str(value_form)+' °F = '+str(5/9*(value_form-32))+' °C'
				if conversion:
					request.session['conversion'].insert(0, rez)
					request.session.modified = True # если не указать эту строчку то новое добавленное значение в список заменит предыдущее, а не дополнит список
				else:
					request.session['conversion'] = [rez]
			else:
				rez = str(value_form)+' °C = '+str(value_form*1.8+32)+' °F'
				if conversion:
					request.session['conversion'].insert(0, rez)
					request.session.modified = True
				else:
					request.session['conversion'] = [rez]
	else:
		form = CelsiusForm()
		
	return render (request, 'celsius\celsius.html', {'menu': menu, 'form': form, 'rez': rez, 'conversion': conversion, 'title': 'Конвертация Цельсия в Фаренгейты'}) 
	
def  cleaning_session (request):
	del request.session['conversion']
	return redirect('celsius')
