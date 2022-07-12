import telepot

token = '5527808459:AAGM0ZDhNe5KBShDtU3TH45ZVThXdpYwU94'
telegramBot = telepot.Bot(token)


def send_message(text):
	telegramBot.getMe()
	telegramBot.sendMessage(567804607, text, parse_mode="Markdown")