import board

def TriArea(x1,y1,x2,y2,x3,y3):
    try:
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return area
    except:
        print("Invalid Coordinates")
        area = 0
        return area

while True:
    
    print("Point 1 Coordinates (x,y):")
    p1 = input()
    x1, y1 = p1.split(",")
    print(f"Point 1: ({p1})")

    print("Point 2 Coordinates (x,y):")
    p2 = input()
    x2, y2 = p2.split(",")
    print(f"Point 2: ({p2})")

    print("Point 3 Coordinates (x,y):")
    p3 = input()
    x3, y3 = p3.split(",")
    print(f"Point 3: ({p3})")

    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    
    area = TriArea(x1,y1,x2,y2,x3,y3)
    print(" ")
    print(f"AREA IS: {area}")
    print(" ")