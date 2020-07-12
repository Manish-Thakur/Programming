#program to check for Palindrome

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

#Method3: using index.
#-------------------------------#
def reverse_string(s):
    str= s[::-1]
    return str


def Main():
    string=input("Enter the string: ")
    result=reverse_string(string)
    checkPalindrome = True if string == result else False
    print("-----------------------------")
    print("original string: ",string)
    print("reversed string: ",result)
    print("checkPalindrome: ",checkPalindrome)

if __name__ == "__main__":
    Main()
    

#Output:
#-------------------------------#
# Enter the string:good
# original string: good
# reversed string: doog
# checkPalindrome: False

# Enter the string:radar
# original string: radar
# reversed string: radar
# checkPalindrome: True