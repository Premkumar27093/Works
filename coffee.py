print("Write how many ml of water the coffee machine has:")
water_ = int(input())
print("Write how many ml of milk the coffee machine has:")
milk_ = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())
print("Write how many cups of coffee you will need:")
cups_ = int(input())
cup_water = 200
cup_milk = 50
cup_coffee = 15
total_water = water_ // cup_water
total_milk = milk_ // cup_milk
total_beans = coffee_beans // cup_coffee
min_coffee = min(total_water, total_milk, total_beans)
remainder_ = int(cups_ - min_coffee)
if cups_ == min_coffee or cups_ == 0 :
    print("Yes, I can make that amount of coffee")
elif cups_ > min_coffee:
    print("No, I can make only", str(min_coffee), "cups of coffee")
elif min_coffee > cups_ > 0:
    print("Yes, I can make that amount of coffee (and even", str(remainder_), "more than that)")



