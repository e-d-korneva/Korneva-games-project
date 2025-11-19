import random

DESCRIPTION = "What number is missing in the progression?"

def get_element(start, step, index):
    return start + index * step

def _generate_progression(start, step, length):
    return [get_element(start, step, i) for i in range(length)]

def generate_round():
    start = random.randint(1, 30)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    progression = _generate_progression(start, step, length)

    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer
