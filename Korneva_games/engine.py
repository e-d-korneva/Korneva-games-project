def run_game(game_module):
    print("Welcome to the Korneva games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(game_module.DESCRIPTION)

    for _ in range(3):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
