import telepot

token = '5527808459:AAGM0ZDhNe5KBShDtU3TH45ZVThXdpYwU94'
my_id = 177914540
telegramBot = telepot.Bot(token)

def send_message(text):
	content_type, chat_type, chat_id = telepot.glance(msg)
