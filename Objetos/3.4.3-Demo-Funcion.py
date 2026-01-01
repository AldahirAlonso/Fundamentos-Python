def circumference(radius):
  pi = 3.14
  circumferenceValue = pi * radius * 2
  return circumferenceValue
def printCircumference(radius):
  myCircumference = circumference(radius)
  print ("Circumference of a circle with a radius of " + str(radius) + " is " + str(myCircumference))


radius1 = 2
radius2 = 5
radius3 = 7

printCircumference(radius1)
printCircumference(radius2)
printCircumference(radius3)
