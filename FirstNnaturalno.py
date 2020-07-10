#program to print first N natural numbers

def first_N(num):
    sum=0
    print("First "+str(num) +" Natural Numbers: \n")
    for i in range(0,num):
        sum+=1
        print(sum)




def main():
    n=int(input("Enter the limit: "))
    first_N(n)


if __name__ == "__main__":
    main()