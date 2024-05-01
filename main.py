import random
import json
from pathlib import Path

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BALANCE = 0

bot = Bot(token="6266482683:AAHfDQoC-e5gM3bqyCyBFka65O9Tmqx3gUI")

PAYMENT_TOKEN = "1877036958:TEST:b29e43a1e7b7c69abeff4364bb5d61e3c9dd4ec4"

dp = Dispatcher(bot)

kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1.add(KeyboardButton('/registratic'))

kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb2.add(KeyboardButton('1.'))
kb2.insert(KeyboardButton('2.'))
kb2.insert(KeyboardButton('3.'))

kb3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3.add(KeyboardButton('+200'))
kb3.insert(KeyboardButton('+100'))
kb3.add(KeyboardButton('+50'))
kb3.insert(KeyboardButton('+30'))
kb3.add(KeyboardButton('+20'))
kb3.insert(KeyboardButton('+10'))

kb4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb4.add(KeyboardButton('Играть▶️'))
kb4.insert(KeyboardButton('Пополнение и вывод🔁'))
kb4.add(KeyboardButton('Баланс💸'))
kb4.insert(KeyboardButton('Помощь🆘'))
kb4.add(KeyboardButton('Рефералы🧩'))

kb5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb5.add(KeyboardButton('/TotalUsers'))
kb5.insert(KeyboardButton('/TotalBalance'))
kb5.add(KeyboardButton('/ListListing'))
kb5.insert(KeyboardButton('/TransVar'))

kb6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb6.add(KeyboardButton('200'))
kb6.insert(KeyboardButton('100'))
kb6.add(KeyboardButton('50'))
kb6.insert(KeyboardButton('30'))
kb6.add(KeyboardButton('20'))
kb6.insert(KeyboardButton('10'))

kb7 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb7.add(KeyboardButton('❌Заблокировано❌'))

kb8 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb8.add(KeyboardButton('Мой код↗️'))
kb8.insert(KeyboardButton('Ввести код↘️'))
kb8.add(KeyboardButton('Назад⬅️'))

ban_list = []

TotalUsers_list = []  #

user_id = []  #
referral_list = []  #
referral_used_list = []  #
bal_list = []  #
rate_list = []  #
number_list = []  #

admin_list_2 = [1076857652]  #
admin_list = [1076857652]  #

referral_var = [10]
trans_var = [0]

# ----------------------------------------------------Filling-list------------------------------------------------------

with open('user.txt', 'r') as f:
    text = f.read()
    print(user_id)
user_id = [int(x) for x in text[1:-1].split(',')]
print(user_id)

with open('balance.txt', 'r') as f:
    text = f.read()
    print(bal_list)
bal_list = [int(x) for x in text[1:-1].split(',')]
print(bal_list)

with open('admin_list_2.txt', 'r') as f:
    text = f.read()
    print(admin_list_2)
admin_list_2 = [int(x) for x in text[1:-1].split(',')]
print(admin_list_2)

with open('admin_list.txt', 'r') as f:
    text = f.read()
    print(admin_list)
admin_list = [int(x) for x in text[1:-1].split(',')]
print(admin_list)

with open('rate.txt', 'r') as f:
    text = f.read()
    print(rate_list)
rate_list = [int(x) for x in text[1:-1].split(',')]
print(rate_list)

with open('referal_user_list.txt', 'r') as f:
    text = f.read()
    print(referral_used_list)
referral_used_list = [int(x) for x in text[1:-1].split(',')]
print(referral_used_list)

with open('total.txt', 'r') as f:
    text = f.read()
    text_2 = text.replace("'", "")
    text_3 = text_2.replace(",", "")
    print(TotalUsers_list)
TotalUsers_list = [str(x) for x in text_3[1:-1].split(' ')]
print(TotalUsers_list)

with open('referal_list.txt', 'r') as f:
    text = f.read()
    text_2 = text.replace("'", "")
    text_3 = text_2.replace(",", "")
    print(referral_list)
referral_list = [str(x) for x in text_3[1:-1].split(' ')]
print(referral_list)

with open('number.txt', 'r') as f:
    text = f.read()
    text_2 = text.replace("'", "")
    text_3 = text_2.replace(",", "")
    print(number_list)
