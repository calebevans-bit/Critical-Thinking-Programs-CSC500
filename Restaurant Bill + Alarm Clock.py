import numpy as np
#Part 1: Restaurant Bills
food_charge = float(input('Price of food? '))
rates = np.array([0.18,0.07]) #0 represents tip 1 represents tax
print('\nTip and Tax Array =', rates*food_charge)
food_charge = food_charge*(1+rates[0]+rates[1])
print('\nThe total charge is:', food_charge)

#Part 2: Alarm Clock
print('\nTime to set your alarm!')
cur_time = int(input('\nEnter current time ')) #Must be military time, rounded
down_time = int(input('\nEnter hours until alarm '))
alarm = (cur_time+down_time)%24
print('\nThe alarm will go off at', alarm)