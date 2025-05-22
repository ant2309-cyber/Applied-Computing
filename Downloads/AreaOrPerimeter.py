def area(length, width):
    shapeArea = length * width
    print("Area = ",shapeArea)

def perimeter(length, width):
    shapePerimeter = 2 * (length + width)
    print ("Perimeter = ", shapePerimeter)
#What is the length and width
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

#Ask for area or perimeter
Measurement = input("What would you like perimeter or area: ")

if Measurement == 'area':
    area(length, width)
elif Measurement == 'perimeter':
    perimeter(length, width)
else:
    print("No pick area or perimeter")       
