
def nav_bar(request):
	menu = [
	    {'title': "Главная", 'url_name': 'home'},
	    {'title': "Сообщения", 'url_name': 'messages'},
	    {'title': "Новости", 'url_name': 'news'},
	    {'title': "Str3", 'url_name': 'str3'},
	    {'title': "О сайте", 'url_name': 'about'},
	    {'title': "Резюме", 'url_name': 'cv'},
	]
	return {'menu': menu}