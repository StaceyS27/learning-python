# Write a program that calculates weight of boxer 
# based on what planet they are on/the planets relative gravity
    # which is given in a chart 

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3
planet_weight = 0

# Write an if statement below:
if planet == 1:
  planet_weight = 0.91 * weight
elif planet == 2:
  planet_weight = 0.38 * weight
elif planet == 3:
  planet_weight = 2.34 * weight
elif planet == 4:
  planet_weight = 1.06 * weight
elif planet == 5:
  planet_weight = 0.92 * weight
elif planet == 6:
  planet_weight = 1.19 * weight 

print("Your weight:", planet_weight)      # Your weight: 432.9 
