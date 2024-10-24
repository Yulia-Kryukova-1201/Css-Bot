from random import randint
import aiogram
import asyncio
import random
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot.asyncio_helper import get_file

bot=Bot(token='7632517853:AAHVCMt5c2Fniy3ncyEJI_fs7c6uPWJLwYs')
dp=Dispatcher()
router=Router()

@router.message(Command('start'))
async def startBot(message: Message):
    first_mess=f"{message.from_user.username}, привет! \n Я Бот-помощник для первокурсников ВСНа.\n Чем я могу тебе помочь?"
    markup = InlineKeyboardBuilder()
    button_f1 = types.InlineKeyboardButton(text='Ищу учебного ассистента', callback_data='Find')
    button_f2 = types.InlineKeyboardButton(text='Ищу записи лекций', callback_data='Lecture')
    button_f3 = types.InlineKeyboardButton(text='Где можно поботать?', callback_data='Botalka')
    button_f4 = types.InlineKeyboardButton(text='Полезные ссылки', callback_data='UrLs')
    button_f5 = types.InlineKeyboardButton(text='Хочется плакать', callback_data='HELP')
    button_f6 = types.InlineKeyboardButton(text='Хочу в бар', callback_data='Bar')
    markup.add(button_f1, button_f2, button_f3, button_f4, button_f5, button_f6)
    await message.answer(first_mess,reply_markup=markup.as_markup())
@dp.callback_query(F.data == 'Find')
async def response1(callback: types.CallbackQuery):
    second_mess = "По какому предмету ты ищещь ассистента?"
    markup1 = InlineKeyboardBuilder()
    assist_f1 = types.InlineKeyboardButton(text="ЛинАл", callback_data="LinAl_assist")
    assist_f2 = types.InlineKeyboardButton(text="Питон", callback_data="Python_assist")
    assist_f3 = types.InlineKeyboardButton(text="МатАн", callback_data="MatAn_assist")
    assist_f4 = types.InlineKeyboardButton(text="С++", callback_data="C++_assist")
    assist_f5= types.InlineKeyboardButton(text="Алкоритмы", callback_data="Alkos_assist")
    assist_f6 = types.InlineKeyboardButton(text="Диcкра", callback_data="Diskra_assist")
    markup1.add(assist_f1, assist_f2, assist_f3, assist_f4, assist_f5, assist_f6)
    await callback.message.answer(second_mess, reply_markup=markup1.as_markup())
@dp.callback_query(F.data == 'Lecture')
async def response2(callback: types.CallbackQuery):
    second_mess = "По какому предмету ты ищещь лекцию?"
    markup2 = InlineKeyboardBuilder()
    subject_f1 = types.InlineKeyboardButton(text="ЛинАл", callback_data="LinAl_lecture")
    subject_f2 = types.InlineKeyboardButton(text="Питон", callback_data="Python_lecture")
    markup2.add(subject_f1, subject_f2)
    await callback.message.answer(second_mess, reply_markup=markup2.as_markup())
@dp.callback_query(F.data == 'Botalka')
async def response3(callback: types.CallbackQuery):
    third_mess = "В каком корпусе ты хочешь поботать?"
    markup3 = InlineKeyboardBuilder()
    korpus_f1 = types.InlineKeyboardButton(text="Покровка", callback_data="Pokrovka")
    korpus_f2 = types.InlineKeyboardButton(text="Мясо", callback_data="Meet")
    markup3.add(korpus_f1, korpus_f2)
    await callback.message.answer(third_mess, reply_markup=markup3.as_markup())
@dp.callback_query(F.data == 'UrLs')
async def response4(callback: types.CallbackQuery):
    fourth_mess = "А вот и полезные ссылочки)"
    markup4 = InlineKeyboardBuilder()
    url_f1 = types.InlineKeyboardButton(text="ЛинАл",
                                        url="https://saharnina.yonote.ru/share/0eef274b-47c8-4b55-a5e3-e45bce12d1b3")
    url_f2 = types.InlineKeyboardButton(text="Питон",
                                        url="http://wiki.cs.hse.ru/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_Python_%D0%9A%D0%9D%D0%90%D0%94_24/25")
    url_f3 = types.InlineKeyboardButton(text="Питон-ведомость",
                                        url="https://docs.google.com/spreadsheets/d/1CIOrRAiYfkrn8_H8aECgg78hbl13VgbOcfAsavfhV2I/edit?gid=960131146#gid=960131146")
    url_f4 = types.InlineKeyboardButton(text="ОРГ-ведомость",
                                        url="https://docs.google.com/spreadsheets/d/1nYELE_GiLsUbxbWJmsGf91ElwFEUPkwl6qaRJAtcZ3A/edit?gid=350665941#gid=350665941")
    markup4.add(url_f1, url_f2, url_f3, url_f4)
    await callback.message.answer(fourth_mess, reply_markup=markup4.as_markup())
