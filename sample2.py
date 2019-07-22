import random as rn
gram=rn.randint(1,6)
count = 0
while True:
   num=int(input("Enter the number"))
   if num==gram:
      count+=1
      print(f"You guessed right number in {count} attempt")
      break
   elif num>gram:
      count+=1
      print("Number guessed is greater")
   else:
      count+=1
      print("Number guessed is smaller")
   if count==3:
      print("Better luck next time")
      break