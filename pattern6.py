#program to print a pattern

n=int(input("Enter the input: "))
for i in range(1,n+1):
    for j in range(1,2*n):
        if j>=n+1-i and j<=(((n+1)/2)+1)+i:
            print("*",end='')

        else:
            print(" ",end='')
        

    print()


    
    '''
output
------------------
Enter the limit: 5

        *
       ***
      *****
     *******
    *********
   
------------------
'''