@dp.callback_query(F.data == 'HELP')
async def response5(callback: types.CallbackQuery):
    fifth_mess = "Какая проблема тебя беспокоит?"
    markup5 = InlineKeyboardBuilder()
    reason_f1 = types.InlineKeyboardButton(text="Я совсем не понимаю лекции по Питону", callback_data="Problem1")
    reason_f2 = types.InlineKeyboardButton(text="Я совсем не понимаю лекции по ЛинАлу", callback_data="Problem2")
    reason_f3 = types.InlineKeyboardButton(text="У меня горят дедлайны, а я просто хочу лавандовый раф", callback_data="Problem3")
    reason_f4 = types.InlineKeyboardButton(text="Я ничего не понимаю... ",
                                           callback_data="Problem4")
    reason_f5 = types.InlineKeyboardButton(text="У меня ничего не получается. Я котик - у меня лапки... ",
                                           callback_data="Problem5")
    reason_f6 = types.InlineKeyboardButton(text="В моей жизни больше нет смысла... ",
                                           callback_data="Problem6")
    reason_f7 = types.InlineKeyboardButton(text="Мне нужно больше кофеина... Больше кофеина...",
                                           callback_data="Problem7")
    reason_f8 = types.InlineKeyboardButton(text="Я так устал(а) и очень хочу спать...",
                                           callback_data="Problem8")
    reason_f9 = types.InlineKeyboardButton(text="Е**ный БЖД",
                                           callback_data="Problem9")
    reason_f10 = types.InlineKeyboardButton(text="Мне не хватает сил всё это вывезти...",
                                           callback_data="Problem10")
    markup5.add(reason_f1, reason_f2, reason_f3, reason_f4, reason_f5, reason_f6, reason_f7, reason_f8, reason_f9, reason_f10)
    await callback.message.answer(fifth_mess, reply_markup=markup5.as_markup())
@dp.callback_query(F.data == 'LinAl_assist')
async def assists_response1(message:Message):
    f = open('assists.txt', 'r', encoding='utf-8')
    response='А вот и твой ассистент по линалу:'+'\n'
    for p in f.readlines():
        p=p.strip().split()
        if p[0]=="ЛинАл":
            for j in range (1, len(p),3):
                response+=(p[j]+" "+p[j+1]+" "+p[j+2]+"\n")
    await bot.send_message(message.from_user.id, response)
@dp.callback_query(F.data == 'Python_assist')
async def assists_response2(message:Message):
    f = open('assists.txt', 'r', encoding='utf-8')
    response='А вот и твои ассистенты по питону:'+'\n'
    for p in f.readlines():
        p=p.strip().split()
        if p[0]=="Питон":
            for j in range (1, len(p),3):
                response+=(p[j]+" "+p[j+1]+" "+p[j+2]+"\n")
    await bot.send_message(message.from_user.id, response)
@dp.callback_query(F.data == 'MatAn_assist')
async def assists_response3(message:Message):
    f = open('assists.txt', 'r', encoding='utf-8')
    response='А вот и твои ассистенты по матану:'+'\n'
    for p in f.readlines():
        p=p.strip().split()
        if p[0]=="Матан":
            for j in range (1, len(p),3):
                response+=(p[j]+" "+p[j+1]+" "+p[j+2]+"\n")
    await bot.send_message(message.from_user.id, response)
@dp.callback_query(F.data == 'C++_assist')
async def assists_response4(message:Message):
    f = open('assists.txt', 'r', encoding='utf-8')
    response='А вот и твои ассистенты по С++:'+'\n'
    for p in f.readlines():
        p=p.strip().split()
        if p[0]=="С++":
            for j in range (1, len(p),3):
                response+=(p[j]+" "+p[j+1]+" "+p[j+2]+"\n")
    await bot.send_message(message.from_user.id, response)
@dp.callback_query(F.data == 'Alkos_assist')
async def assists_response5(message:Message):
    f = open('assists.txt', 'r', encoding='utf-8')
    response='А вот и твои ассистенты по алкоритмам:'+'\n'
    for p in f.readlines():
        p=p.strip().split()
        if p[0]=="Алгоритмы":
            for j in range (1, len(p),3):
                response+=(p[j]+" "+p[j+1]+" "+p[j+2]+"\n")
    await bot.send_message(message.from_user.id, response)
