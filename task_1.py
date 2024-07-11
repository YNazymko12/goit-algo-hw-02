import queue
import time
import random

# Функція генерації нових заявок
def generate_request(request_queue, request_id):
    priority = random.randint(1, 10)  # Пріоритет заявки (1 - найвищий пріоритет)
    request_data = f"Заявка №{request_id} з пріоритетом {priority}"
    request_queue.put((priority, request_data))
    print(f"Сгенеровано нову заявку: {request_data}")

# Функція обробки заявок
def process_request(request_queue):
    if not request_queue.empty():
        priority, request_data = request_queue.get()
        print(f"Обробка заявки: {request_data}")
        # Симуляція затримки обробки
        time.sleep(random.uniform(0.5, 2.0))
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    request_queue = queue.PriorityQueue()
    request_id = 0

    try:
        while True:
            # Генерування нових заявок з імовірністю 50%
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)

            # Обробка заявок з імовірністю 50%
            if random.choice([True, False]):
                process_request(request_queue)
            
            # Затримка між ітераціями
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем")

if __name__ == "__main__":
    main()

