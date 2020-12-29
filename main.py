# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
line = "=============="
print(names)
print (line)
print (len(names))
print (line)
max_list = len(names) - 1
print (f"Max list : {max_list}")
pay = random.randint(0,max_list)
payp = names[pay]
print (line)
print (f"{payp} is going to pay for meal")