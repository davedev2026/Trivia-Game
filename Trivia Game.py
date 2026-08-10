print("Welcome to my Trivia Quiz Game")
print("Pick a number from 1 to 10")
print("Type 'quit' to finish")

questions = {
    1:{"q":"What is the capital of England? ","a":"london"},
    2:{"q":"What does CPU stand for? ","a": "central processing unit"},
    3:{"q":"How many local local governments are in Nigeria? ","a":"774"},
    4:{"q":"The capital of Germany? ","a":"berlin"},
    5:{"q":"The first African(Black person)to win a Nobel price is Prof.? ","a":"wole soyinka"},
    6:{"q":"The longest river in Africa is? ","a":"river nile"},
    7:{"q":"The largest country by landmass is? ","a":"russia"},
    8:{"q":"The largest continent by landmass is? ","a":"asia"},
    9:{"q":"Which country is projected to become the 3rd most populous country in the world by 2050? ","a":"nigeria"},
    10:{"q":"The morbid fear of being closed in a confined space is? ","a":"claustrophobia"}
}

score = 0
used_numbers = []

while len(used_numbers) < 10:
    user_input = input(f"Pick a number from 1-10 or type 'quit' to finish: ")

    if user_input.lower() == "quit":
        break

    try:
        pick = int(user_input)
    except ValueError:
        print("please enter a number 1-10 or type 'quit'")
        continue

    if pick < 1 or pick > 10:
        print("That number is not available. Pick 1-10")
        continue

    if pick in used_numbers:
        print("You already picked that one! Pick another😊")
        continue

    used_numbers.append(pick)
    question_data = questions[pick]

    answer = input(question_data["q"] + " ")

    if answer.lower().strip() == question_data["a"]:
        print("correct!\n")
        score += 1
    else:
        print("Incorrect!")
        print("Correct answer:", question_data["a"].title(), "\n")
else:
    print(f"\nYou answered all 10 questions!")
    print(f"Your final score: {score}/10")

print("Thanks for playing!")
print(f"\nYour final score: {score}/{len(used_numbers)}")






