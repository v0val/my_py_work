import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
	bot.reply_to(message, ".")

def send_welcome(message):
	bot.send_message(message.chat.id, "")

@bot.message_handler(content_types=['text'])
def summi_poly(message):
    stri = message.text
    polynom1, polynom2 = stri.split()
    polynom1 = polynom1.replace(' ', '')
    polynom2 = polynom2.replace(' ', '')
    # делаю "костыли"
    polynom1 = '+' + polynom1[:-2] + '*x^0'
    polynom2 = '+' + polynom2[:-2] + '*x^0'
    # выясняю какова максимальная степень многочлена, и определяю массив размерности этой степени
    n1 = polynom1.find('^', 1, len(polynom1))
    n2 = polynom2.find('^', 1, len(polynom2))
    p1 = int(polynom1[n1 + 1])
    p2 = int(polynom2[n2 + 1])
    maxi = max(p1, p2)
    # определяю размер списков (по максимуму)
    mas1 = [0] * (maxi + 1)
    mas2 = [0] * (maxi + 1)
    # извлекаю коэфициенты многочлена и пишу их в список, (позиция = степени)
    N = len(polynom1)
    i = maxi + 1
    tr = 0
    while i != 0:
        p1 = polynom1.find('^', tr, N)
        z1 = polynom1.find('+', tr, N)
        z2 = polynom1.find('*', tr, N)
        i = int(polynom1[p1 + 1])
        mas1[i] = int(polynom1[z1 + 1:z2])
        tr = p1 + 1
        #print(int(polynom1[p1 + 1]), polynom1[z1 + 1:z2])
    #print(mas1)
    N = len(polynom2)
    i = maxi + 1
    tr = 0
    while i != 0:
        p1 = polynom2.find('^', tr, N)
        z1 = polynom2.find('+', tr, N)
        z2 = polynom2.find('*', tr, N)
        i = int(polynom2[p1 + 1])
        mas2[i] = int(polynom2[z1 + 1:z2])
        tr = p1 + 1
        #print(int(polynom2[p1 + 1]), polynom2[z1 + 1:z2])
    #print(mas2)

    #print('сумма коэфициентов: ')
    for i in range(maxi + 1):
        mas1[i] = mas1[i] + mas2[i]
    #print(mas1)

    # формируем многочлен (сумма исходных многочленов):

    polynom = ''
    for i in range(maxi, -1, -1):
        if i == 1 or i == -1:
            polynom += str(mas1[i]) + '*x + '
        if i > 0 and mas1[i] != 0 and i != 1:
            polynom += str(mas1[i]) + '*x^' + str(i) + ' + '
        if i <= 0 and i != -1:
            polynom += str(mas1[i]) + ' = 0'
        
        
    #print(polynom)
    bot.send_message(message.chat.id, 'cумма многочленов '+f'{polynom}' )
    #bot.reply_to(message,'ничья')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text + ', дружище')

bot.infinity_polling()
