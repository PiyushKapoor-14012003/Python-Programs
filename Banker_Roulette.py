names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person_who_will_pay=names[random_choice]
print(f"{person_who_will_pay} is going to buy the meal today!")
