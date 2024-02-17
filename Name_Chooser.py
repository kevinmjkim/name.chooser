import random
import os

import time
print(os.path.exists("/Users/kevinkim/Documents/GitHub/names.txt"))
my_list = []


with open("/Users/kevinkim/Documents/GitHub/names.txt","r") as my_file:
    for line in my_file:
        print("Welcome to Name Generator")
        response = input("type yes or no to generate name")
        if response == "yes":
            my_list.append(line.strip())
            cpu_choice = random.choice(my_list)
            print(cpu_choice)
            time.sleep(2)
        elif response == "no":
            
         
           print("Why you even type this?!")
           time.sleep(2)
         




'''

my_list = []
                
my_list.append(1)
my_list.append(17)                        
my_list.append(420692)

print (my_list)
print(my_list[-4])


print(len(my_list))
'''

