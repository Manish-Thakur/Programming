#program to print pattern

n=int(input("Enter the limit: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end='')

    print("\n")

'''
output
------------------
Enter the limit: 5
*****
****
***
**
*
------------------
'''