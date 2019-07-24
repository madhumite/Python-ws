'''accept number from user then find series'''

n = int(input("Enter the number"))
sum=0.0
if n>0:
   for i in range(1,n+1):
      sum+=1/(i*i*i)
      
print(f"result is{sum}")