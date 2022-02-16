import random


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements using the Comparative Operator == Equal to in order to display gas level messages
def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU HAVE RUN OUT OF GAS***\n     Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING YOU HAVE ALMOST RUN OUT OF GAS***\n     THE CLOSEST GAS STATION IS")
    elif gasLevelIndicator == " Quarter Tank":
        print("You are on a QUARTER TANK of gas\nStart Planing a Trip to The Gas Station!!!")
    elif gasLevelIndicator == " Half Tank":
        print("You are on a HALF TANK of gas\nYou have 125 more miles to empty")
    elif gasLevelIndicator == " Three Quarter Tank":
        print("You have a Three Quarters Tank of gas\nKeep on trucking away with your 200 miles of gas")
    else:
        print("You have a FULL of gas\nCongrats you just spent who knows how long out side for some gasoline")


# Call Functions Here
gasLevelAlert()