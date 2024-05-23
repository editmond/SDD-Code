import numpy
def solveQuadratic(a,b,c):
    x = 0
    discriminant = b**2 - (4*a*c)
    print(f"Discriminant is: {discriminant}")
    x1, x2= 0,0
    isSolved = True
    if discriminant >= 0:
        x1= (b - numpy.sqrt(discriminant))/(2*a)
        x2= (b - numpy.sqrt(discriminant)) / (2 * a)
    else:
        print("No real solution")
        isSolved = False
    return x1, x2, isSolved

a = int(input("a coefficient: "))
b = int(input("b coefficient: "))
c = int(input("c coefficient: "))
sol1, sol2, isSolved = solveQuadratic(a,b,c)
if isSolved:
    print(f"The two solutions are x={sol1} and x={sol2}")
