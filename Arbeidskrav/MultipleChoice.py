questions = [
    "Q1. What is the capital of Norway?\n(a) Bergen\n(b) Oslo\n(c) Stavanger\n(d) Trondheim\n",
    "Q2. What is the currency of Norway?\n(a) Euro\n(b) Pound\n(c) Krone\n(d) Deutsche Mark\n",
    "Q3. What is the largest city in Norway?\n(a) Oslo\n(b) Stavanger\n(c) Bergen\n(d) Trondheim\n",
    "Q4. When is constitution day (the national day) of Norway?\n(a) 27th May\n(b) 17th May\n(c) 17th April\n(d) 27th "
    "April\n",
    "Q5. What color is the background of the Norwegian flag?\n(a) Red\n(b) White\n(c) Blue\n(d) Yellow\n",
    "Q6. How many countries does Norway border?\n(a) 1\n(b) 2\n(c) 3\n(d) 4\n",
    "Q7. What is the name of the university in Trondheim?\n(a) UiS\n(b) UiO\n(c) NMBU\n(d) NTNU\n",
    "Q8. How long is the border between Norway and Russia?\n(a) 96 km\n(b) 196 km\n(c) 296 km\n(d) 396 km\n",
    "Q9. Where in Norway is Stavanger?\n(a) North\n(b) South\n(c) South-west\n(d) South-east\n",
    "Q10. From which Norwegian city did the world’s famous composer Edvard Grieg come?\n(a) Oslo\n(b) Bergen\n(c) "
    "Stavanger\n(d) Tromsø\n"
]

answers = ["b", "c", "a", "b", "c", "b", "d", "c", "c", "b"]

loginInfo = {"PGR107": "Python"}


def run_quiz(q, a):
    score = 0
    wrong_answers = []
    for i in range(len(q)):
        user_answer = input(q[i] + "\nYour answer: ").lower()
        if user_answer == a[i]:
            score += 1
        else:
            wrong_answers.append((questions[i], user_answer, answers[i]))
    print("You got", score, "out of", len(q), "correct.")

    if score < len(questions):
        print("Here are the correct answers for the questions you answered wrong:\n")
        for question, user_ans, correct_ans in wrong_answers:
            print("Question:", question)
            print("Your answer:", user_ans)
            print("Correct answer:", correct_ans)
            print()
    else:
        print("You got everything correct!")


def login_info():
    username_input = input("Enter Username: ")
    password_input = input("Enter Password: ")
    if username_input in loginInfo and password_input == loginInfo[username_input]:
        run_quiz(questions, answers)
    else:
        print("Invalid username and/or password")
        login_info()


login_info()
