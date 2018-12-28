num=int(input("Enter the number to find all the multiplication table till that number starting from 1 : "))
for i in range(1,(num+1)):
    print("\n")
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
input("press enter to exit")