number_list = [str(x) for x in text_3[1:-1].split(' ')]
print(number_list)

with open('ban.txt', 'r') as f:
    text = f.read()
    text_2 = text.replace("'", "")
    text_3 = text_2.replace(",", "")
    print(ban_list)
ban_list = [str(x) for x in text_3[1:-1].split(' ')]
print(ban_list)

# ----------------------------------------------------Filling-list------------------------------------------------------

RANDOM = ['1.', '2.', '3.']

reg2 = '''
Вы уже зарегистрированы!✅
Нажимай ' Играть▶️ ' и вперёд к большим выигрышам!'''

popol = '''
Пополнение⬇️
Если вы хотите пополнить баланс то вводите суму с '+' перед суммой пополнения...
Пример: +100

Вывод⬆️
Если вы хотите вывести средства с баланса вводите сумму с ' - ' перед суммой вывода,
затем через пробел введите номер карты для вывода используя "<>"💳
Пример: -100 <4441 1144 0000 0000>

️⚠️В случае неправильного ввода данных, запрос на вывод не будет передан администратору!'''

ban_text = '''
Ваш аккаунт мог быть заблокирован по одной или нескольким причинам!
Одни из причин:
* Мошенничество
* Попытки нарушить работу бота
* Нарушение работы бота
* Обман
* 
И т.д...

⚠️⚠️⚠️
Если вы считаете что произошла ошибка, и вы хотите вывести средства, то перешлите это сообщение нашему администратору, 
так же он вам скажет точную причину блокировки аккаунта.

admin: @nikita_web_zone'''

oplata = '''

✅Оплатите введёную сумму за ссылкой ниже⬇️'''

okarta = '''
Ваша карта отправлена!💳✅

Вскоре администратор выведет ваши деньги.💸'''

vvyvoda = '''

⚠️К сожалению во время вывода средст нельзя играть, и игра будет заблокирована.

Администратор в течении нескольких минут выведет ваши средства и разблокирует игру✅'''

START = '''
Привет!❤️

Я бот, нажимай кнопку ниже и начинай играть у тебя уже на балансе 100 игровых монет

Тестовый бот, перед запуском. Попробуйте поиграть используя демо счёт,
и если вы нашли что нам нужно улучшить, или ваше предложения то пиши "! Ваше предложение" прямо в бот.
Обязательно напишите восклицательный знак, пробел, и затем ваш текс. Мы будем очень рады если вы напишете нам.)  

Жми кнокупку регистрации ниже, и начинай!💸🥳'''

HELP = '''
Тестовый бот, перед запуском. Попробуйте поиграть используя демо счёт,
и если вы нашли что нам нужно улучшить, или ваше предложения то пиши "! Ваше предложение" прямо в бот.
Обязательно напишите восклицательный знак, пробел, и затем ваш текс. Мы будем очень рады если вы напишете нам.)



Слеш команды пользователей:
/start -”Команда для запуска бота”
/help - “Команда помощи, связи с администратором”
/registratic -”Команда регистрации”

Команды пользователей:
Баланс💸  -”Команда для проверки баланса”
Помощь🆘 -”Команда помощи, связи с администратором”
Пополнение и вывод🔁 -”Команда для запуска бота”
Играть▶️ -”Команда для начала игры”
Рефералы🧩 -”Команда для открытия опции (Рефералы)”
Назад⬅️ -”Команда возвращения на главное меню”
Мой код↗️ -”Команда просмотра своего реферального кода”
Ввести код↘  -”Команда для ввода реферального кода”

Связь с администратором: @nikita_web_zone'''


# ------------------------------------------------PAYMENT---------------------------------------------------------------


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def succsess(message: types.Message):
    await message.answer(f'Платёж прошёл успешно: {message.successful_payment.order_info}')


# ------------------------------------------------USER------------------------------------------------------------------


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=START, reply_markup=kb1)
    await bot.send_message(chat_id=admin_list[0], text=f'NEW USER!!!\n\n{message.from_user.first_name}\n'
                                                       f'{message.from_user.username}\n{message.from_user.id}',
                           reply_markup=kb1)


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=HELP, reply_markup=kb4)


