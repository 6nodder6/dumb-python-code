import time
import random
finished = 1
number_list = []
while finished == 1:
    total_numbers = input("How many numbers do you want to sort? \n")
    numberrange_min = int(input("What is the lowest number allowed? \n"))
    numberrange_max = int(input("what is the highest number allowed? \n"))
    total_numbers = int(total_numbers)
    progress = 0
    while progress < total_numbers:
        random_number = random.randint(numberrange_min, numberrange_max)
        number_list.append(random_number)
        progress = progress + 1
    print("Your random number set is: ", number_list)
    time.sleep(.5)
    #considered using sorted() but it doesn't fit the constraints of the problem
    x = 0
    highest_number = (number_list[0])
    while int(x) < int(total_numbers):
        current_val = int(number_list[x])
        print("The current number is: ", current_val)
        x = x+1
        if int(current_val) >= int(highest_number):
            highest_number = current_val
            print("The current highest number is ", highest_number)
        else:
            print("The current highest number (",highest_number,") is larger than this value (",current_val,")")
    finished = 0
print("THE HIGHEST NUMBER HAS BEEN SELECTED!")
time.sleep(1)        
print("\nthe highest number is: ", highest_number)
