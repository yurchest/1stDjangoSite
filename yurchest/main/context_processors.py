
def nav_bar(request):
	menu = [
	    {'title': "Главная", 'url_name': 'home'},
	    {'title': "Str1", 'url_name': 'str1'},
	    {'title': "Str2", 'url_name': 'str2'},
	    {'title': "Str3", 'url_name': 'str3'},
	    {'title': "О сайте", 'url_name': 'about'},
	    {'title': "Резюме", 'url_name': 'cv'},
	]
	return {'menu': menu}