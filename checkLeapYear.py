#program to check Leap Year or Not

# Method1: check using single line if-else statement
#---------------------------------------------------
year=int(input("Enter the year: "))
result="Leap Year" if year%400==0 else "Leap Year" if year%4==0 and year % 100!=0 else "Not Leap Year"
print(result)


#Method2: check using functions
#----------------------------------------------------
def checkLeap(year):
    if (year%400==0):
        print("Leap Year")
    elif (year%4==0 and year%100!=0):
            print("Leap Year")
    else:
        print("Not Leap Year")
    


while (True):
    def main():
        yr=int(input("Enter the Year: "))
        checkLeap(yr)
       
    if __name__ == "__main__":
        main()

    if input("Continue__(y/n): ")!='y': 
        print("Bye!") 
        break
       
