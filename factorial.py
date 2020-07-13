#program to print the factorial of a number

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def Main():
    num=int(input("Enter the number: "))
    result=factorial(num)
    print("Factorial: ",result)

if __name__ == "__main__":
    Main()
     
# #Output:
#------------------#
# Enter the number: 5
# Factorial = 120


