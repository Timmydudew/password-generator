import os 
import random
 
random4 = [1234,5678,5679,6066,7058,4056,5554,6023]

def password():
    choice = input("do you want letters or numbers")
    if choice==letter:
       letter = int(input("how many letters"))
    else:
        print("I don't understand ")
      
def function():
    if len(letter)>5 or len(letter)==5:
       print("too much length")
      return password()
    elif len(letter)<4:
       print("number must be four")
     os.system(clear)
      return password()
    elif len(letter)==4:
       random.choice(random4)
      print("that's ur password ")
     os.system(clear)
     return password()
    else:
         print("I don't understand")
    
