import requests
import os
from datetime import datetime

WEBHOOK = os.environ.get('DISCORD_WEBHOOK')

def load_tasks():
    with open('tasks.json', 'r', encoding='utf-8') as f:
        import json
        data = json.load(f)
    return data['tasks']

def get_today_task(tasks):
    day = datetime.now().day
    index = (day - 1) % len(tasks)
    return tasks[index]

def send_to_discord(task):
    today = datetime.now().strftime('%d.%m.%Y')
    
    # Здесь НЕТ имени вебхука и НЕТ аватарки — только чистое сообщение
    payload = {
        "content": f"📅 **Задание на {today}**\n\n{task}"
    }
    
    r = requests.post(WEBHOOK, json=payload)
    print(f"Статус: {r.status_code}")
    if r.status_code == 204:
        print("✅ Отправлено!")
    else:
        print(f"❌ Ошибка: {r.text}")

if __name__ == "__main__":
    if not WEBHOOK:
        print("Ошибка: DISCORD_WEBHOOK не найден")
    else:
        tasks = load_tasks()
        task = get_today_task(tasks)
        send_to_discord(task)