@dp.message_handler(commands=['registratic'])
async def reg_message(message: types.Message):
    chat_id = message.from_user.id
    if chat_id in user_id:
        await bot.send_message(chat_id=chat_id, text=reg2, reply_markup=kb4)
    elif chat_id not in user_id:
        if chat_id in ban_list:
            await bot.send_message(chat_id=chat_id, text='❌ К сожалению ваш аккаунт был заблокирован!',
                                   reply_markup=kb7)
        elif chat_id not in ban_list:
            user_id.append(message.from_user.id)
            referral_list.append(f'RE{message.from_user.id}')
            referral_used_list.append(1)
            bal_list.append(100)
            rate_list.append(0)
            number_list.append(' ')
            TotalUsers_list.append(f'@{message.from_user.username}')
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
            file = open('rate.txt', 'w')
            file.write(str(rate_list))
            file.close()
            file = open('number.txt', 'w')
            file.write(str(number_list))
            file.close()
            file = open('user.txt', 'w')
            file.write(str(user_id))
            file.close()
            file = open('total.txt', 'w')
            file.write(str(TotalUsers_list))
            file.close()
            await bot.send_message(chat_id=chat_id, text='Вы успешно зарегистрировались✅', reply_markup=kb4)


# ------------------------------------------------ADMIN-----------------------------------------------------------------

@dp.message_handler(commands=['Admin'])
async def start_message(message: types.Message):
    if message.from_user.id in admin_list:
        await bot.send_message(chat_id=message.from_user.id, text="welcome admin", reply_markup=kb5)
    elif message.from_user.id not in admin_list:
        await bot.send_message(chat_id=message.from_user.id, text="You no admin!")
        await bot.send_message(chat_id=admin_list[0],
                               text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                    f"\nПытался зайти в админ-панель!",
                               reply_markup=kb5)


@dp.message_handler(commands=['TotalUsers'])
async def start_message(message: types.Message):
    if message.from_user.id in admin_list:
        a = len(TotalUsers_list)
        await bot.send_message(chat_id=message.from_user.id, text=f'Total Users: {a}', reply_markup=kb5)
    elif message.from_user.id not in admin_list:
        await bot.send_message(chat_id=message.from_user.id, text=f'No command!')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'!!! USER: {message.from_user.id}\n@{message.from_user.username}\n'
                                    f'\nПопитка мошеничества!\n'
                                    f'\n"Нажатие команды /TotalUser".',
                               reply_markup=kb5)


@dp.message_handler(commands=['TotalBalance'])
async def start_message(message: types.Message):
    if message.from_user.id in admin_list:
        a = sum(bal_list)
        await bot.send_message(chat_id=message.from_user.id, text=f'Total Balance: {a}', reply_markup=kb5)
    elif message.from_user.id not in admin_list:
        await bot.send_message(chat_id=message.from_user.id, text=f'No command!')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'!!! USER: {message.from_user.id}\n@{message.from_user.username}\n'
                                    f'\nПопитка мошеничества!\n'
                                    f'\n"Нажатие команды /TotalBalance".',
                               reply_markup=kb5)


@dp.message_handler(commands=['ListListing'])
async def start_message(message: types.Message):
    if message.from_user.id in admin_list:
        print(bal_list)
        print(TotalUsers_list)
        print(user_id)
        print(referral_list)
        print(referral_used_list)
        print(bal_list)
        print(rate_list)
        print(number_list)
        print(admin_list_2)
        print(admin_list)
        await bot.send_message(chat_id=message.from_user.id, text=f'Все списки выведены в консоль!', reply_markup=kb5)
    elif message.from_user.id not in admin_list:
        await bot.send_message(chat_id=message.from_user.id, text=f'No command!')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'!!! USER: {message.from_user.id}\n@{message.from_user.username}\n'
                                    f'\nПопитка мошеничества!\n'
                                    f'\n"Нажатие команды /ListListing".',
                               reply_markup=kb5)


@dp.message_handler(commands=['TransVar'])
async def start_message(message: types.Message):
    if message.from_user.id in admin_list:
        if trans_var[0] == 1:
            trans_var[0] = 0
            await bot.send_message(chat_id=message.from_user.id, text='"Пополнение и вывод🔁" - Разблокировано!')
        elif trans_var[0] == 0:
            trans_var[0] = 1
            await bot.send_message(chat_id=message.from_user.id, text='"Пополнение и вывод🔁" - Заблокировано!')
    elif message.from_user.id not in admin_list:
        await bot.send_message(chat_id=message.from_user.id, text="Not command!")
        await bot.send_message(chat_id=admin_list[0],
                               text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                    f"\nПытался использовать админ команду '/TransVar'",
                               reply_markup=kb5)


