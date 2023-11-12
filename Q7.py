import random
count=0
while count<=10:
    secrect_num=random.randint(0,1)
    if secrect_num == 0:
        print("Heads")
    else:
        print("Tails")
    count+=1

