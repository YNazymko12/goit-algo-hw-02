from collections import deque


def is_palindrome(input_string: str) -> bool:
    # Нормалізація рядка: перетворення в нижній регістр та видалення пробілів
    normalized_str = ''.join(input_string.lower().split())

    # Створення двосторонньої черги
    deq = deque(normalized_str)

    # Порівняння символів з обох кінців черги
    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    return True


# Приклад використання
print(is_palindrome("Pan ap"))  # Output: True
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("This is not a palindrome"))  # Output: False