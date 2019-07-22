import random as rn
gram=rn.randint(1,6)
num=int(input())
while(count<=6):
   if num==gram:
      print("Same number")
   elif num>gram:
      print("Number entered is greater")
   elif num<gram:
      print("Number entered is smaller")
   count+=1
