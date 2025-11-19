import random

DESCRIPTION = "What is the result of the expression?"

_OPERATORS = ["+", "-", "*"]

def _calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b

def generate_round():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(_OPERATORS)
    question = f"{a} {op} {b}"
    correct_answer = str(_calculate(a, b, op))
    return question, correct_answer
