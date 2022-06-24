# This program checks if a given israeli ID is valid number using the "check digit" system
# 
# @author: Gilad Samuel
# @version: 1.1.0

def sum_digits(n):                                      # return the sum of digits of a number
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

check_list = [1,2,1,2,1,2,1,2,1]
check_sum = 0
id_list = []

ID = input("please type your ID: ")

if len(ID) != 9:                                         # ID don't have 9 digits
    print("ID shold be 9 digits")
    
elif not ID.isdigit():                                   # ID isn't a number
    print("Illegal ID, all digits need to be numbers")
    
else: 
    ID = int(ID)                                          # change ID variable from str to int

    while ID:                                             # put all digits of ID in a list
        id_list.insert(0, ID % 10)
        ID //=10

    for x in range(9):                                    # multiply ID digits with check_list digits
        temp = check_list[x] * id_list[x] 
        
        if temp <=9:                                      # if result of a multiply greater then 9, sum of digits insted
            check_list[x] = temp                          
        else:
             check_list[x] = sum_digits(temp)             
    
    for x in check_list:                                  # sum results
        check_sum += x

    if check_sum % 10 == 0:                               # if sum divided by 10 with no remainder, ID valid
        print("ID number is valid")        
    else: 
        print("ID number is not valid")