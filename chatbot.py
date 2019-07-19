# --- Define
def greetingFunction():
    print("Greetings")

def additionalFunction(num1,num2):
    print("I will add 22 numbers")
    answer = num1 + num2
    print(f"the answer is {answer}")

def responsetouser(userAnswer):
    if(userAnswer == 'good'):
        print("I'm happy to hear I'm good too")
    if(userAnswer == 'bad'):
        print("I'm sorry, How can I help")

# --- Put your main program below! ---
def main():
  while True:
    # answer = input("(What will you say?) ")
    # print("That's cool!")

    greetingFunction()


    user_input = input("How are you today ?")
    responsetouser(userAnswer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
