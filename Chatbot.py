import random

def chatbot():
    print("Hello! I am a chatbot. How can I assist you today? [You can use 'help' to know more]")
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
            break

def get_response(user_input):
    greetings = ["Hi!", "Hello!", "Hey there!"]
    farewells = ["Goodbye!", "Bye!", "See you later!"]
    jokes = ["Why don't scientists trust atoms? Because they make up everything!", 
             "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
             "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    
    if user_input.lower() == "hello" or user_input.lower() == "hi":
        return random.choice(greetings)
    elif user_input.lower() == "how are you":
        return "I'm good, thank you! How about you?"
    elif user_input.lower() == "tell me a joke":
        return random.choice(jokes)
    elif user_input.lower() == "bye":
        return random.choice(farewells)
    elif user_input.lower(). == "guess age":
        guess_age()
    elif user_input.lower(). == "count":
        count()
    elif user_input.lower(). == "test my knowledge":
        test()
    else:
        return "Sorry, I didn't understand. Can you please rephrase?"

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of driving your age by 3, 5 and 7.")
    
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 + 0 + rem5*21 +rem7*15) % 105
    
    print("Your age is {0}; that's good time to start programming!".format(age))
    
def count():
    print("Now I will gave you that I can count to any number you want.")
    num = int(input())
    
    counter = 0
    while counter<=num:
        print("{0} !".format(counter))
        counter += 1
        
def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods ?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To demonstrate the execution of a program.")
    print("4. To interrupt the execution of a program.")
    
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
    
    print("Completed, have a nice day!")
    

# Start the chatbot
chatbot()
