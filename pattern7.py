#program to print a pattern

n=int(input("Enter the input: "))
for i in range(1,n+1):
    for j in range(1,2*n):
        if j>=i and j<=2*n-i:
            print("*",end='')

        else:
            print(" ",end='')
        

    print()


    
    '''
output
------------------
Enter the limit: 5

    *********
     *******
      *****
       ***
        *
   
------------------
'''