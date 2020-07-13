#program to print multiplication table of given number

def mutliply_no(n,l):
    print("Multiplication table of",n,"is: ")
    for i in range(1,l+1):
        print(n,"X",i,"=",n*i)

def Main():
    n=int(input("Enter the number: "))
    l=int(input("Enter the limit: "))
    mutliply_no(n,l)



if __name__ == "__main__":
    Main()


# #Output:
# #---------------------#
# input: Enter the number= 2
# input: Enter the limit= 10
# Multiplication table of 2 is:
# 2X1=2
# 2X2=4
# 2X3=6
# 2X4=8
# 2X5=10
# 2X6=12
# 2X7=14
# 2X8=16
# 2X9=18
# 2X10=20