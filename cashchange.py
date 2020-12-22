counter = 0
change = 0
print("How much does your item cost?")
price = float(input())
print("How much money did you pay?")
paid = float(input())
if paid > price:
    change = paid - price
    print("the change is:")
    print("####################")
    if change - 100 >= 0:
        while change - 100 >= 0:
            change = change - 100
            counter = counter + 1
        print("hundred euro bills: ", counter)
        counter = 0
    if change - 50 >= 0:
        while change - 50 >= 0:
            change = change - 50
            counter = counter + 1
        print("fifty euro bills: ", counter)
        counter = 0
    if change - 20 >= 0:
        while change - 20 >= 0:
            change = change - 20
            counter = counter + 1
        print("twenty euro bills: ", counter)
        counter = 0
    if change - 10 >= 0:
        while change - 10 >= 0:
            change = change - 10
            counter = counter + 1
        print("ten euro bills: ", counter)
        counter = 0
    if change - 5 >= 0:
        while change - 5 >= 0:
            change = change - 5
            counter = counter + 1
        print("five euro bills: ", counter)
        counter = 0
    if change - 2 >= 0:
        while change - 2 >= 0:
            change = change - 2
            counter = counter + 1
        print("two euro coins: ", counter)
        counter = 0
    if change - 1 >= 0:
        while change - 1 >= 0:
            change = change - 1
            counter = counter + 1
        print("one euro coins: ", counter)
        counter = 0
    if change - 0.5 >= 0:
        while change - 0.5 >= 0:
            change = change - 0.5
            counter = counter + 1
        print("fifty cent coins: ", counter)
        counter = 0
    if change - 0.20 >= 0:
        while change - 0.20 >= 0:
            change = change - 0.20
            counter = counter + 1
        print("twenty cent coins: ", counter)
        counter = 0
    if change - 0.10 >= 0:
        while change - 0.10 >= 0:
            change = change - 0.10
            counter = counter + 1
        print("ten cent coins: ", counter)
        counter = 0
    if change - 0.05 >= 0:
        while change - 0.05 >= 0:
            change = change - 0.05
            counter = counter + 1
        print("five cent coins: ", counter)
        counter = 0
    if change - 0.02 >= 0:
        while change - 0.02 >= 0:
            change = change - 0.02
            counter = counter + 1
        print("two cent coins: ", counter)
        counter = 0
    if change - 0.01 >= 0:
        while change - 0.01 >= 0:
            change = change - 0.01
            counter = counter + 1
        print("one cent coins: ", counter)
        counter = 0
elif paid == price:
    print("Just the right amount of money")
else:
    print("Not enough money")