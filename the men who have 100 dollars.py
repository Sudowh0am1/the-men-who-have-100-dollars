# this is the Question : there's 50 men and each one has 100 dollar. how much money will remain for each one
# if in every round they borrow exactly 1 dollar to a random person.
# suppose that we do it 200 times. POINT : the one who has zero money will be omitted. 


import random
# import Matplotlib.pyplot as plt

peoples_money = []
for i in range (0, 50):
    # each person has 100 dollars first
    peoples_money.append(100)  

# if we do it 200 times
for cycle in range (0,200):
    for person1 in range (0, 50):
        person2 = random.randrange(0, 50)

        while peoples_money[person2] == 0:
           person2 = random.randrange(0, 50)
        
        if peoples_money[person1] != 0:
            peoples_money[person1] = peoples_money[person1] - 1
            peoples_money[person2] = peoples_money[person2] + 1

print (peoples_money)
