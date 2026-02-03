import random
def guess_number_game():
    print("Welcome to the Guess the Number Game!")
    print("Enter the  number in the range (1<=number<=1000)")
    computer_value= random.randint(1, 1000)
    count = 0
    while  True:
         user_input = int(input("Try again! Enter your guess: "))
         count += 1
         if(user_input == computer_value):
          print("Congratulations! You've guessed the correct number!", computer_value)
         
          break
         else:
          if(user_input > computer_value) :
                print("Sorry, that's incorrect, the correct number is less than:", user_input)
              
          elif(user_input < computer_value):
             print("Sorry, that's incorrect. The correct number is greater than:", user_input)
            
         
         
    print("You guessed the number in", count, "attempts.")

guess_number_game()