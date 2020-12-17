gs_flat_charge = 20
premium_gs_flat_charge = 125

def ground_shipping(weight):
  if weight <= 2:
    return (weight*1.5) + gs_flat_charge
  elif weight > 2 and weight <= 6:
    return (weight*3) + gs_flat_charge
  elif weight > 6 and weight <= 10:
    return (weight*4) + gs_flat_charge
  else:
    return (weight*4.75) + gs_flat_charge

def drone_shipping(weight):
  if weight <= 2:
    return weight*4.5
  elif weight > 2 and weight <= 6:
    return weight*9
  elif weight > 6 and weight <= 10:
    return weight*12
  else:
    return weight*14.25


def cheapest(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_gs_flat_charge

  if ground < drone and ground < premium:
    return "Ground shipping is cheapest. It would cost $" +ground+ "."
  elif drone < ground and drone < premium:
    return "Drone shipping is cheapest. It would cost $" +drone+ "."
  else:
    return "Premium ground shipping is cheapest. It would cost $" +str(premium)+ "."
