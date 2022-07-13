from .models import VisitNumber, Userip

def change_info(request):
	number_visits = VisitNumber.objects.filter(id=1)
	if number_visits:
		number_visits = number_visits[0]
		number_visits.count += 1
	else:
		number_visits = VisitNumber(id=1)
		number_visits.count = 1
	number_visits.save()

	if 'HTTP_X_FORWARDED_FOR' in request.META:  # Получить IP
		client_ip = request.META['HTTP_X_FORWARDED_FOR']
		client_ip = client_ip.split(",")[0]  # Так вот настоящий айпи
	else:
		client_ip = request.META['REMOTE_ADDR']  # Получить IP прокси здесь
		# print(client_ip)

	ip_exist = Userip.objects.filter(ip=str(client_ip))
	if ip_exist:  # Определить, существует ли ip
		uobj = ip_exist[0]
		uobj.count += 1
	else:
		uobj = Userip()
		uobj.ip = client_ip
		uobj.count = 1
	uobj.save()