@dp.callback_query(F.data == 'Diskra_assist')
async def assists_response6(message:Message):
    f = open('assists.txt', 'r', encoding='utf-8')
    response='А вот и твои ассистенты по дискре:'+'\n'
    for p in f.readlines():
        p=p.strip().split()
        if p[0]=="Дискра":
            for j in range (1, len(p),3):
                response+=(p[j]+" "+p[j+1]+" "+p[j+2]+"\n")
    await bot.send_message(message.from_user.id, response)
@dp.callback_query(F.data == 'LinAl_lecture')
async def response1(callback: types.CallbackQuery):
    seventh_mess = "По какой теме ты ищешь лекцию?"
    markup7 = InlineKeyboardBuilder()
    l1=types.InlineKeyboardButton(text="Векторы", callback_data="NoLectures")
    l2=types.InlineKeyboardButton(text="Множества", callback_data="NoLectures")
    l3=types.InlineKeyboardButton(text="Комплексные числа", callback_data="NoLectures")
    l4=types.InlineKeyboardButton(text="Группы, кольца и поля", callback_data="NoLectures")
    l5=types.InlineKeyboardButton(text="Векторные пространства", callback_data="NoLectures")
    l6=types.InlineKeyboardButton(text="Матрицы. Метод Гаусса", callback_data="NoLectures")
    l7=types.InlineKeyboardButton(text="Базис и размерность векторного пространства", callback_data="NoLectures")
    l8=types.InlineKeyboardButton(text="Линейная зависимость", url="https://rutube.ru/plst/641837/")
    l9=types.InlineKeyboardButton(text="Определитель матрицы", url="https://drive.google.com/drive/folders/1sTDSlpReX4OgHdXPd6LB1j0mXreFSq-z")
    l10=types.InlineKeyboardButton(text="Обратные матрицы. Метод Крамера", url="https://drive.google.com/drive/folders/1iblxo0zybgo3jcj3Q6PibJ1uaIPqJbQ2")
    l11=types.InlineKeyboardButton(text="Отображение между векторными пространствами", callback_data="NoLectures")
    markup7.add (l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11)
    await callback.message.answer(seventh_mess, reply_markup=markup7.as_markup())
@dp.callback_query(F.data == 'NoLectures')
async def assists_response(message:Message):
    answer=("К сожалению, записи лекции по этой теме не найдены. Возможно, они появятся чуть позже. Ты можешь попросить конспекты у своих одногруппников, чтобы разобраться с темой")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Python_lecture')
