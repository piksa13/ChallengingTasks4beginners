import sys
netAmount = 0
while True:
    s = input('Enter a letter and a number separated by space OR press enter to quit: ')
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass
print(f'The netAmount is {netAmount}')

