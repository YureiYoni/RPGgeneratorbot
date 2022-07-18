from aiogram import types

delete_kb = types.ReplyKeyboardRemove()

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