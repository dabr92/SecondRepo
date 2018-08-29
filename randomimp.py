import random
import sys
import os
start = 0
stopp = 100
x = 0
y = 0
rand2 = 0
z = 0
q = 0
w = 100
r = 0
p = 0
rand3 = 0
randtest = 0
i = 0

while random.randrange(start,stopp) !=20:
    print(randtest)


for r in range (q,w):
    rand3 = random.randrange(start,stopp)
    p = p+1
    print(rand3)
print("Det tog ",p,"loopar")


while (rand2!=20):
    rand2 = random.randrange(start,stopp)
    z = z+1
    print(rand2)
print("Det tog ",z,"loopar")



while x==0:
    rand = random.randrange(start, stopp)
    print(rand)
    y = y+1
    if (rand ==20):
        break
print("det tog ",y, "looopar")

print("--------------------------------------------")

print ("Första loopen tog ",y,"rundor.\nAndra loopen tog ",z,"rundor.\nTredje loopen tog ",p,"rundor.\nTillsammans blir det ",y+z+p, "loopar")

print("--------------------------------------------")
#THIS IS