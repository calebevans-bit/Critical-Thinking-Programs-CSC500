#Part 1: Average Rainfall
num_years = int(input('How many years of rainfall? '))
total_rainfall = 0
for i in range(num_years):
    print(f'Year {i+1}')
    for month in range(1,13):
        month_rainfall = float(input(f'Amount of rainfall for month {month} in inches: '))
        total_rainfall += month_rainfall
avg_rainfall = total_rainfall / (num_years * 12)
print(f'\nAmount of months: {num_years * 12}')
print(f'Total rainfall: {total_rainfall} inches')
print(f'Average rainfall: {avg_rainfall:.2f} inches per month')

#Part 2: Bookstore Points
num_books = int(input('How many books have you bought from the CSUG Bookstore this month?: '))
if 0 <= num_books < 2:
    print('\nYou do not have enough books for points this month!')
elif 2 <= num_books < 4:
    print('\nYou have 5 points!')
elif 4 <= num_books < 6:
    print('\nYou have 15 points!')
elif 6 <= num_books < 8:
    print('\nYou have 30 points!')
elif 8 <= num_books:
    print('\nYou have 60 points!')
else:
    print('\nImpossible. Please enter a positive integer!')