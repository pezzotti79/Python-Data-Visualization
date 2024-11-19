
# Baseball Chatbot
# This chatbot is designed to answer basic questions about baseball.

def greet():
    print("Hello! I'm your baseball chatbot. Ask me anything about baseball!")
    print("To exit, just type 'exit'.")

def handle_input(user_input):
    responses = {
        "what is baseball": "Baseball is a bat-and-ball game played between two opposing teams who take turns batting and fielding.",
        "rules of baseball": "The main objective is to score runs by hitting the ball and running across a series of four bases arranged in a diamond shape.",
        "tell me about baseball teams": "There are many famous baseball teams, such as the New York Yankees, Los Angeles Dodgers, and Boston Red Sox.",
        "how many players": "Each baseball team has nine players on the field at any given time.",
        "what is a home run": "A home run is when a batter hits the ball out of the park, allowing them to round all the bases and score a run without getting out."
    }
    # Basic response matching
    response = responses.get(user_input.lower(), "I'm not sure about that. Could you ask something else about baseball?")
    return response

def main():
    greet()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Thanks for chatting with me.")
            break
        response = handle_input(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
