cost = 0
gs_flat_charge = 20
gsp_flat_charge = 125
drone_flat_charge = 0

def ground_shipping(weight):
  if weight <= 2:
    cost = (weight * 1.50) + gs_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 2 and weight <= 6:
    cost = (weight * 3) + gs_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 6 and weight <= 10:
    cost = (weight * 4) + gs_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 10:
    cost = (weight * 4.75) + gs_flat_charge
    print ("Your cost is: %s " % cost)
def ground_shipping_premium(weight):
  if weight <= 2:
    cost = (weight * 1.50) + gsp_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 2 and weight <= 6:
    cost = (weight * 3) + gsp_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 6 and weight <= 10:
    cost = (weight * 4) + gsp_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 10:
    cost = (weight * 4.75) + gsp_flat_charge
    print ("Your cost is: %s " % cost)
def drone_shipping(weight):
  if weight <= 2:
    cost = (weight * 4.50) + drone_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 2 and weight <= 6:
    cost = (weight * 9) + drone_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 6 and weight <= 10:
    cost = (weight * 12) + drone_flat_charge
    print ("Your cost is: %s " % cost)
  elif weight > 10:
    cost = (weight * 14.25) + drone_flat_charge
    print ("Your cost is: %s " % cost)

def welcome_shipping():
  print("1- Ground Shipping\n2- Ground Shipping Premium\n3- Drone Shipping")
  question = int(input("Which shipping would you like?"))
  weight = float(input("How many kilos is your package?"))
  if question == 1:
    ground_shipping(weight)
  elif question == 2:
    ground_shipping_premium(weight)
  elif question == 3:
    drone_shipping(weight)
  else:
    print("Error...")

welcome_shipping()
