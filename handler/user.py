from aiogram import types
from create import dp, Dispatcher
from aiogram.dispatcher.filters import Text
import stratz
import requests
from config.admin import user_list, player_list
from config.settings import Stratz_key
import asyncio
import datetime
from handler.defenition import Game_Modes, Heroes_pool, mmr_rank


#------------------Params for stratz_api-------------------#
header = {'Authorization':f'Bearer {Stratz_key}'}



#--------------------------End------------------------------#

#-----------------------Handler start-----------------------#
@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await message.answer('Для начала работы прошу ознакомиться с правилами использования: \n \n'
    '1) Для просмотра статистики вы должны иметь аккаунт на opendota.com и stratz.com\n'
    '2) Аккаунты opendota.com и stratz.com должны быть публичными \n' 
    '3) Получить доступ к боту у @Relictum017 \n \n' 
    'Если потребуется помощь, напишите команду /help')

    
#---------------------------End-----------------------------#

#----------------------User Selection-----------------------#



#---------------------------End-----------------------------#
#----------------------Global variables---------------------#
LAST_MATCH_ID = None
is_processing = True
users_states = {}
users_mmr = {}
#---------------------------End-----------------------------#



#-----------------Handler notification_on-------------------# 
@dp.message_handler(commands=['notification_on'])
async def check_match_status(message: types.Message):

    user_id = message.from_user.id
    if user_id == user_list['user_1']:
        player_id = player_list['player_1']
        

    if user_id not in users_states or not users_states[user_id]:
    
        users_states[user_id] = True

        global user_name

        await message.answer('Уведомления включены!\n\n'
                        'Теперь вы будете получать статистику после каждого сыгранного матча')
        
        
        global LAST_MATCH_ID

        global is_processing
        is_processing = True
        n = 0
        while is_processing:
            

            url = f'https://api.opendota.com/api/players/{player_id}/matches?limit=1'
            player_url = f'https://api.opendota.com/api/players/{player_id}'
        
        # Отправляем GET-запрос к API OpenDota
            response = requests.get(url)
            response_player = requests.get(player_url)

            
            # Проверяем успешность запроса
            if response.status_code == 200:
                
                # Парсим JSON-ответ и отправляем ID последнего матча пользователю
                data = response.json()
                data_player = response_player.json()

                if data:
                    last_match_id = data[0]['match_id']
                    

                    if LAST_MATCH_ID != last_match_id:
                        LAST_MATCH_ID = last_match_id
                    
                        duration = data[0]['duration']
                        duration = str(datetime.timedelta(seconds=duration))
                        hero = data[0]['hero_id']
                        kill = data[0]['kills']
                        death = data[0]['deaths']
                        assist = data[0]['assists']
                        gamemode_code = data[0]['game_mode']
                        result = data[0]['radiant_win']

                        mmr = data_player['mmr_estimate']['estimate']
                        user_name = data_player['profile']['personaname']
                        game_mode_name = Game_Modes.get(gamemode_code,'Unknown')

                        hero_name = Heroes_pool.get(hero)
                        player_rank = mmr
                        player_rank = mmr_rank(player_rank)

                        users_mmr[user_name] = mmr

                        
                        
                        

                        match_results = []
                        for match in data:
                            if result and match['player_slot'] < 128 or not result and match['player_slot'] >= 128:
                                result = 'Победа'
                                match_results.append("Победа")
                            else:
                                result = 'Поражение'
                                match_results.append('Поражение')
                        
                        

                        await message.answer(
                        f'Ваша статистика, {user_name}\n \n'
                        f'Режим игры: {game_mode_name}\n'
                        f'Результат: {result}\n'
                        f'Герой: {hero_name}\n'
                        f'У/С/П: {kill}/{death}/{assist}\n\n'
                        f'Длительность: {duration}\n'
                        f'MMR: {mmr} ({player_rank})\n'
                        )
                        
                        
                        
                    else:
                        
                        time_now = datetime.datetime.now()
                        format_time = time_now.strftime('%H:%M:%S')
                        print(
                        f'---------Request {n}---------\n'
                        'Не найдено новых матчей\n'
                        f'ID игрока: {player_id}\n'
                        f'Steam аккаунт: {user_name}\n'
                        f'Время запроса: {format_time}\n'
                        '---------------------------')
                        n = n+1

            else:
                await message.answer(f'Ошибка при получении данных: {response.status_code}')
    
            await asyncio.sleep(10)
    else:
        await message.answer('Вы уже получаете уведомления о новых матчах!\n \n'
                    'Чтобы выключить уведомления, выполните - /notification_off')



            
                    


        
        
