import math

def main():
    print("This program will calculate the area and circumference of a circle")
    print("and the volume and surface area of a sphere given the radius")
    #getting the radius from user
    r = eval(input("\nEnter the radius: "))
    #using the radius to find other values
    a = math.pi * r ** 2
    
    v = (4 / 3) * math.pi * r ** 3
    
    c = 2 * math.pi * r
    
    sa = 4 * math.pi * r ** 2
    
    #display results
    print("\nArea of the circle:", a)
    print("Circumference of the circle:", c)
    print("Volume of the sphere:", v)
    print("Surface area of the sphere:", sa)

main()
