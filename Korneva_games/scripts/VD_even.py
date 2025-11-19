import random

def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0

def ask_question():
    """Генерирует вопрос и получает ответ пользователя."""
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    print(f"Question: {number}")
    user_answer = input("Your answer: ").strip().lower()
    return user_answer, correct_answer

def main():
    print("Welcome to the VD-games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_count = 0
    while correct_count < 3:
        user_answer, correct_answer = ask_question()

        if user_answer not in ("yes", "no"):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
