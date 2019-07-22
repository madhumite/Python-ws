def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  
 
num = int(input("Enter the number"))  
 #temp=0
if num <= 0:  
   print("Cannot find fibonacci")  
else:  
   print("Fibonacci series:")  
   for i in range(num):
       #temp=fibo(i)
       print(fibo(i))

