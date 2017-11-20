import math
def checkio(data):
    data = eval(data)
    # coordinates of each point
    x1 = data[0][0]
    y1 = data[0][1]
    x2 = data[1][0]
    y2 = data[1][1]
    x3 = data[2][0]
    y3 = data[2][1]

    # intermediate calculations
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2 * (A * (y3 - y2) - B * (x3 - x2))
    if G == 0:
        quit()

    # coordinates of the center
    cx = (D * E - B * F) / G
    cy = (A * F - C * E) / G

    # radius of the circle
    r = math.sqrt((cx - x1) ** 2 +(cy - y1) ** 2 )
    return "(x-{Cx:.3g})^2+(y-{Cy:.3g})^2={R:.3g}^2".format(Cx=cx, Cy=cy, R=round(r, 2))

print(checkio("(2,2),(6,2),(2,6)"))

