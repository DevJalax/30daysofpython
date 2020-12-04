# program to loop through a list of numbers and add +2
list_add=[1,2,3,4,5,6,7,8,9,10]
list1=[]
for x in list_add:
    num=x+2
    list1.append(num)
print(list1)

#patternprog
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#Python Program to Print the Fibonacci sequence
a,b,sum=0,1,0
n=int(input("enter the number"))
for i in range(i,n+1):
    print(sum,end=" ")
    a=b
    b=sum
    sum=a+b

#armstrong

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")




