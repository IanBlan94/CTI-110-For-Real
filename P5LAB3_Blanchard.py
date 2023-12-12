#CTI-110
#P5LAB3
#Blanchard
#11/7/23
import random
def welcome_message():
    print("Welcome to the Quiz Game!")
    print("Answer the questions correctly and see your score at the end.")
def get_question_and_answer(question_set):
    question, answer = random.choice(question_set)
    return question, answer
def ask_question(question):
    print(question)
    user_answer = input("Your answer: ")
    return user_answer
def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        return True
    return False
def show_score(score):
    print(f"Your current score is: {score}")
def goodbye_message(score):
    print("Thank you for playing!")
    print(f"Your final score is: {score}")
# Define your question set here
question_set = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest ocean in the world?", "Pacific"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci")
]
# Main function
def main():
    welcome_message()
    score = 0
    for _ in range(3): # Change the range to the number of questions you want to ask
        question, answer = get_question_and_answer(question_set)
        user_answer = ask_question(question)
        if check_answer(user_answer, answer):
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
        show_score(score)

    goodbye_message(score)
# Run the main function
def ask_to_repeat():
    repeat = input("Would you like to repeat the quiz? (yes/no): ")
    if repeat.lower() == "yes":
        return True
    return False
main()















