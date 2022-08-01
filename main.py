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
done = False
money = 0.0

def report():
  print(f"Water: {resources['water']}ml")    
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: {money}")
def check_resources(ingredients):
  resources_needed = True
  for resource in resources:
    if resources[resource] < ingredients[resource]:
      print("failed")
      resources_needed = False
  if resources_needed:
    for resource in resources:
      resources[resource] = resources[resource] - ingredients[resource]
    print(f"Here is your {choice}!")


while(done == False):
  choice = input("What would you like (expresso/latte/cappuccino): ")
  if choice == 'off':
    done = True
  elif choice == 'report':
    report()
  else:
    check_resources(MENU[choice]['ingredients'])