async def response1(callback: types.CallbackQuery):
    seventh_mess = "По какой теме ты ищешь лекцию?"
    markup8 = InlineKeyboardBuilder()
    l1=types.InlineKeyboardButton(text="1 лекция: Арифметика",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-09-10T06-20-18Z.mp4")
    l2=types.InlineKeyboardButton(text="2 лекция: Условный оператор, цикл while, вещественные числа",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-09-12T06-20-18Z.mp4")
    l3=types.InlineKeyboardButton(text="3 лекция: Строки, цикл for",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-09-17T06-20-18Z.mp4")
    l4=types.InlineKeyboardButton(text="4 лекция: Функции и рекурсия",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-09-19T06-20-18Z.mp4")
    l5=types.InlineKeyboardButton(text="5 лекция: Списки и сортировка ",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-09-24T06-20-18Z.mp4")
    l6=types.InlineKeyboardButton(text="6 лекция: Функциональное программирование-1",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-09-26T06-20-18Z.mp4")
    l7=types.InlineKeyboardButton(text="7 лекция: Функциональное программирование-2",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-10-01T06-20-18Z.mp4")
    l8=types.InlineKeyboardButton(text="8 лекция: Множества и словари",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-10-03T06-21-08Z.mp4")
    l9=types.InlineKeyboardButton(text="9 лекция: Классы-1",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-10-08T06-21-11Z.mp4")
    l10=types.InlineKeyboardButton(text="10 лекция: Классы-2",
                                  url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-10-10T06-20-25Z.mp4")
    l11=types.InlineKeyboardButton(text="11 лекция: Классы. Механизм наследования",
                                   url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-10-15T06-23-42Z.mp4")
    l12=types.InlineKeyboardButton(text="12 лекция: Модули и принципы",
                                   url="https://disk.yandex.ru/d/SINY6vliqUkI7w/%D0%93%D0%BE%D1%80%D1%88%D0%BA%D0%BE%D0%B2%20%D0%A1.%202024-10-17T06-20-19Z.mp4")
    markup8.add (l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12)
    await callback.message.answer(seventh_mess, reply_markup=markup8.as_markup())
@dp.callback_query(F.data == 'Pokrovka')
async def botalka_response1(message:Message):
    answer1="Самые базовые коворки на Покровке - это библиотека, большой атриум и кафе \"Груша\". \n В библиотеке есть несколько этажей, так что место поботать всегда найдётся, можно приходить с едой и кофе, здесь на это никто не смотрит. \n Однако есть нюанс: на всех этажах библиотеки, кроме 1, нельзя шуметь и громко разговаривать."
    answer2="Большой Атриум-прекрасное место,чтобы поботать мужду парами. \n Комфортное промтранство, удобные сидения, есть возможность подзарядить свои девайсы - вот что делает Большой Атриум Большим Атриумом. \n Но стоит учитывать, что в Большом Атриуме всегда много людей, и если ты любитель поботать в одиночестве, то тебеб может быть неудобно ботать там"
    answer3="Кафе \"Груша\" - камерная и уютная боталка, которая находится в корпусе R. \n Здесь можно насладится вкусным кофе и выпечкой, не отвелекаясь от процесса бота. \n Один из немногих минусов этого кафе - очень мало места и там почти всегда заняты места."
    await bot.send_message(message.from_user.id, answer1+'\n'+'\n'+answer2+'\n'+'\n'+answer3)
@dp.callback_query(F.data == 'Meet')
async def botalka_response2(message:Message):
    answer1="База бота на Мясе - это коворки на этажах М20. Особенно на 5 и 6. \nА также атриум на М20 и коворк на Кривоколенном."
    answer2="Коворки на этажах М20 - это без преувеличения лучшее места для бота. Здесь есть боталки на любой вкус - от одиночных столов до пуфиков и креслиц. Также тут много розеток, так что здесь удобно ботать с компом. "
    answer3="Малый Атриум на М20 - комфортное пространсвтво для работы над групповыми проектом. Здесь есть и круглый стол с пуфиками, и парты с удобными креслами. Вообщем это прекрасное места для бота. Пока там немного людей. Чаще всего (особенно ближе к вечеру) там собирается множество студентов и становится очень-очень тесно."
    answer4="Коворк на Кривоколенном - один из самых лучших коворков в кластере на Мясе. Сам коворк поделён на несколько зон, так что даже если в коворке собирается много людей, каждый сможет найти себе место для бота. В этои и есть вся прелесть коворка на Кривоколенном. "
    await bot.send_message(message.from_user.id, answer1+'\n'+'\n'+answer2+'\n'+'\n'+answer3+"\n"+"\n"+answer4)
@dp.callback_query(F.data == 'Problem1')
async def help_response1(message:Message):
    answer=("С этой проблемой сталкиваются многие первокурсники ВСНа, так что это основа, так сказать, база (а всё потому что лектор слегка (нет) криво объясняет и часто забегает вперед).\n \n Возможные решения:\n \n 1) Попробуй пересмотреть непонятную лекцию несколько раз, останавливая и разбирая, что делает лектор и почесу это так.\n \n 2) Доставай ассистентов с любыми вопросами. Они обязательно ответят и помогут. Наверное. \n 3) Не бойся спрашивать одногруппников про контесты и лекции. В группе обязательно найдутся шарящие люди. \n Как говорится, командная работа-наше всё! \n \n 4) Если не понятно, как работает та или иная функция, или хочешь уточнить синтаксис, попробуй почитать документацию к языку Python или найди интересующую тему на ФКН вики \n (ссылка есть в боте в разделе \"Полезные ссылки\"-\"Питон\")" )
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem2')
async def help_response2(message:Message):
    answer=("ЛинАл - это первая ступенька на лестнице, ведущей в мир математики и программирования на ВСНе, поэтому стоит хорошо разбираться в идеях Линейной Алгебры. \n \n Советы: \n \n  1) Пересмотри лекции и попроси конспекты у одногруппников. Повторение материала помогает его быстрее понять и запомнить. \n \n 2) Обязательно ходи на консультации по ЛинАлу от ассистентов. На консультации разбирается много полезных задач, на примере которых можно быстрее понять тему. \n \n 3) Консультации от Нины Евгеньевны - это тоже мастхэв для любого ВСНщика. \n \n 4) Доставай ассистентов со всеми своими вопросами и непонятками. Они помогут)")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem3')
async def help_response3(message:Message):
    answer=("Плевать на дедлайны. \nПусть горят синим пламенем. \nПросто иди и возьми себе большой лавандовый раф, Солнышко)")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem4')
async def help_response4(message:Message):
    answer=("Чтобы понять, что происходит вокруг тебя, нужно сначала разобраться в себе, понять себя и свои эмоции. \n \nВ этом тебе поможет моя коллега: @moodtracker_arrpely_bot")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem5')
async def help_response(message:Message):
    answer=("В этой ситуации главное - не поддаваться панике и не стрессовать. Если что-то не получается с первого раза - это нормально, пробуй ещё и ещё раз. \n \n У тебя всё получится) \n Даже если ты котик и у тебя лапки)")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem6')
async def assists_response6(message:Message):
    answer = ("Не грусти, держи анекдот: \n \n")
    f = open('anecdoty.txt', 'r', encoding='utf-8')
    f = f.readlines()
    a = random.randint(0, len(f) - 1)
    s = f[a].split()
    response = ''
    for i in range(len(s)):
        if s[i] == '\\r\\n':
            response += ('\n')
        else:
            response += (str(s[i]) + " ")
    answer+=response
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem7')
async def help_response7(message:Message):
    answer=("Если для высокой продуктивности тебе необходима чашка кофе, обязательно посети эти кофейни: \n \n 1) \"Jeffrey's Coffee\". Уютная атмосфера, разнообразное меню и вкусный кофе помогут тебе найти тот самый напиток, с которым ты будешь ботать до полуночи. В Jeffrey's есть карта лояльности, на которую приходит кэшбек бонусами от покупок, так что не забывай предъявить карту на кассе) \n \n 2) \"Правда Кофе\". Прекрасная кофейня, которая радует каждого студента ароматным и вкусным кофе и приятными ценами. А если ещё покажешь студенческий при покупке напитка от среднего размера, получишь скидку 10% \n \n (Это не реклама, честно) ")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem8')
async def help_response8(message:Message):
    answer=("Даже если у тебя горят дедлайны и ты ничего не успеваешь, всё равно не стоит пренебрегать своим здоровьем и сном. \n \n Так что заходи в коворки на М20 , аходи себе пуфик и располагайся по-удобнее, ведь в ближайший час ты просто спокойно поспишь)")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem9')
async def help_response9(message:Message):
    answer=("Это головная боль многих первокурсников, так что здесь ничего не поделаешь... Просто эту фигню надо закрыть, несмотря на то, что она постоянно ложится. \n \n Как говорил один классик: \n\"Нормальный предмет 3мя буквами не назовут\" ")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Problem10')
async def help_response10(message:Message):
    answer=("В этой ситуации главное - не словить выгорание. Чтобы восполнить физические и душевные силы, выдели себе целый день. Отдохни, погуляй, закажи любимую еду, сделай себе масочку и ни о чём не беспокойся. \n \n Не ничего важнее твоего душевного здоровья \n \n Помни об этом)")
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Bar')
async def bar_response1(callback: types.CallbackQuery):
    second_mess = "С какой целью ты хочешь пойти в бар?"
    markup1 = InlineKeyboardBuilder()
    bar_f1 = types.InlineKeyboardButton(text="Напиться и забыться", callback_data="Bar_YES")
    bar_f2 = types.InlineKeyboardButton(text="Посидеть с компанией друзей и культурно выпить", callback_data="Bar_YES")
    bar_f3 = types.InlineKeyboardButton(text="Поботать", callback_data="Bar_NO")
    markup1.add(bar_f1, bar_f2, bar_f3)
    await callback.message.answer(second_mess, reply_markup=markup1.as_markup())
@dp.callback_query(F.data == 'Bar_YES')
async def bar_response1(message:Message):
    answer=("Ты сделал правильный выбор, первак! \n Вот список классных баров на Чистых: \n \n1) Волчья стая \n2) Сионист \n3) Слоны и мамонты \n4) Пока никто не видит \n5) Крапива \n6) BeerMood \n7) На чили \nУдачи, первак!" )
    await bot.send_message(message.from_user.id, answer)
@dp.callback_query(F.data == 'Bar_NO')
async def bar_response2(callback: types.CallbackQuery):
    response=("Первак, подумай хорошенько и прими правильный выбор. Ведь только приняв правильный выбор, мы обретаем свободу!")
    markup1 = InlineKeyboardBuilder()
    bar_f1 = types.InlineKeyboardButton(text="Я иду пить!!!", callback_data="Bar_YES")
    markup1.add(bar_f1)
    await callback.message.answer(response, reply_markup=markup1.as_markup())
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__=='__main__':
    asyncio.run(main())
