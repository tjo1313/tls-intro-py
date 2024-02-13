# Assume you have $1000 in the bank and earn 5% interest annually. What is your
# balance after 5 years?

balance = (1000 * 1.05) * (1.05 ** 4)
print(balance)

#Same problem as aboe but using augmented assignment

balance = 1000 * 1.05    # year1
balance *= 1.05 # year2
balance *= 1.05 # year3
balance *= 1.05 # year4
balance *= 1.05 # year5

print(balance)