import logging
import random

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

from config import TOKEN, CHANNEL_ID

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    no_state = State()

    startchoice = State()

    character = State()
    shop = State()
    loot = State()  
    encounter = State()
    room = State()  
    output = State() 

    gen_character = State()
    gen_shop = State()
    gen_loot_lvl = State()
    gen_loot = State()
    gen_encounter = State()
    gen_room = State()  

delete_kb = types.ReplyKeyboardRemove()

item_mundane = "Обыденное"
item_useful = "Полезное"
item_professional = "Профессиональное"
item_magical = "Магическое"
item_highly_magical = "Высокомагическое"
item_unique = "Уникальное"

def readlff(filename):
    with open(filename) as lr:
        lines = lr.readlines()

    random_line = random.choice(lines).strip() 
    return random_line

def generate_random_item(body_level):

    r_rarity = random.randint(1,100)

    if body_level == 1:
        if r_rarity <= 65:
            generated_item_rarity = item_mundane
        elif 90 >= r_rarity >= 66:
            generated_item_rarity = item_useful
        elif 100 >= r_rarity >= 91:
            generated_item_rarity = item_professional
    elif body_level == 2:
        if r_rarity <= 50:
            generated_item_rarity = item_mundane
        elif 80 >= r_rarity >= 51:
            generated_item_rarity = item_useful
        elif 95 >= r_rarity >= 81:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 96:
            generated_item_rarity = item_magical
    elif body_level == 3:
        if r_rarity <= 40:
            generated_item_rarity = item_mundane
        elif 75 >= r_rarity >= 41:
            generated_item_rarity = item_useful
        elif 94 >= r_rarity >= 76:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 95:
            generated_item_rarity = item_magical
    elif body_level == 4:
        if r_rarity <= 40:
            generated_item_rarity = item_mundane
        elif 75 >= r_rarity >= 41:
            generated_item_rarity = item_useful
        elif 92 >= r_rarity >= 76:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 93:
            generated_item_rarity = item_magical
    elif body_level == 5:
        if r_rarity <= 40:
            generated_item_rarity = item_mundane
        elif 75 >= r_rarity >= 41:
            generated_item_rarity = item_useful
        elif 94 >= r_rarity >= 76:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 95:
            generated_item_rarity = item_magical
    elif body_level == 6:
        if r_rarity <= 35:
            generated_item_rarity = item_mundane
        elif 70 >= r_rarity >= 36:
            generated_item_rarity = item_useful
        elif 90 >= r_rarity >= 71:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 91:
            generated_item_rarity = item_magical
    elif body_level == 7:
        if r_rarity <= 30:
            generated_item_rarity = item_mundane
        elif 65 >= r_rarity >= 31:
            generated_item_rarity = item_useful
        elif 87 >= r_rarity >= 66:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 87:
            generated_item_rarity = item_magical
    elif body_level == 8:
        if r_rarity <= 20:
            generated_item_rarity = item_mundane
        elif 55 >= r_rarity >= 21:
            generated_item_rarity = item_useful
        elif 82 >= r_rarity >= 56:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 83:
            generated_item_rarity = item_magical
    elif body_level == 9:
        if r_rarity <= 20:
            generated_item_rarity = item_mundane
        elif 49 >= r_rarity >= 21:
            generated_item_rarity = item_useful
        elif 74 >= r_rarity >= 50:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 75:
            generated_item_rarity = item_magical
    elif body_level == 10:
        if r_rarity <= 20:
            generated_item_rarity = item_mundane
        elif 42 >= r_rarity >= 21:
            generated_item_rarity = item_useful
        elif 69 >= r_rarity >= 43:
            generated_item_rarity = item_professional
        elif 100 >= r_rarity >= 70:
            generated_item_rarity = item_magical
    elif 15 >= body_level >= 11:
        if r_rarity <= 10:
            generated_item_rarity = item_mundane
        elif 30 >= r_rarity >= 11:
            generated_item_rarity = item_useful
        elif 60 >= r_rarity >= 31:
            generated_item_rarity = item_professional
        elif 95 >= r_rarity >= 61:
            generated_item_rarity = item_magical
        elif 100 >= r_rarity >= 96:
            generated_item_rarity = item_highly_magical
    elif body_level >= 16:
        if r_rarity <= 10:
            generated_item_rarity = item_mundane
        elif 30 >= r_rarity >= 11:
            generated_item_rarity = item_useful
        elif 60 >= r_rarity >= 31:
            generated_item_rarity = item_professional
        elif 89 >= r_rarity >= 61:
            generated_item_rarity = item_magical
        elif 100 >= r_rarity >= 90:
            generated_item_rarity = item_highly_magical

    item_rarity = generated_item_rarity

    if item_rarity == item_mundane:
        random_item = readlff("mundane_items.txt")
    elif item_rarity == item_useful:
        random_item = readlff("useful_items.txt")
    elif item_rarity == item_professional:
        random_item = readlff("professional_items.txt")
    elif item_rarity == item_magical:
        random_item = readlff("magical_items.txt")
    elif item_rarity == item_highly_magical:
        random_item = readlff("highly_magical_items.txt")
    return random_item

