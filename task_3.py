def check_brackets(sequence):
    # Словник для відповідних пар дужок
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Стек для зберігання відкритих дужок
    stack = []

    for char in sequence:
        if char in bracket_pairs.values():
            # Якщо це відкриваюча дужка, додаємо її в стек
            stack.append(char)
        elif char in bracket_pairs.keys():
            # Якщо це закриваюча дужка
            if stack == [] or bracket_pairs[char] != stack.pop():
                return "Несиметрично"
        
    
    # Якщо стек порожній після обробки всіх символів, дужки симетричні
    return "Симетрично" if stack == [] else "Несиметрично"

# Тест
test_cases = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for test in test_cases:
    print(f"{test}: {check_brackets(test)}")