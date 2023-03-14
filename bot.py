import telebot
from bs4 import BeautifulSoup
from random import randint
import os
from fuzzywuzzy import fuzz

mas = []
muscal = ["musick/b1.mp3", 'musick/bc1.mp3','musick/ns1.mp3', "musick/fa1.mp3", "musick/bc2.mp3", "musick/bz1.mp3", "musick/a1.mp3","musick/m1.mp3"]

def sredsl(text):
    try:
        text=text.lower().strip()
        if os.path.exists('base.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'

def t_bot(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,"привет хочешь узнать топ аниме напиши '/animetop' , хочешь увидеть рандомное аниме то пиши '/randomanime', если хочешь поиграть в игру угадай опенинг то напиши '/opplay', если хочешь поговорить с бот_тян то просто напиши ей , напиши /about это о создателе")

    @bot.message_handler(commands=['animetop'])
    def animtop_message(message):
        headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36" }
        # with open("anime_top.html",'w',encoding="utf8") as file:
        #     file.write(req.text)
        with open("anime_top.html",encoding="utf8") as file:
            src = file.read()
        
        soup = BeautifulSoup(src, "lxml")
        div_naz = soup.find_all("div",class_="movie-item__title")
        a_ss = soup.find_all("a",class_="movie-item__link")
        cout = 0
        for i in div_naz:
            a = a_ss[cout]
            a = a.get('href')
            strr = f"{i.text}. Посмотреть на https://yummyanime.tv/top-100/{a}"
            bot.send_message(message.chat.id,strr)
            cout+=1
        
    @bot.message_handler(commands=['randomanime'])
    def animtop_message(message):
        headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36" }
        # with open("anime_top.html",'w',encoding="utf8") as file:
        #     file.write(req.text)
        with open("anime_top.html",encoding="utf8") as file:
            src = file.read()
        
        soup = BeautifulSoup(src, "lxml")
        div_naz = soup.find_all("div",class_="movie-item__title")
        a_ss = soup.find_all("a",class_="movie-item__link")
        cout = 0
        massiv = []
        for i in div_naz:
            a = a_ss[cout]
            a = a.get('href')
            strr = f"{i.text}. Посмотреть на https://yummyanime.tv/top-100/{a}"
            massiv.append(strr)
            cout+=1

        rand = randint(0,100)
        bot.send_message(message.chat.id,massiv[rand])
        
    @bot.message_handler(commands=['opplay']) 
    def oppla(message):
        global indi
        index1 = randint(0,len(muscal)-1)
        indi = index1
        bot.send_audio(message.chat.id, open(muscal[index1],'rb'))
        bot.register_next_step_handler(message, op)
        bot.send_message(message.chat.id,"Как вы думайте из какого аниме этот опенинг?")

    @bot.message_handler(commands='about')
    def about(message):
        bot.send_message(message.chat.id,"Созадетель Семенов Святолсав")
        bot.send_message(message.chat.id,"github - https://github.com/ElephantGame1")
        bot.send_message(message.chat.id,"sourceforge - https://sourceforge.net/u/elephantgame/profile")
        bot.send_message(message.chat.id,"itch - https://elephant-studio.itch.io/")

    #чат бот
    @bot.message_handler()
    def chat_bot(message):
        f=open(str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
        s=sredsl(message.text)
        f.write('u: ' + message.text + '\n' + s +'\n')
        f.close()
        bot.send_message(message.chat.id, s)

    @bot.message_handler(content_types='text')
    def op(message):
        global indi
        text = message.text
        slovo = text.lower()
        if "блич" in slovo and indi == 0:
            bot.send_message(message.chat.id,"Правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")
        elif "черный клевер" in slovo and indi == 1 or "черный клевер" in slovo and indi == 4 or "чёрный клевер" in slovo and indi == 1 or "чёрный клевер" in slovo and indi == 4:
            bot.send_message(message.chat.id,"Правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")
        elif "в школе маг" in slovo and indi == 2:
            bot.send_message(message.chat.id,"Правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")
        elif "алхимик" in slovo and indi == 3:
            bot.send_message(message.chat.id,"Правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")
        elif "бездомный бог" in slovo and indi == 5:
            bot.send_message(message.chat.id,"Правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")
        elif "атака титанов" in slovo and indi == 6:
            bot.send_message(message.chat.id,"Правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")
        elif "мастера меча онлайн" in slovo and indi == 7 or "ммо" in slovo and indi == 7 or "ммо" in slovo and indi == 7 :
            bot.send_message(message.chat.id,"Правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")
        else:
            bot.send_message(message.chat.id,"Не правильно")
            indi = 0
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.chat.id,"Веселая игра получилась?")

    bot.infinity_polling()

# get_data("https://yummyanime.tv/top-100/",mesto)
tokin = "5046906232:AAGa4ffor0g9BvK0jr3sYw44UkFI47ReA0Y"
if os.path.exists('base.txt'):
    f=open('base.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()

t_bot(tokin)