def generate_weapon_property():
    weapon_property = readlff("weapon_properties.txt")
    return weapon_property

def generate_weapon_magical_effect():
    weapon_magical_effect = readlff("weapon_magical_effects.txt")
    return weapon_magical_effect

def generate_random_weapon():
    item_weapon = readlff("weapons.txt")
    return item_weapon

def generate_simple_weapon():
    item_weapon = readlff("weapons_simple.txt")
    return item_weapon

def generate_martial_weapon():
    item_weapon = readlff("weapons_martial.txt")
    return item_weapon

def generate_exotic_weapon():
    item_weapon = readlff("weapons_exotic.txt")
    return item_weapon

def generate_firearm_weapon():
    item_weapon = readlff("weapons_firearms.txt")
    return item_weapon

def generate_random_armor():
    item_armor = readlff("armor.txt")
    return item_armor

def generate_light_armor():
    item_armor = readlff("armor_light.txt")
    return item_armor

def generate_medium_armor():
    item_armor = readlff("armor_medium.txt")
    return item_armor

def generate_heavy_armor():
    item_armor = readlff("armor_heavy.txt")
    return item_armor

def generate_shield():
    item_shield = readlff("shields.txt")
    return item_shield
    


async def bot_restart():
    await bot.send_message(CHANNEL_ID, "Уррр! Я перрезагррузился! (@RavenFriend_RP_Bot). \n\n⭐Чудного вам дня!⭐")

new_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
new_kb.add("Персонаж", "Магазин", "Лут", "Энкаунтер", "Комната", "Отмена")

again_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
again_kb.add("Сгенерировать", "В начало", "Отмена")

new_character = types.ReplyKeyboardMarkup(resize_keyboard=True)
new_character.add("Бедняк", "Горожанин", "Торговец", "Боец", "Военный", "Человек веры", "Маг", "В начало", "Отмена")

new_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
new_shop.add("Алхимия", "Продуктовый", "Оружейник", "Бронник", "Случайная лавка", "Магия", "Книжный", "Ведьмовство", "Черный рынок", "В начало", "Отмена")

new_loot = types.ReplyKeyboardMarkup(resize_keyboard=True)
new_loot.add("Осмотр тела", "Осмотр сундука", "Осмотр тайника", "Стандартная магическая вещь", "Особая магическая вещь", "В начало", "Отмена")

new_encounter = types.ReplyKeyboardMarkup(resize_keyboard=True)
new_encounter.add("Подземелье", "Город", "Лес", "Джунгли", "Руины", "Болото", "Под водой", "Нежить", "Разбойники", "Гуманоиды", "Странное", "В начало", "Отмена")

new_room = types.ReplyKeyboardMarkup(resize_keyboard=True)
new_room.add("Подземелье", "Поместье", "Руины", "Деревенский домик", "В начало", "Отмена")

loot_body_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
loot_body_kb.add("Обычный враг", "Элитный враг", "Босс", "В начало", "Отмена")

loot_chest_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
loot_chest_kb.add("Жилой сундук", "Шкаф с вещами", "Драгоценный сундук", "В начало", "Отмена")

loot_secret_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
loot_secret_kb.add("Схрон", "Элитный враг", "Босс", "В начало", "Отмена")

standart_magical_item_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
standart_magical_item_kb.add("Обычный враг", "Элитный враг", "Босс", "В начало", "Отмена")

unique_magical_item_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
unique_magical_item_kb.add("Обычный враг", "Элитный враг", "Босс", "В начало", "Отмена")


