#Write a function that uses while, 
#if and continue statements to print all the even numbers between 0 and 50. 

def even_numbers():
   x=0
   while  x<=50:
      if x%2==0:
       print(x)
      x+=1 
      continue
   
#Write a function that takes an integer argument
#  and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.
def argument(num):
   if  num<2:
    print("Not prime")
   elif num>2:
     x=range(2,num)
   for i in x:
      if num%i==0:
         print('not Prime')
         break
   else:
      print("Prime")

#Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def integers (nums):
   sum=0
   for num in nums:
    if num%2==0:
      sum+=num
      
   print(sum)

#Write a function that takes any two integers as input,
# and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_3(num1, num2):
    total = 0
    for num in range(num1, num2+1):
        if num % 3 == 0:
            total += num
    print("The sum of numbers between", num1, "and", num2, "divisible by 3 is:", total)