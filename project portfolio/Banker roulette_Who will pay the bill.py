import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
x = len(names)
ran = random.randint(0, x-1)
person_who_will_pay = names[ran]
print(person_who_will_pay.title() + " is going to buy the meal today. ")
