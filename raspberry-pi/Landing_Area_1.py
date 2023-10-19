import board




def TriArea(x1,y1, x2,y2, x3,y3):
    area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return int(area)


while True:
    
    print("Point 1 Coordinates:")
    x1 = input()
    y1 = input()
    print("Point 1 Coordinates:")
    x2 = input()
    y2 = input()
    print("Point 1 Coordinates:")
    x3 = input()
    y3 = input()