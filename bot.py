import requests
import os
from datetime import datetime
import json

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
        "content": f"{task}"
    }
    
    r = requests.post(WEBHOOK, json=payload)
    print(f"Статус: {r.status_code}")

if __name__ == "__main__":
    if not WEBHOOK:
        print("Ошибка: DISCORD_WEBHOOK не найден")
    else:
        tasks = load_tasks()
        task = get_today_task(tasks)
        send_to_discord(task)
