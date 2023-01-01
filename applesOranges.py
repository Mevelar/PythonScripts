print("How many groceries.")

def fruit(apples, oranges, peaches):
    return apples + oranges + peaches

def veggies(carrots, celery, lettuce):
    return carrots + celery + lettuce

def meats(chicken, beef, pork):
    return chicken + beef + pork

f = lambda apples, oranges, peaches : apples + .49 + oranges + .64 + peaches + 2.99
v = lambda carrots, celery, lettuce : carrots + 1.25 + celery + 2.10 + lettuce + .85
m = lambda chicken, beef, pork : chicken + 5.99 + beef + 10.99 + pork + 7.89

print (fruit(5, 3, 6) + veggies(4, 6, 2) + meats(2, 1, 4),"items")
print ("$",(f(5, 3, 6) + v(4, 6, 2) + m(2, 1, 4)))
