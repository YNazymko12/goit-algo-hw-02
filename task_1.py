from queue import Queue
import random
import time

# Створення черги заявок
request_queue = Queue()

# Функція генерації нових заявок
def generate_request():
    # Створення нових заявок з унікальним номером
    request_id = random.randint(1, 1000)
    # Додавання заявок до черги
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги")

# Функція обробки заявок
def process_request():
    # Якщо черга не пуста:
    if not request_queue.empty():
        #Видалення заявки з черги
        request_id = request_queue.get()
        #Обробка заявки
        print(f"Заявка {request_id} оброблена")
    else:
        print("Черга порожня")

try:
    while True:
        generate_request()
        process_request()
        # Імітація деякої затримки між операціями
        time.sleep(1)

except KeyboardInterrupt:
    print("Програма завершена.")

    