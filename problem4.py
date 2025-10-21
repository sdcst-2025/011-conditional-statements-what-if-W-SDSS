#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a > b and a > c:
  hyp = a
  side1 = b
  side2 = c
elif b > a and b > c:
  hyp = b
  side1 = a
  side2 = c
else:
  hyp = c
  side1 = a
  side2 = b

actual = hyp**2
calculated = side1**2 + side2**2
percent = (actual - calculated) / actual*100

if 0 <= percent <= 2:
  print("that is a right triangle")
elif percent <= 0:
  print("that is an acute triangle")
else:
  print("that is an obtuse triangle")
