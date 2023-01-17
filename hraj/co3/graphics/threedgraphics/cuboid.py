def cuboid_area():
    l=int(input("Enter the length of cuboid"))
    w=int(input("Enter the width of cuboid"))
    h=int(input("Enter the height of cuboid"))
    return 2*(l*w+w*h+l*h) 
print(cuboid_area())
def perimeter_cuboid():
    l=int(input("Enter the length of cuboid"))
    w=int(input("Enter the width of cuboid"))
    h=int(input("Enter the height of cuboid"))
    return 4*(l+w+h)
print(perimeter_cuboid())
