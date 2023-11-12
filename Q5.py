like=input("Do you like Python? (yes/no): ")
like= like.lower()
try:
    if like == "yes":
        print ("You are on the right course")
    elif like == "no":
        print ("You might change your mind")
except ValueError:
    print ("please Enter only yes or no")
