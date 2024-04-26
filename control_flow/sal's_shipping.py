# Sal Shipping

# Sal runs a shipping company and wants to find the best deal for his cumstomers
# wants to find cheapest way to ship items: ground, ground premium, or drone

weight = 8.4
price_ground = 0

# ground shipping
if weight <= 2:
  price_ground = 1.50 * weight + 20
elif weight <= 6:
  price_ground = 3.00 * weight + 20
elif weight <= 10:
  price_ground = 4.00 * weight + 20
else:
  price_ground = 4.75 * weight + 20

print("Ground Shipping Price $", price_ground)

# pemium ground shipping 
price_premium_ground = 125
print("Ground Shipping Premium $", price_premium_ground)

# drone shipping

