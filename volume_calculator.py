import math
print('Shape Volume Calculator')
print('-'*20)
print('1.Caculate Volume of a Cone.')
print('2.Caculate Volume of a Cube.')
print('3.Caculate Volume of a Cylinder.')

shape = str(input('Choose 1, 2, 3: '))
if shape == "1":
   coneHeight = float(input('Enter the height of the cone: '))
   coneRad = float(input("Enter the Radius of the Cone: "))
   volCone = (math.pi * (coneRad*coneRad) * coneHeight/3)
   print("The Volume is ",volCone)
elif shape == "2":
    length = float(input('Enter the Length of the cube: '))
    volCube = (length*length*length)
    print("The Volume is ",volCube)
elif shape == "3":
    radCylinder = float(input('Enter the Radius of the cylinder: '))
    cyHeight = float(input('Enter the Height of the cylinder'))
    volCylinder = (math.pi * radCylinder*radCylinder*cyHeight)
    print("The Volume is: ",volCylinder)
else:
    print('Error: Entered a wrong number. Program Ending')
    
    
