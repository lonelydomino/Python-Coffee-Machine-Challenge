MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
cash = {
  "money": 0.0
}
done = False

def report():
  print(f"Water: {resources['water']}ml")    
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: {cash['money']}")
  
def check_resources(ingredients):
  for resource in resources:
    if resources[resource] < ingredients[resource]:
      print("Not enough resources")
      return False  
  return True  
  
def deduct_resources(ingredients, cost):
  for resource in resources:
    resources[resource] -= ingredients[resource]
  cash['money'] -= cost

def process_coins():
  print("Please insert coins.")
  total = int(input("How many quarters?")) * 0.25
  total += int(input("How many dimes?")) * 0.1
  total += int(input("How many nickles?")) * 0.05
  total += int(input("How many pennies?")) * 0.01
  return total

  
while(done == False):
  choice = input("What would you like (espresso/latte/cappuccino): ")
  if choice == 'off':
    done = True
  elif choice == 'report':
    report()
  else:
    drink = MENU[choice]
    cash['money'] += process_coins()
    if check_resources(drink['ingredients']) and cash['money'] >= drink['cost']:
      deduct_resources(drink['ingredients'], drink['cost'])
      print(f"Here is your {drink}!")
    else:
      print("Not enough resources.")