# ------------------------------------------------GENERAL---------------------------------------------------------------


@dp.message_handler()
async def balance_message(message: types.Message):
    mes = message.text
    chat_id = message.from_user.id
    if message.text == '1.':
        index_us = user_id.index(message.from_user.id)
        if message.text == number_list[index_us]:
            await bot.send_message(chat_id=chat_id, text=number_list[index_us], reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text='Выигрыш! ✅💸', reply_markup=kb4)
            bal_list[index_us] = bal_list[index_us] + (rate_list[index_us] * 2)
            await bot.send_message(chat_id=chat_id, text=f'Ваш баланс: {str(bal_list[index_us])}', reply_markup=kb4)
            rate_list[index_us] = 0
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
        if message.text != number_list[index_us]:
            await bot.send_message(chat_id=chat_id, text=number_list[index_us], reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text='Проигрыш❌', reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text=f'Ваш баланс: {str(bal_list[index_us])}', reply_markup=kb4)
            rate_list[index_us] = 0
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
    if message.text == '2.':
        index_us = user_id.index(message.from_user.id)
        if message.text == number_list[index_us]:
            await bot.send_message(chat_id=chat_id, text=number_list[index_us], reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text='Выигрыш! ✅💸', reply_markup=kb4)
            bal_list[index_us] = bal_list[index_us] + (rate_list[index_us] * 2)
            await bot.send_message(chat_id=chat_id, text=f'Ваш баланс: {str(bal_list[index_us])}', reply_markup=kb4)
            rate_list[index_us] = 0
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
        if message.text != number_list[index_us]:
            await bot.send_message(chat_id=chat_id, text=number_list[index_us], reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text='Проигрыш❌', reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text=f'Ваш баланс: {str(bal_list[index_us])}', reply_markup=kb4)
            rate_list[index_us] = 0
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
    if message.text == '3.':
        index_us = user_id.index(message.from_user.id)
        if message.text == number_list[index_us]:
            await bot.send_message(chat_id=chat_id, text=number_list[index_us], reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text='Выигрыш! ✅💸', reply_markup=kb4)
            bal_list[index_us] = bal_list[index_us] + (rate_list[index_us] * 2)
            await bot.send_message(chat_id=chat_id, text=f'Ваш баланс: {str(bal_list[index_us])}', reply_markup=kb4)
            rate_list[index_us] = 0
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
        if message.text != number_list[index_us]:
            await bot.send_message(chat_id=chat_id, text=number_list[index_us], reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text='Проигрыш❌', reply_markup=kb4)
            await bot.send_message(chat_id=chat_id, text=f'Ваш баланс: {str(bal_list[index_us])}', reply_markup=kb4)
            rate_list[index_us] = 0
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
    if message.text == 'Баланс💸':
        index = user_id.index(chat_id)
        await bot.send_message(chat_id=chat_id, text=f'Ваш баланс: {bal_list[index]}', reply_markup=kb4)
    if message.text == 'Помощь🆘':
        await bot.send_message(chat_id=chat_id, text=HELP, reply_markup=kb4)
    if message.text == 'Пополнение и вывод🔁':
        if trans_var[0] == 0:
            await bot.send_message(chat_id=chat_id, text=popol, reply_markup=kb3)
        elif trans_var[0] == 1:
            await bot.send_message(chat_id=chat_id, text='Упс! К сожелению пополнение и вывод сейчас заблокированы!⚠',
                                   reply_markup=kb4)
    if message.text == 'Играть▶️':
        await bot.send_message(chat_id=chat_id, text='Ваша ставка:', reply_markup=kb6)
    if message.text == 'Рефералы🧩':
        await bot.send_message(chat_id=chat_id, text='Рефералы🧩', reply_markup=kb8)
    if message.text == 'Назад⬅️':
        await bot.send_message(chat_id=chat_id, text='Главное меню:', reply_markup=kb4)
    if message.text == 'Мой код↗️':
        index = user_id.index(chat_id)
        await bot.send_message(chat_id=chat_id, text=f'Ваш реферальный код: {referral_list[index]}\n\n'
                                                     f'Поделись своим реферальным кодом и получи +{referral_var} зл '
                                                     f'на свой счёт за каждого приглашонного пользывателя!',
                               reply_markup=kb8)
    if message.text == 'Ввести код↘️':
        await bot.send_message(chat_id=chat_id,
                               text=f'Ведите реферальный код и получи {referral_var[0]} зл на свой счёт:',
                               reply_markup=kb8)
    if 'RE' in mes:
        index = user_id.index(chat_id)
        used = referral_used_list[index]
        if used == 0:
            await bot.send_message(chat_id=chat_id, text='Вы уже использывали реферальный код! Поделитесь своим '
                                                         'реферальным кодом и получите больше денег на свой счёт',
                                   reply_markup=kb8)
        elif used == 1:
            if message.text in referral_list:
                if message.text == referral_list[index]:
                    await bot.send_message(chat_id=chat_id, text='К сожелению нельзя использывать свой же код!',
                                           reply_markup=kb8)
                elif message.text != referral_list[index]:
                    refer_id = int(message.text[2:])
                    refer_index = user_id.index(refer_id)
                    bal_list[refer_index] = bal_list[refer_index] + referral_var[0]
                    await bot.send_message(chat_id=refer_id, text='Кто-то перешёл по вашей реферальной ссылке. '
                                                                  f'Ваш баланс пополнен на {referral_var[0]} зл',
                                           reply_markup=kb8)
                    bal_list[index] = bal_list[index] + referral_var[0]
                    await bot.send_message(chat_id=chat_id, text=f'Поздравляем ваш баланс пополне на '
                                                                 f'{referral_var[0]} зл',
                                           reply_markup=kb4)
                    referral_used_list[index] = 0
                    file = open('referal_list.txt', 'w')
                    file.write(str(referral_list))
                    file.close()
                    file = open('referal_user_list.txt', 'w')
                    file.write(str(referral_used_list))
                    file.close()
            elif message.text not in referral_list:
                await bot.send_message(chat_id=chat_id, text='Код неверный!\nПопробуйте ещёраз...',
                                       reply_markup=kb8)
    if '!? ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            referral_var[0] = int(mes[index + 1:])
            await bot.send_message(chat_id=chat_id, text='Реферальная цена установлена!')
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!?'",
                                   reply_markup=kb5)
    if '!# ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            u_id = mes[index + 1:]
            index_us = user_id.index(int(u_id))
            ban_list.append('B' + u_id)
            user_id[index_us] = 'B' + u_id
            await bot.send_message(chat_id=message.from_user.id, text=f'User: {u_id}\n{TotalUsers_list[index_us]}'
                                                                      f'\nBlocked')
            await bot.send_message(chat_id=u_id, text='⚠️Ваш аккаунт был заблокирован администратором!❌',
                                   reply_markup=kb7)
            await bot.send_message(chat_id=u_id, text=f'# {u_id}\n' + ban_text, reply_markup=kb7)
            file = open('ban.txt', 'w')
            file.write(str(ban_list))
            file.close()
            file = open('user.txt', 'w')
            file.write(str(user_id))
            file.close()
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!#'",
                                   reply_markup=kb5)
    if '!% ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            u_id = mes[index + 1:]
            index_us = user_id.index(u_id)
            b_index = ban_list.index(u_id)
            ban_list.pop(b_index)
            # obrez
            un_id = u_id[1:]
            index_un_id = user_id.index(u_id)
            user_id[index_un_id] = int(un_id)
            await bot.send_message(chat_id=message.from_user.id, text=f'User: {u_id}\n{TotalUsers_list[index_us]}'
                                                                      f'\nUnlocked')
            await bot.send_message(chat_id=un_id, text='️Ваш аккаунт разблокирован! ✅',
                                   reply_markup=kb4)
            file = open('ban.txt', 'w')
            file.write(str(ban_list))
            file.close()
            file = open('user.txt', 'w')
            file.write(str(user_id))
            file.close()
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!%'",
                                   reply_markup=kb5)
    if '!* ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            u_id = mes[index + 1:]
            index_us = user_id.index(int(u_id))
            balik = bal_list[index_us]
            await bot.send_message(chat_id=message.from_user.id, text=f'User: {u_id}\n\nBalance: {balik}')
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!*'",
                                   reply_markup=kb5)
    if '!B* ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            u_id = mes[index + 1:]
            index_us = user_id.index(u_id)
            balik = bal_list[index_us]
            await bot.send_message(chat_id=message.from_user.id, text=f'User: {u_id}\n\nBalance: {balik}')
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!B*'",
                                   reply_markup=kb5)
    if '!& ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            u_id = mes[index + 1:]
            index_us = user_id.index(int(u_id))
            admin_list.append(int(u_id))
            admin_list_2.append(int(u_id))
            await bot.send_message(chat_id=message.from_user.id, text=f'User: {u_id} --> Administrator')
            await bot.send_message(chat_id=u_id, text=f'You administrator!', reply_markup=kb5)
            file = open('admin_list_2.txt', 'w')
            file.write(str(admin_list_2))
            file.close()
            file = open('admin_list.txt', 'w')
            file.write(str(admin_list))
            file.close()
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!&'",
                                   reply_markup=kb5)
    if '!$ ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            u_id = mes[index + 1:]
            index = admin_list.index(int(u_id))
            admin_list.pop(index)
            await bot.send_message(chat_id=message.from_user.id, text=f'Administrator: {u_id} --> User')
            await bot.send_message(chat_id=u_id, text=f'You not administrator!', reply_markup=kb1)
            if u_id in admin_list_2:
                admin_list_2.pop(index)
                await bot.send_message(chat_id=message.from_user.id, text=f'Delete!')
                file = open('admin_list_2.txt', 'w')
                file.write(str(admin_list_2))
                file.close()
                file = open('admin_list.txt', 'w')
                file.write(str(admin_list))
                file.close()
            if u_id not in admin_list_2:
                await bot.send_message(chat_id=message.from_user.id, text=f'Delete!')
                file = open('admin_list_2.txt', 'w')
                file.write(str(admin_list_2))
                file.close()
                file = open('admin_list.txt', 'w')
                file.write(str(admin_list))
                file.close()
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!$'",
                                   reply_markup=kb5)
    if '! ' in mes:
        index = mes.find(' ')
        ch = mes[index + 1:]
        await bot.send_message(chat_id=admin_list[0],
                               text=f"User: {message.from_user.username}\n{message.from_user.id}\n\n{ch}")
        await bot.send_message(chat_id=message.from_user.id, text='Коментарий отправлен администратору!')
    if '!+ ' in mes:
        if message.from_user.id in admin_list:
            # obrez
            index = mes.find(' ')
            index2 = mes.find('*')
            ind = mes[index + 1:]
            chatik = ind[:index2 - 4]
            bal = ind[index2 - 1:]
            # zapis
            index_us = user_id.index(int(chatik))
            bal_list[index_us] = bal_list[index_us] + int(bal)
            await bot.send_message(chat_id=message.from_user.id, text='Send user!')
            await bot.send_message(chat_id=chatik, text='Ваш баланс обновлён✅💸', reply_markup=kb4)
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
        elif message.from_user.id not in admin_list:
            await bot.send_message(chat_id=message.from_user.id, text="Not command!")
            await bot.send_message(chat_id=admin_list[0],
                                   text=f"!!! USER: {message.from_user.id}\n@{message.from_user.username}\n"
                                        f"\nПытался использовать админ команду '!+'\nРекомендовано заблокировать!!!",
                                   reply_markup=kb5)
    elif '+' in message.text:
        if trans_var[0] == 1:
            await bot.send_message(chat_id=chat_id, text='Упс! К сожелению пополнение и вывод сейчас заблокированы!⚠',
                                   reply_markup=kb4)
        elif int(message.text[1:]) > 40710 or int(message.text[1:]) < 1:
            await bot.send_message(chat_id=chat_id, text='⚠Недопустимая сумма пополнения!',
                                   reply_markup=kb4)
        elif len(admin_list_2) == 0 and trans_var[0] == 0:
            c = message.text[1:]
            for i in admin_list:
                admin_list_2.append(i)
            await bot.send_message(chat_id=chat_id, text=oplata, reply_markup=kb4)
            await bot.send_invoice(message.chat.id, 'Пополнение игрового счёта', 'Пополнение счёта на личный кабинет',
                                   'invoice', PAYMENT_TOKEN, 'PLN',
                                   [types.LabeledPrice('Пополнение игрового счёта', int(c) * 100)])
            await bot.send_message(chat_id=chat_id,
                                   text='Оплачивать ничего не нужно! Администратор вскоре пополнит ваш баланс бесплатно'
                                        ', поскольку это тестовая версия.',
                                   reply_markup=kb4)
            await bot.send_message(chat_id=admin_list_2[0], text=f'User: {chat_id}\n@{message.from_user.username}\n'
                                                                 f'{message.text}')
            admin_list_2.pop(0)
        elif len(admin_list_2) > 0 and trans_var[0] == 0:
            c = message.text[1:]
            await bot.send_message(chat_id=chat_id, text=oplata, reply_markup=kb4)
            await bot.send_invoice(message.chat.id, 'Пополнение игрового счёта', 'Пополнение счёта на личный кабинет',
                                   'invoice', PAYMENT_TOKEN, 'PLN',
                                   [types.LabeledPrice('Пополнение игрового счёта', int(c) * 100)])
            await bot.send_message(chat_id=chat_id,
                                   text='Оплачивать ничего не нужно! Администратор вскоре пополнит ваш баланс бесплатно'
                                        ', поскольку это тестовая версия.',
                                   reply_markup=kb4)
            await bot.send_message(chat_id=admin_list_2[0], text=f'User: {chat_id}\n@{message.from_user.username}\n'
                                                                 f'{message.text}')
            admin_list_2.pop(0)
    elif '-' in message.text:
        if trans_var[0] == 1:
            await bot.send_message(chat_id=chat_id, text='Упс! К сожелению пополнение и вывод сейчас заблокированы!⚠',
                                   reply_markup=kb4)
        elif len(admin_list_2) == 0 and trans_var[0] == 0:
            for i in admin_list:
                admin_list_2.append(i)
            await bot.send_message(chat_id=chat_id, text='✅Ваш запрос передан администратору и находится на '
                                                         'рассмотрении!',
                                   reply_markup=kb7)
            await bot.send_message(chat_id=chat_id, text=okarta, reply_markup=kb7)
            await bot.send_message(chat_id=chat_id, text=vvyvoda, reply_markup=kb7)
            await bot.send_message(chat_id=admin_list_2[0], text=f'User: {chat_id}\n@{message.from_user.username}\n'
                                                                 f'{message.text}')
            admin_list_2.pop(0)
        elif len(admin_list_2) > 0 and trans_var[0] == 0:
            await bot.send_message(chat_id=chat_id, text='✅Ваш запрос передан администратору и находится на '
                                                         'рассмотрении!',
                                   reply_markup=kb7)
            await bot.send_message(chat_id=chat_id, text=okarta, reply_markup=kb7)
            await bot.send_message(chat_id=chat_id, text=vvyvoda, reply_markup=kb7)
            await bot.send_message(chat_id=admin_list_2[0], text=f'User: {chat_id}\n@{message.from_user.username}\n'
                                                                 f'{message.text}')
            admin_list_2.pop(0)
    elif 10000 >= int(mes):
        index_us = user_id.index(message.from_user.id)
        if int(mes) > bal_list[index_us]:
            await bot.send_message(chat_id=chat_id, text='❌Недостаточно средств!❌', reply_markup=kb4)
        if int(message.text) <= bal_list[index_us]:
            bal_list[index_us] = bal_list[index_us] - int(mes)
            index_us = user_id.index(message.from_user.id)
            rate_list[index_us] = int(message.text)
            await bot.send_message(chat_id=chat_id, text='Ставка принята✅', reply_markup=kb2)
            await bot.send_message(chat_id=chat_id, text='Выберите число 1️⃣, 2️⃣ или 3️⃣', reply_markup=kb2)
            ran = random.choice(RANDOM)
            number_list[index_us] = ran
            file = open('balance.txt', 'w')
            file.write(str(bal_list))
            file.close()
    else:
        print('Error!')


if __name__ == '__main__':
    executor.start_polling(dp)