#--------------------------End--------------------------#

#----------------Handler notification_off---------------#
@dp.message_handler(commands=['notification_off'])
async def stop_notificate(message: types.Message):

    global is_processing
    is_processing = False
    users_states.clear()

    await message.answer('Уведомления выключены \n\n'
    'Если захотите получать информацию о завершённых матчах, выполните команду:\n'
    '/notification_on')
#--------------------------End--------------------------#

#----------------------Handler help---------------------#
@dp.message_handler(commands=['help'])
async def help(message: types.Message):

        await message.answer('Список доступных вам команд:\n \n'
        '/notification_on - Включить уведомления о статистике завершённых матчей\n'
        '/notification_off - Выключить уведомления о статистике матчей\n'
        '/profile - Предоставляет статистику вашего профиля\n'
        )
#---------------------------End-------------------------#

#---------------------Handler profile-------------------#
@dp.message_handler(commands=['profile'])
async def profile(message:types.Message):

    user_id = message.from_user.id
    if user_id == user_list['user_1']:
        player_id = player_list['player_1']

    stratz_url = f'https://api.stratz.com/api/v1/Player/{player_id}'
    match_summary = f'https://api.stratz.com/api/v1/Player/{player_id}/summary'

    response = requests.get(stratz_url, headers=header)
    response_summary = requests.get(match_summary, headers=header)
    
    
    data = response.json()
    data_summary = response_summary.json()

    user_name = data['steamAccount']['name']
    is_smuft = data['steamAccount']['smurfFlag']
    dota_plus = data['steamAccount']['isDotaPlusSubscriber']
    battlepass = data['battlePass'][0]['level']
    alltime_wins = data_summary['allTime']['matches']['win']
    alltime_matches = data_summary['allTime']['matches']['matchCount']
    alltime_loses = alltime_matches-alltime_wins
    games_in_month = data_summary['oneMonth']['matches']['matchCount']
    wins_in_month = data_summary['oneMonth']['matches']['win']
    lose_in_month = games_in_month - wins_in_month


    if dota_plus == True:
        dota_plus = 'Есть'
    else:
        dota_plus = 'Нет'

    if is_smuft == 0:
        is_smuft = 'Нет'

    if is_smuft == 1:
        is_smuft = 'Да'

    await message.answer(
    f'Имя игрока: {user_name}\n'
    f'Уровень боевого пропуска: {battlepass}\n'
    f'Подписка Plus: {dota_plus}\n'
    f'Смурф: {is_smuft}\n\n'
    'Статистика за всё время:\n'
    f'Всего игр: {alltime_matches}\n'
    f'Побед: {alltime_wins}\n'
    f'Поражений: {alltime_loses}\n\n'
    'Статистика за последний месяц:\n'
    f'Всего игр: {games_in_month}\n'
    f'Побед: {wins_in_month}\n'
    f'Поражений: {lose_in_month}')


#---------------------------End-------------------------#



 


        







#--------------------Register_handlers------------------#
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(stop_notificate, commands=['notification_off'])
    dp.register_message_handler(check_match_status, commands=['notification_on'])
    dp.register_message_handler(start, commands = ['start'])
    dp.register_message_handler(help, commands= ['help'])

#--------------------------End--------------------------#