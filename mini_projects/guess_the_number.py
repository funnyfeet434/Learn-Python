import random
random.seed()
random_number = random.randrange(1, 6) 

print("I have rolled a six-sided die. Can you guess the number?")

i = 3
while i>0:
  print("You may guess " + str(i) + " times.")
  guessed_number = input()
  if guessed_number == str(random_number):
      print("Yes! The number is " + str(random_number) + ".")
      break
  i -= 1
  if i > 0: 
      print("No, that's not it. Please try again.")
  else: 
      print("Still wrong. The number was " + str(random_number) + ".")
