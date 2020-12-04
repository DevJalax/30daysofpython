l1 = [] 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 

	l1.append(ele) # adding the element 
        l1.sort()
	
max=l1[n-1]
min=l1[0]
l1.pop(1)  #removing an element
print("Maximum no is ",max)
print("Minimum no is ",min) 
