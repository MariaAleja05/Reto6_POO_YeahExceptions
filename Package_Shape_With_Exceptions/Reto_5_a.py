from paquete_5a.shape import Point
from paquete_5a.shape import Isosceles
from paquete_5a.shape import Equilateral
from paquete_5a.shape import Scalene
from paquete_5a.shape import TriRectangle
from paquete_5a.shape import Square

# Exception handling
try:
    def t_isoceles():       # To test isosceles triangle
        A = Point(0,0)
        B = Point(4,0)
        C = Point(2,3)
        isosceles=Isosceles(True, [A,B,C], [], [])
        edges_isoceles = isosceles.compute_edges()
        inner_angles_isoceles = isosceles.compute_inner_angles()
        perimeter_isosceles = isosceles.compute_perimeter()
        area_isosceles = isosceles.compute_area()
        print("\nIsosceles Triangle:")
        print("Edges: ", edges_isoceles)
        print("Inner angles: ", inner_angles_isoceles)
        print("Perimeter: ", perimeter_isosceles)
        print("Area: ", area_isosceles)

    def t_equilateral():    # To test equilateral triangle
        A = Point(0,0)
        B = Point(3,0)
        C = Point(1.5,2.598)
        equilateral=Equilateral(True, [A,B,C], [], [])
        edges_equilateral = equilateral.compute_edges()
        inner_angles_equilateral = equilateral.compute_inner_angles()
        perimeter_equilateral = equilateral.compute_perimeter()
        area_equilateral = equilateral.compute_area()
        print("\nEquilateral Triangle:")
        print("Edges: ", edges_equilateral)
        print("Inner angles: ", inner_angles_equilateral)
        print("Perimeter: ", perimeter_equilateral)
        print("Area: ", area_equilateral)

    def t_scalene():        # To test scalene triangle
        A = Point(-1,2)
        B = Point(3,0)
        C = Point(0,-3)
        scalene=Scalene(True, [A,B,C], [], [])
        edges_scalene = scalene.compute_edges()
        inner_angles_scalene = scalene.compute_inner_angles()
        perimeter_scalene = scalene.compute_perimeter()
        area_scalene = scalene.compute_area()
        print("\nScalene Triangle:")
        print("Edges: ", edges_scalene)
        print("Inner angles: ", inner_angles_scalene)
        print("Perimeter: ", perimeter_scalene)
        print("Area: ", area_scalene)

    def t_trirectangle():   # To test right triangle
        A = Point(-1,2)
        B = Point(3,0)
        C = Point(0,-3)
        trirectangle=TriRectangle(True, [A,B,C], [], [])
        edges_rectangle = trirectangle.compute_edges()
        inner_angles_trirectangle = trirectangle.compute_inner_angles()
        perimeter_trirectangle = trirectangle.compute_perimeter()
        area_trirectangle = trirectangle.compute_area()
        print("\nRight Triangle:")
        print("Edges: ", edges_rectangle)
        print("Inner angles: ", inner_angles_trirectangle)
        print("Perimeter: ", perimeter_trirectangle)
        print("Area: ", area_trirectangle)

    def r_square():         # To test square
        A = Point(0,0)
        B = Point(0,4)
        C = Point(4,4)
        D = Point(4,0)
        square=Square(True, [A,B,C,D], [], [])
        edges_square = square.compute_edges()
        inner_angles_square = square.compute_inner_angles()
        perimeter_square = square.compute_perimeter()
        area_square = square.compute_area()
        print("\nSquare:")
        print("Edges: ", edges_square)
        print("Inner angles: ", inner_angles_square)
        print("Perimeter: ", perimeter_square)
        print("Area: ", area_square)

    # To show results
    t_isoceles()
    t_equilateral()
    t_scalene()
    t_trirectangle()
    r_square()

except TypeError as error:             # Type error
    print(f"Error: {error}")
except ValueError as error:             # Invalid value
    print(f"Error: {error}")
except IndexError as error:             # List index out of range
    print(f"Error: {error}")
except ImportError as error:             # Import error
    print(f"Error: {error}")
except ZeroDivisionError as error:             # Division by zero
    print(f"Error: {error}")
except AttributeError as error:             # Attribute error
    print(f"Error: {error}")
except Exception as error:              # Other exceptions
    print(f"Error: {error}")