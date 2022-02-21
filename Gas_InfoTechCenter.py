import random


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements the Comparative Operator == Equal To in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","Love's","Meijer","Costco","Sunoco"]
    miles = round(random.uniform(1, 25), 2)
    if gasLevelIndicator == "Empty":
        print("   WARNING YOU ARE ON EMPTY\n Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("      WARNING\n Your gas tank is low on gas\n The closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("     You have a quarter tank of gas left\n The closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")

    elif gasLevelIndicator == "Half Tank":
        print("     You have a Half tank of gas left\n You have 126 miles to empty")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("     You have Three quarter tank of gas left\n You have 210 miles to empty")
    else:
     print("     You be FULL of Gas \n You have 310 miles to empty")

# Call Functions Here
gasLevelAlert()