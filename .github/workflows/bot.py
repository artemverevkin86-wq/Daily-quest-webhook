import requests
import json
from datetime import datetime
import os

WEBHOOK = os.environ.get('DISCORD_WEBHOOK')

def load_tasks():
    with open('tasks.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['tasks']

def get_today_task(tasks):
    day = datetime.now().day
    index = (day - 1) % len(tasks)
    return tasks[index]

def send_to_discord(task):
    today = datetime.now().strftime('%d.%m.%Y')
    payload = {
        "username": "Задания дня",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/1998/1998592.png",
        "embeds": [{
            "title": f"📅 Задание на {today}",
            "description": task,
            "color": 0x5865F2
        }]
    }
    r = requests.post(WEBHOOK, json=payload)
    print('OK' if r.status_code == 204 else f'Error {r.status_code}')

if __name__ == "__main__":
    if not WEBHOOK:
        print("Нет DISCORD_WEBHOOK")
    else:
        tasks = load_tasks()
        task = get_today_task(tasks)
        send_to_discord(task)
