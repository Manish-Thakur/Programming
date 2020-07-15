#prograam to print a pattern

n=int(input("Enter the limit: "))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end='')
    print('\n')


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
     
        
    

