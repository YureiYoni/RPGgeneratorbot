import logging

from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from keyboards import *

from config import TOKEN, CHANNEL_ID

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)


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

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

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