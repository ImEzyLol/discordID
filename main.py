import requests
import datetime

token = '' #bot token to interact with API
user_id = '1090393830047617034' #your user ID

def fetch_user(id):
    url = f'https://discord.com/api/v9/users/{id}'
    headers = {
        'Authorization': f'Bot {token}'
    }
    response = requests.get(url, headers=headers)
    if not response.ok:
        raise Exception(f'Error status code: {response.status_code}')
    return response.json()


try:
    #will tell you: join date, and other info the can be retreived from API from User ID, animated pfps start with a_, whilst normal pngs dont
    user_data = fetch_user(user_id)
    snowflake_id = user_data['id']
    creation_timestamp = ((int(snowflake_id) >> 22) + 1420070400000) / 1000
    creation_date = datetime.datetime.fromtimestamp(creation_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print(f"User's creation date: {creation_date}")
    user_data = fetch_user(user_id)
    print(user_data)
except Exception as e:
    print(f'Error fetching user: {e}')
