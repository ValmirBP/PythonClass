import math
print('{:=^50}'.format(' CHALLENGE 011 '))

print('write a software that calculate the meter square of a wall and calculate how munch liters of paint is necessary  as well')

shape = input (' Please write the shape  of the please \n consider:\n T = riangle \n R = Rectangle \n S = Square \n L = Losangle \n TR =  Trapeziun \n C = Circle \n ' )


match shape:
    case "t":
        print("You choose Triangle")
        basis = int(input(' input the Basis of the Triangle in meters: '))
        height = int(input(' input the height of the triangle in meters: '))
        area = (basis*height)/2
        paitQnt = area/2
        print('the Area of this triangle is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "T":
        print("You choose Triangle")
        basis = int(input(' input the Basis of the Triangle in meters: '))
        height = int(input(' input the height of the triangle in meters: '))
        area = (basis*height)/2
        paitQnt = area/2
        print('the Area of this triangle is {}m² \nthe quantity needed is {} '.format (area,paitQnt))
                
    case "r":
        print("You choose Rectangle")
        basis = int(input(' input the Basis of the Rectangle in meters: '))
        height = int(input(' input the height of the Rectangle in meters: '))
        area = (basis*height)
        paitQnt = area/2
        print('the Area of this Rectangle is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "R":
        print("You choose Rectangle")
        basis = int(input(' input the Basis of the Rectangle in meters: '))
        height = int(input(' input the height of the Rectangle in meters: '))
        area = (basis*height)
        paitQnt = area/2
        print('the Area of this Rectangle is {}m² \nthe quantity needed is {} '.format (area,paitQnt))
        
    case "s":
        print("You choose Square")
        basis = int(input(' input the Basis of the Square in meters: '))
        height = int(input(' input the height of the Square in meters: '))
        area = (basis*height)
        paitQnt = area/2
        print('the Area of this Square is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "S":
        print("You choose Square")
        basis = int(input(' input the Basis of the Square in meters: '))
        height = int(input(' input the height of the Square in meters: '))
        area = (basis*height)
        paitQnt = area/2
        print('the Area of this Square is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "l":
        print("You choose Losangle")
        smallerDiagonal = int(input(' input the smallest Diagonal of the Losangle in meters: '))
        biggerDiagonal = int(input(' input the Bigest Diagonal of the Losangle in meters: '))
        area = (biggerDiagonal*smallerDiagonal)/2
        paitQnt = area/2
        print('the Area of this Losangle is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "L":
        print("You choose Losangle")
        smallerDiagonal = int(input(' input the smallest Diagonal of the Losangle in meters: '))
        biggerDiagonal = int(input(' input the Bigest Diagonal of the Losangle in meters: '))
        area = (biggerDiagonal*smallerDiagonal)/2
        paitQnt = area/2
        print('the Area of this Losangle is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "tr":
        print("You choose Trapeziun")
        smallerBasis = int(input(' input the smallest Basis of the Trapeziun in meters: '))
        biggerBasis = int(input(' input the Bigest Basis of the Trapeziun in meters: '))
        height = int(input(' input the height of the Trapeziun in meters: '))
        area = (biggerBasis+smallerBasis)*height/2
        paitQnt = area/2
        print('the Area of this Trapeziun is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "TR":
        print("You choose Trapeziun")
        smallerBasis = int(input(' input the smallest Basis of the Trapeziun in meters: '))
        biggerBasis = int(input(' input the Bigest Basis of the Trapeziun in meters: '))
        height = int(input(' input the height of the Trapeziun in meters: '))
        area = (biggerBasis+smallerBasis)*height/2
        paitQnt = area/2
        print('the Area of this Trapeziun is {}m² \nthe quantity needed is {} '.format (area,paitQnt))

    case "c":
        print("You choose Circle")
        diameter = int(input(' input the Diameter of the Circle in meters: '))
        radius =  diameter/2
        area = radius**2*math.pi
        paitQnt = area/2
        print('the Area of this Circle is {:.2f}m² \nthe quantity needed is {:.2f} '.format (area,paitQnt))

    case "C":
        print("You choose Circle")
        diameter = int(input(' input the Diameter of the Circle in meters: '))
        radius =  diameter/2
        area = radius**2*math.pi
        paitQnt = area/2
        print('the Area of this Circle is {:.2f}m² \nthe quantity needed is {:.2f} '.format (area,paitQnt))
        
    case _:
        print("Sorry try again")


print('{:=^50}'.format(' CHALLENGE 011 END '))

