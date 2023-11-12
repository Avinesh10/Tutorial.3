num1= float(input("Enter a number"))
num2= float(input("Enter another number"))
operator= input("Choose the operator + or - or * or /")
try:
    if operator == '+':
        answer= num1 + num2
    elif operator == '-':
        answer= num1 -num2
    elif operator == '*' :
        answer = num1 * num2
    elif operator == '/':
        answer = num1/num2
    else:
        print("Enter a valid number")
    print("Answer is ",answer)    
except ZeroDivisionError:
    print("You cannot divide by zero")
        

