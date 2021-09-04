import random
a=random.randint(1,9)
chances=1
while(chances<=5):
    g=int(input("enter the number"))
    if(a==g):
        print("your guess is correct")
        break
    chances=chances-1
if(chances==0):
    print("Try Again.The original number was ",a)