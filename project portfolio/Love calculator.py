print("Welcome to the love calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
#name1=name1.lower()
#name2=name2.lower()
l=name1.count("l") + name2.count("l")
o=name1.count("o") + name2.count("o")
v=name1.count("v") + name2.count("v")
e=name1.count("e") + name2.count("e")
t=name1.count("t") + name2.count("t")
r=name1.count("r") + name2.count("r")
u=name1.count("u") + name2.count("u")
e=name1.count("e") + name2.count("e")
love = l + o + v + e
true = t + r + u + e
score=str(true) + str(love)
score=int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}. You go together like coke and mentos, fizzzle fizzle!!!")
elif score >= 40 and score <= 50:
    print(f"your score is {score}. Congratulations, you are a good match.")
else:
    print(f"Your score is {score}, just look somewhere else.")
