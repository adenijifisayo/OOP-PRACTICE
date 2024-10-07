class Microwave:
    def __init__(self, brand: str, price: float, power_rating: str):
        self.brand = brand
        self.price = price 
        self.power_rating = power_rating 
Thermocool = Microwave('Thermocool', 50000, 'B')
smeg = Microwave('smeg', 40000, 'A')
class Fridge:
    def __init__(self, brand: str, price: float, power_rating: str):
        self.brand= brand
        self.price= price
        self.power_rating= power_rating
LG = Fridge('LG', 50000, 'A')
ThermocoolFridge = Fridge('ThermocoolFridge', 50000, 'B')
def e_commerce():
    choice = int(input('what do you want to buy 1 for microwave 2 for fridge'))
    if choice == 1:
        type= int(input('which type of microwave do you want 1 for smeg, 2 for Thermocool'))
        if type == 1:
            print(smeg.brand)
            print(smeg.price)
            print(smeg.power_rating)
        else:
            print(Thermocool.brand)
            print(Thermocool.price)
            print(Thermocool.power_rating)
    else:
        pick = int(input('please input the the type of fridge you want 1 for LG and 2 for Thermocool'))
        if pick == 1:
            print(LG.brand)
            print(LG.price)
            print(LG.power_rating)
        else:
            print(ThermocoolFridge.brand)
            print(ThermocoolFridge.price)
            print(ThermocoolFridge.power_rating)
try:
    e_commerce()
except:
    print('start over and input a correct figure ')