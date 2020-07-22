#program to print a pattern

n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n+1-i:
            print("*",end='')
        else:
            print(" ",end='')

    print()


    
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