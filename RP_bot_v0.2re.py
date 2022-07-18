import random

from keyboards import *
from rp_generators import *
from command_handlers import *

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor 

async def bot_restart():
    await bot.send_message(CHANNEL_ID, "Уррр! Я перрезагррузился! (@RavenFriend_RP_Bot). \n\n⭐Чудного вам дня!⭐")

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

    inp_body_level = int(data['loot_level'])

    await message.answer(generate_multiple_random_items(inp_body_level), reply_markup=again_kb)

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