@dp.message_handler(state='*', commands='Отмена')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Отменено. Нажмите или напишите /start, чтобы начать заново.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state='*', commands='В начало')
@dp.message_handler(Text(equals='В начало', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await Form.startchoice.set()
    await message.answer('Врремя выбиррать:', reply_markup=new_kb)

@dp.message_handler(state='*', commands='/creator')
@dp.message_handler(Text(equals='/creator', ignore_case=True), state='*')
async def creator_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Святые пёрррышки! Нашелся умник, который ррраскопал команду [/creator]?! Мой создатель - @stygianyurei, он же Юррра. Чё каво, сучки?!\n\n/start?', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state='*', commands='/help')
@dp.message_handler(Text(equals='/help', ignore_case=True), state='*')
async def help_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Я не буду вам помогать, я же ворронья знать! УХУХУХУХУХУХУХ!!! *неразборчивый клёкот* Бууууфффуууууу!!!!! Хотя... ладно. Но только сегодня! Если что-то не так, пиши @stygianyurei. А пока давай, жми /start, и пошли генеррррить как есть. *бурчит тихо* ...Неблагодаррные...', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands='start')
async def p_greeting(message: types.Message):
    
    await Form.startchoice.set()
    await message.answer("Врремя выбирррать:", reply_markup=new_kb)

@dp.message_handler(state=Form.startchoice)
async def p_startchoice(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['start_choice'] = message.text

    if data['start_choice'] == "Персонаж":
        await Form.character.set()
        await message.answer("Нужно выбррать тип перррсонажа", reply_markup=new_character)
    elif data['start_choice'] == "Магазин":
        await Form.shop.set()
        await message.answer("Нужно выбррать тип магазина", reply_markup=new_shop)
    elif data['start_choice'] == "Лут":
        await Form.loot.set()
        await message.answer("Нужно выбррать тип лута", reply_markup=new_loot)
    elif data['start_choice'] == "Энкаунтер":
        await Form.encounter.set()
        await message.answer("Нужно выбррать тип энкаунтеррра", reply_markup=new_encounter)
    elif data['start_choice'] == "Комната":
        await Form.room.set()
        await message.answer("Нужно выбррать тип комнаты", reply_markup=new_room)
    else:
        await state.finish()
        await message.answer('Дубина! Такого варррианта не было! Пиши /start, чтобы начать заново.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=Form.character)
async def p_character(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['character_choice'] = message.text

    if data['character_choice'] == "Бедняк":
        await message.answer("Вот твой бедняк", reply_markup=again_kb)
        await Form.gen_character.set()
    elif data['character_choice'] == "Горожанин":
        await message.answer("Вот твой горожанин", reply_markup=again_kb)
        await Form.gen_character.set()
    elif data['character_choice'] == "Торговец":
        await message.answer("Вот твой торговец", reply_markup=again_kb)
        await Form.gen_character.set()
    elif data['character_choice'] == "Боец":
        await message.answer("Вот твой боец", reply_markup=again_kb)
        await Form.gen_character.set()
    elif data['character_choice'] == "Военный":
        await message.answer("Вот твой военный", reply_markup=again_kb)
        await Form.gen_character.set()
    elif data['character_choice'] == "Человек веры":
        await message.answer("Вот твой человек веррры", reply_markup=again_kb)
        await Form.gen_character.set()
    elif data['character_choice'] == "Маг":
        await message.answer("Вот твой маг", reply_markup=again_kb)
        await Form.gen_character.set()
    else:
        await state.finish()
        await message.answer('Эх ты! Не было такого выборра. Пиши /start, чтобы начать заново.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=Form.gen_character)
async def g_character(message: types.Message, state: FSMContext):

    r_sex = random.randint(0,1)
    if r_sex == 0:
        c_sex = "Женщина"
    elif r_sex == 1:
        c_sex = "Мужчина"

    def generate_character():

        r_sex = random.randint(0,1)
        if r_sex == 0:
            c_sex = "Женщина"
        elif r_sex == 1:
            c_sex = "Мужчина"
        
        r_race = random.randint(1,12)
        if r_race <= 6:
            race_type = "Human"
            c_race = readlff("human.txt")
        elif 9 >= r_race > 6:
            race_type = "Common"
            c_race = readlff("common_races.txt")
        elif 11 >= r_race > 9:
            race_type = "Unusual"
            c_race = readlff("unusual_races.txt")
        elif r_race == 12:
            race_type = "Rare"
            c_race = readlff("rare_races.txt")
        
        if c_race == "Человек":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Дворф":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Дворф":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Эльф":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Гном":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Полурослик":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Полуэльф":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Полуорк":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Аасимар":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Бистфолк":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Дампир":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Дроу":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Фэтчлинг":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Тифлинг":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Гоблин":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Орк":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Хобгоблин":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Ифрит":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Кобольд":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Орид":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Сильф":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Тэнгу":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Ундин":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Грипли":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Китсунэ":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Мерфолк":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Нагажи":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Самсаран":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Стрикс":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Сули":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Свирфнеблин":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Ванара":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Ваянг":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        elif c_race == "Вишканя":
            if c_sex == "Мужчина":
                c_name = readlff("character_human_male_name.txt")
                c_lname = readlff("character_human_last_name.txt")
            elif c_sex == "Женщина":
                c_name = readlff("character_human_female_name.txt")
                c_lname = readlff("character_human_last_name.txt")
        ready_character = "Имя: " + c_name + " " + c_lname + "\n\nПол: " + c_sex + "\n\nРаса: " + c_race
        return ready_character

    if message.text == "Сгенерировать":
        await message.answer(generate_character())

@dp.message_handler(state=Form.shop)
async def p_shop(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['shop_choice'] = message.text

    if data['shop_choice'] == "Алхимия":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    elif data['shop_choice'] == "Продуктовый":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    elif data['shop_choice'] == "Оружейник":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    elif data['shop_choice'] == "Бронник": 
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    elif data['shop_choice'] == "Случайная лавка":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    elif data['shop_choice'] == "Магия":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    elif data['shop_choice'] == "Книжный":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.next()
    elif data['shop_choice'] == "Ведьмовство":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    elif data['shop_choice'] == "Черный рынок": 
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_shop.set()
    else:
        await state.finish()
        await message.answer('Эх ты! Не было такого выборра. Пиши /start, чтобы начать заново.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=Form.loot)
async def p_loot(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['loot_choice'] = message.text

    if data['loot_choice'] == "Осмотр тела":
        await message.answer("Нужно выбрррать урровень тела (1-20)", reply_markup=delete_kb)
        await Form.gen_loot_lvl.set()
    elif data['loot_choice'] == "Осмотр сундука":
        await message.answer("Получите", reply_markup=loot_chest_kb)
        await Form.gen_loot_lvl.set()
    elif data['loot_choice'] == "Осмотр тайника":
        await message.answer("Получите", reply_markup=loot_secret_kb)
        await Form.gen_loot_lvl.set()
    elif data['loot_choice'] == "Стандартная магическая вещь":
        await message.answer("Получите", reply_markup=standart_magical_item_kb)
        await Form.gen_loot_lvl.set()
    elif data['loot_choice'] == "Особая магическая вещь":
        await message.answer("Получите", reply_markup=unique_magical_item_kb)
        await Form.gen_loot_lvl.set()
    else:
        await state.finish()
        await message.answer('Эх ты! Не было такого выборра. Пиши /start, чтобы начать заново.', reply_markup=types.ReplyKeyboardRemove())
    
@dp.message_handler(state=Form.gen_loot_lvl)
async def g_loot_lvl(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['loot_level'] = message.text
    
    await message.answer("Теперрь выберрри тип тела", reply_markup=loot_body_kb)
    await Form.gen_loot.set()

@dp.message_handler(state=Form.gen_loot)
async def g_loot(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['loot_body_choice'] = message.text

    body_richness = random.randint(1,100)

    body_level = int(data['loot_level'])

    very_small_item_ammount = random.randint(0,2)

    small_item_ammount = random.randint(2,4)

    average_item_ammount = random.randint(4,7)

    big_item_ammount = random.randint(7,10)

    very_big_item_ammount = random.randint(10,13)

    hoarder_item_ammount = random.randint(13,25)

    if body_richness <= 5:
        item_ammount = very_small_item_ammount
    elif 6 <= body_richness <= 30:
        item_ammount = small_item_ammount
    elif 31 <= body_richness <= 80:
        item_ammount = average_item_ammount
    elif 81 <= body_richness <= 90:
        item_ammount = big_item_ammount
    elif 91 <= body_richness <= 98:
        item_ammount = very_big_item_ammount
    elif 99 <= body_richness <= 100:  
        item_ammount = hoarder_item_ammount  

    random_items_collective = ""

    for i in range(1,item_ammount):
        current_item = generate_random_item(body_level)
        i_number = str(i)
        random_items_collective += "\n" + i_number + ") " + current_item

    await message.answer(random_items_collective, reply_markup=again_kb)

@dp.message_handler(state=Form.encounter)
async def p_encounter(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['encounter_choice'] = message.text

    if data['shop_choice'] == "Подземелье":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Город":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Лес":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Джунгли":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Руины":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Болото":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Под водой":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Нежить":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Разбойники":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Гуманоиды":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    elif data['encounter_choice'] == "Странное":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_encounter.set()
    else:
        await state.finish()
        await message.answer('Эх ты! Не было такого выборра. Пиши /start, чтобы начать заново.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.room)
async def p_room(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['room_choice'] = message.text

    if data['character_choice'] == "Подземелье":
        await message.answer("Получите", reply_markup=again_kb)
        await Form.gen_room.set()
    elif data['character_choice'] == "Поместье":
        await message.answer("Получите", reply_markup=again_kb)
        Form.gen_room.set()
    elif data['character_choice'] == "Руины":
        await message.answer("Получите", reply_markup=again_kb)
        Form.gen_room.set()
    elif data['character_choice'] == "Деревенский домик":
        await message.answer("Получите", reply_markup=again_kb)
        Form.gen_room.set()
    else:
        await state.finish()
        await message.answer('Эх ты! Не было такого выборра. Пиши /start, чтобы начать заново.', reply_markup=types.ReplyKeyboardRemove())

if __name__ == '__main__':
    executor.start(dp, bot_restart())
    executor.start_polling(dp, skip_updates=True)