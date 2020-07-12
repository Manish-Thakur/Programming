#program to reverse a given string

#Method1: using recursion.
#-------------------------------#
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+s[0]

#Method2: using loop.
#-------------------------------#
def reverse_string(s):
    str= ""
    for i in s:
        str=i+str

    return str


def Main():
    string=input("Enter the string: ")
    print("original string: ",string)
    result=reverse_string(string)
    print("reversed string: ",result)

if __name__ == "__main__":
    Main()
    

#Output:
#-------------------------------#
Enter the string:good
original string: good
reversed string: doog