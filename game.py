import random

def check(computer, user):

    if computer == user:
        return 0

    if computer == 0 and user == 1:
        return -1

    if computer == 1 and user == 2:
        return -1

    if computer == 2 and user == 0:
        return -1

    return 1


def play(user):

    computer = random.randint(0, 2)

    score = check(computer, user)

    choices = ["Snake", "Water", "Gun"]

    if score == 0:
        result = "🤝 It's a Draw!"

    elif score == -1:
        result = "💻 Computer Wins!"

    else:
        result = "🎉 You Win!"

    return {
        "user": choices[user],
        "computer": choices[computer],
        "result": result
    }