
import random
import json

trivia_questions = {
    "What is the maximum number of players on the field for one team at a time?": "9",
    "What is it called when a batter swings and misses three pitches?": "strikeout",
    "How many innings are in a standard baseball game?": "9",
    "What position does the player standing behind home plate play?": "catcher",
    "What do you call a home run with the bases loaded?": "grand slam"
}

def greet_user():
    print("Welcome to the Baseball Chatbot!")
    name = input("What's your name? ")
    print(f"Hello, {name}! I can answer your baseball questions or we can play a baseball trivia game.")
    return name

def baseball_faq():
    faq = {
        "home run": "A home run is when the batter hits the ball out of the park in fair territory, scoring a run.",
        "pitcher": "The pitcher is the player who throws the ball to the batter.",
        "catcher": "The catcher is the player who catches pitches the batter doesn't hit and plays behind home plate.",
        "strike": "A strike is when a batter swings and misses or doesn't swing at a ball in the strike zone.",
        "bases loaded": "Bases loaded refers to a situation where there are runners on first, second, and third base."
    }
    question = input("Ask me a baseball question (e.g., 'What is a home run?'): ").lower()
    found = False
    for key, answer in faq.items():
        if key in question:
            print(answer)
            found = True
            break
    if not found:
        print("I'm sorry, I don't know the answer to that question.")

def play_trivia():
    print("Let's play baseball trivia!")
    score = 0
    for question, answer in trivia_questions.items():
        user_answer = input(f"{question} ").lower()
        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{answer}'.")
    print(f"Your final score is {score}/{len(trivia_questions)}.")
    return score

def save_score(name, score):
    try:
        with open("trivia_scores.json", "a") as file:
            file.write(f"{name}: {score}\n")
        print(f"Your score has been saved, {name}!")
    except Exception as e:
        print(f"An error occurred while saving the score: {e}")

def main_chatbot():
    name = greet_user()
    while True:
        choice = input("What would you like to do? (1: Ask a question, 2: Play trivia, 3: Exit) ").strip()
        if choice == "1":
            baseball_faq()
        elif choice == "2":
            score = play_trivia()
            save_score(name, score)
        elif choice == "3":
            print("Goodbye! Thanks for using the Baseball Chatbot.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_chatbot()
