import random

# The Magic 8-Ball is a popular toy developed in the 1850's for fortune-telling or advice seeking.

# Write a program that can answer any Yes or No questions with a different fortune each time it executes.


def magic(name, question):

    answer = ""

    random_number = random.randint(1, 11)

    if random_number == 1:
        answer = "Yes-definitely."
    elif random_number == 2:
        answer = "It is decidedly so."
    elif random_number == 3:
        answer = "Without a doubt."
    elif random_number == 4:
        answer = "Reply hazy, try again."
    elif random_number == 5:
        answer = "Ask again later."
    elif random_number == 6:
        answer = "Better not tell you now."
    elif random_number == 7:
        answer = "My Sources say no."
    elif random_number == 8:
        answer = "Outlook not so good."
    elif random_number == 9:
        answer = "Very doubtful."
    elif random_number == 10:
        answer = "You are fortunate today."
    elif random_number == 11:
        answer = "In your dreams."
    else:
        "Error"

    if len(name) == 0 and len(question) > 0:
        print(f"{question}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif len(question) == 0:
        print("The magic 8-Ball needs your question.")
    else:
        print(f"{name} asks: {question}")
        print(f"Magic 8-Ball's answer: {answer}")


magic("Chirpa", "Will I get bird feed today?")
# magic("", "Will I get bird feed today?")
# magic("", "")
