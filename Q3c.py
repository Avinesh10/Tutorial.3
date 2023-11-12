cost=int(input("Enter the cost of the meal "))
satis=input("Rate how satisfied are you with the dinner. 1=very satisfied,2 = satisfied , 3 = dissatisfied ")
if satis == "1":
    cost = cost*120/100
elif satis =="2":
    cost = cost*115/100
else:
    cost = cost*110/100
print("Your total bill is ", cost)