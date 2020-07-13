#program to print first N natural numbers

def first_N(num):
    sum=0
    print("First "+str(num) +" Natural Numbers: ")
    for i in range(0,num,+1):
        sum+=1
        print(sum)

#program to print N natural numbers in reverse order

def first_N(num):
    sum=num
    print("First ", num , " Natural numbers in reverse: ")
    for i in range(num,0,-1):
        print(sum)
        sum-=1
        

def main():
    n=int(input("Enter the limit: "))
    first_N(n)


if __name__ == "__main__":
    main()