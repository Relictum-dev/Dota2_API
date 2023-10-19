import requests
player_id = 90313958

player_url = f'https://api.opendota.com/api/players/{player_id}'


response = requests.get(player_url)
            
            
            # Проверяем успешность запроса
if response.status_code == 200:
                
                # Парсим JSON-ответ и отправляем ID последнего матча пользователю
    data = response.json()
    if data:
        mmr = data['mmr_estimate']['estimate']
        print(f'ММР:{mmr}')