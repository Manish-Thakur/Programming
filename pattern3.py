# program to print a pattern

n=int(input("Enter the limit: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=n+1-i:        #check condition, if true then print star else print space
            print("*",end='')
        else:
            print(" ",end='')

    print()                 #this will print a new line



    '''
output
------------------
Enter the limit: 5
    *
   **
  ***
 ****
*****
------------------
'''