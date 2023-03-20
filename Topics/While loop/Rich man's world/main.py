deposit = int(input())
INTEREST_RATE = 0.071
GUARANTEED_AMOUNT = 700000
number_of_years = 0
total_amount = deposit

while total_amount < GUARANTEED_AMOUNT:
    interest = total_amount * INTEREST_RATE
    total_amount += interest
    number_of_years += 1

print(number_of_years)
