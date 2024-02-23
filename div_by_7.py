num = 0
while (True):

    num = int(input("Enter the number"))
    if (num%7==0):
        print("Num div by 7")
       
    else:
        print("Num not div by 7")
        
    user_input = input("Enter 'yes' to continue or 'no' to quit: ")
    if user_input.lower() == 'no':
        break