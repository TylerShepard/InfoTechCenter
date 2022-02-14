import random

# Gas level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quater Tank","Half Tank","Three Quarters Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)

gasLevelGauge()



