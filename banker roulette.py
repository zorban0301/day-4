import random
name=input("give everybody's name seperated by a comma: ")
names=name.split(",")
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person_who_will_pay=names[random_choice]
print(f"{person_who_will_pay} is the one who is going to pay for the meal today.")