import random
from command_handlers import *

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

def generate_multiple_random_items(body_level):
    body_richness = random.randint(1,100)

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
    return random_items_collective