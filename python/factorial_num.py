fact=1
num=int(input("Enter the number to find its factorial : "))
#for i in range(1,(num+1)):
    #fact = fact * i

i=1
while(i<=num):
    fact = fact * i
    i = i+1

    
print("Factorial of a number",num,"is",fact)

input("press enter to exit")
