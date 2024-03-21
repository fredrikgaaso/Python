def main():
    login = {"PGR107": "Python"}
    username_input = input("Enter Username: ")
    password_input = input("Enter Password: ")

    login = login_info(login, username_input, password_input)

    if login:
        print("Welcome " + username_input)
        run_quiz()
    else:
        print("Invalid username and/or password")
        main()


def login_info(login, username, password):
    if username in login and password == login[username]:
        return True
    else:
        return False


def run_quiz():
    quiz_questions = {
        "Q1. What is the capital of Norway?\n(a) Bergen\n(b) Oslo\n(c) Stavanger\n(d) Trondheim\n": "b",
        "Q2. What is the currency of Norway?\n(a) Euro\n(b) Pound\n(c) Krone\n(d) Deutsche Mark\n": "c",
        "Q3. What is the largest city in Norway?\n(a) Oslo\n(b) Stavanger\n(c) Bergen\n(d) Trondheim\n": "a",
        "Q4. When is constitution day (the national day) of Norway?\n(a) 27th May\n(b) 17th May\n(c) 17th "
        "April\n(d) 27th April\n": "b",
        "Q5. What color is the background of the Norwegian flag?\n(a) Red\n(b) White\n(c) Blue\n(d) Yellow\n": "c",
        "Q6. How many countries does Norway border?\n(a) 1\n(b) 2\n(c) 3\n(d) 4\n": "b",
        "Q7. What is the name of the university in Trondheim?\n(a) UiS\n(b) UiO\n(c) NMBU\n(d) NTNU\n": "d",
        "Q8. How long is the border between Norway and Russia?\n(a) 96 km\n(b) 196 km\n(c) 296 km\n(d) 396 km\n": "c",
        "Q9. Where in Norway is Stavanger?\n(a) North\n(b) South\n(c) South-west\n(d) South-east\n": "c",
        "Q10. From which Norwegian city did the world’s famous composer Edvard Grieg come?\n(a) Oslo\n(b) "
        "Bergen\n(c) Stavanger\n(d) Tromsø\n": "b"
    }
    wrong_answers = {}
    score = 0
    for question, answers in quiz_questions.items():
        user_answer = input(question + "\nYour answer: ").lower()
        if user_answer in answers:
            score += 1
        else:
            wrong_answers[question] = (user_answer, answers)
    print("You got", score, "out of", len(quiz_questions), "correct.")

    if score < len(quiz_questions):
        print("Here are the correct answers for the questions you answered wrong:\n")
        for question, (user_answer, correct_answer) in wrong_answers.items():
            print("Question:", question)
            print("Your answer:", user_answer)
            print("Correct answer:", correct_answer)
            print()
    else:
        print("You got everything correct!")

    print("Do you want to take the test again? y/n")
    answer = input().lower()
    if answer == "y":
        run_quiz()
    else:
        print("Thanks for playing!")


main()
